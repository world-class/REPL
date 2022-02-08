# Standard library
from datetime import datetime

# Third-party libraries
import pytest
from hypothesis import example, given, strategies as st


# Local imports
import update_week


@given(
    st.datetimes(
        # Test until Saturday before the first week: Sunday considered week 1
        min_value=datetime(2019, 1, 1),
        max_value=datetime(2021, 10, 9),
    )
)
@example(datetime(2021, 10, 9))
def test_get_current_week_number_returns_non_positive_int_before_semester_has_started(
    current_date: datetime,
):
    """
    Test random dates before starting and force checking for 2 days before.
    Exclude Sunday because we will set the week to 1 on the day before the
    next semester starts.

    Args:
        current_date (datetime): Receive a datetime object from Hypothesis.
    """
    next_semester_start_date = datetime(2021, 10, 11)
    assert (
        update_week.get_current_week_number(
            current_date, next_semester_start_date
        )
        <= 0
    )


def test_get_current_week_number_returns_1_on_Sunday_right_before_semester():
    """
    We want to see "Week 1" on the Sunday when we're about to start the next
    semester.
    """
    next_semester_start_date = datetime(2021, 10, 11)  # Monday
    today = datetime(2021, 10, 10)  # Day before starting, Sunday
    result = update_week.get_current_week_number(
        today, next_semester_start_date
    )
    assert result == 1


@given(
    st.datetimes(
        # Testing from Monday to Saturday (we have a separate test above
        # exclusively for Sunday)
        min_value=datetime(2021, 10, 11),
        max_value=datetime(2021, 10, 16),  # Stop at Saturday: Sunday = Week 2
    )
)
def test_get_current_week_number_returns_1_on_first_week_of_semester(
    current_date: datetime,
):
    """
    Assumes a semester ends at week 22 (included), which has been the case so far.
    Any date within the first week should return 1, EXCLUDING the following
    Sunday, on which day the script updates in advance for the following week.

    Args:
        current_date (datetime): Receive a datetime object from Hypothesis.
    """
    next_semester_start_date = datetime(2021, 10, 11)  # Monday
    result = update_week.get_current_week_number(
        current_date, next_semester_start_date
    )
    assert result == 1


@pytest.mark.parametrize(
    "current_date,expected_week",
    [
        (datetime(2021, 10, 17), 2),  # Monday
        (datetime(2021, 10, 18), 2),  # Monday
        (datetime(2021, 10, 19), 2),  # Tuesday
        (datetime(2021, 10, 24), 3),  # Sunday
        (datetime(2021, 10, 25), 3),  # Monday
        (datetime(2021, 10, 31), 4),  # Sunday
        (datetime(2021, 11, 1), 4),  # Monday
        (datetime(2021, 12, 29), 12),  # Wednesday (last week 2021)
        (datetime(2022, 1, 2), 13),  # Sunday (first week 2022)
        (datetime(2022, 1, 3), 13),  # Monday
        (datetime(2022, 1, 6), 13),  # Thursday
        (datetime(2022, 2, 20), 20),  # Sunday
        (datetime(2022, 3, 7), 22),  # Monday
        (datetime(2022, 3, 13), 23),  # Sunday
        (datetime(2022, 3, 14), 23),  # Monday: semester done
        (datetime(2022, 4, 1), 25),  # Friday
        (datetime(2022, 4, 2), 25),  # Saturday
    ],
)
def test_get_current_week_number_returns_positive_int_when_semester_is_ongoing_or_done(
    current_date: datetime, expected_week: int
):
    """
    Assumes a semester ends at week 22 (included).
    Any date within the ongoing semester should return a positive integer,
    even when the semester is done and the date for the next semester hasn't
    been set.

    Args:
        current_date (datetime): Receive a datetime object from Hypothesis.
    """
    next_semester_start_date = datetime(2021, 10, 11)  # Monday
    result = update_week.get_current_week_number(
        current_date, next_semester_start_date
    )
    assert result == expected_week


@pytest.mark.parametrize(
    "current_week",
    [23, 24, 25],
)
def test_get_text_to_display_returns_correct_text_when_semester_has_ended(
    current_week: int,
):
    semester_start_date = datetime(2021, 10, 11)
    expected_text = (
        f"- Semester done/ending :tada:. [Week: **{current_week}**]"
    )
    result = update_week.get_text_to_display(current_week, semester_start_date)
    assert result == expected_text


@pytest.mark.parametrize(
    "current_week",
    [-2, -1, 0],
)
def test_get_text_to_display_returns_correct_text_when_semester_has_yet_to_start(
    current_week: int,
):
    semester_start_date = datetime(2021, 10, 11)
    next_semester_formatted_date = "Monday 11 October 2021"
    expected_text = (
        "- Semester done/ending :tada:. Start date "
        f"of the next semester: **{next_semester_formatted_date}**."
    )
    result = update_week.get_text_to_display(current_week, semester_start_date)
    assert result == expected_text


@pytest.mark.parametrize(
    "current_week",
    [1, 2, 11, 12, 13, 20, 21, 22],
)
def test_get_text_to_display_returns_correct_text_when_semester_is_ongoing(
    current_week: int,
):
    semester_start_date = datetime(2021, 10, 11)
    expected_text = f"- Week **{current_week}**."
    result = update_week.get_text_to_display(current_week, semester_start_date)
    assert result == expected_text


@given(st.integers(min_value=26, max_value=42))
def test_get_text_to_display_returns_warning_message_if_next_semester_start_date_should_be_updated(
    current_week: int,
):
    """
    If the week number becomes greater than 25, we probably forgot to set the
    next semester date if it is known by that point, so display a message to
    let users know they can file an issue in the repo.

    If we got beyond week 42, there's probably a bigger issue to worry about
    than updating this file, so don't test further...
    """
    semester_start_date = datetime(2021, 10, 11)
    url = (
        "https://github.com/world-class/REPL/issues/new?labels=bug"
        "&title=%5BBUG%5D%20Start%20date%20of%20next%20semester%20should%20be"
        "%20displayed%20in%20the%20README"
    )
    expected_text = (
        f"- Week **{current_week}**. Did we forget to specify when the next semester"
        f" is starting? Please [let us know by filing an issue]({url})!"
    )
    result = update_week.get_text_to_display(current_week, semester_start_date)
    assert result == expected_text


def test_write_text_to_display_in_README(tmpdir):
    # Text we want to put in the README file
    text_to_display = "- Semester done/ending :tada:. [Week: **12**]"

    # Create a test output to store some README content
    file_path = tmpdir.join("output.md")

    # Let's pretend that's all there is in the README
    readme_content = """\
# Have an issue, some feedback or want to contribute?

There are two main ways blabla...

---

# Current week

- Something should be written here...

# • [Frequently Asked Questions (FAQ)](faq/README.md)"""

    # Write that fictional input to the README
    file_path.write(readme_content)

    # Execute the function that should update that content
    update_week.write_text_to_display_in_readme(text_to_display, file_path)

    # This is the new content we should have in that file
    new_readme_content = f"""\
# Have an issue, some feedback or want to contribute?

There are two main ways blabla...

---

# Current week

{text_to_display}

# • [Frequently Asked Questions (FAQ)](faq/README.md)
"""

    # At this point, we should have updated the file correctly
    assert file_path.read() == new_readme_content
