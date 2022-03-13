"""
Update the status of the (ongoing or not) semester by
writing text in the main README.md file.
"""
from datetime import datetime, timedelta
import fileinput


def main(semester_start_date: datetime = datetime(2022, 4, 4)) -> None:
    """
    Main function to execute. Simply update the date parameter when the
    current semester is done.
    """
    current_date = datetime.today()
    current_week = get_current_week_number(current_date, semester_start_date)
    text_to_display = get_text_to_display(current_week, semester_start_date)
    write_text_to_display_in_readme(text_to_display)


def get_current_week_number(
    current_date: datetime, semester_start_date: datetime
) -> int:
    """
    Return the current week number. Assumes that one day before the next start
    date (Sunday), we set the week number to 1 and any subsequent Sunday is the
    day on which the week is updated.

    Args:
        current_date (datetime): Today's date.
        semester_start_date (datetime): Start date of the semester.

    Returns:
        int: Current week number relative to semester_start_date.
    """
    sunday_start = semester_start_date - timedelta(days=1)

    # If it's Sunday, don't apply a time delta (it would just remove a week)
    # since we update the week number on Sundays.
    sunday_now = current_date - timedelta(days=(current_date.weekday() % 6))

    # Start counting weeks at 1 (not zero even if it's CS so we match week
    # numbers on Coursera ;))
    return int((sunday_now - sunday_start).days / 7 + 1)


def get_text_to_display(
    current_week: int, semester_start_date: datetime
) -> str:
    """
    Returns the text that should be displayed for the status of the current
    week in the README.

    Args:
        current_week (int): Week number as integer.
        semester_start_date (datetime): Start date of the next semester.

    Returns:
        str: Text to display in the README.
    """
    # In between semesters: semester done and announcing next semester start
    if current_week <= 0:
        next_semester_formatted_date = semester_start_date.strftime(
            "%A %-d %B %Y"
        )
        return (
            "- Semester done/ending :tada:. Start date "
            f"of the next semester: **{next_semester_formatted_date}**."
        )

    # Week between 1 and 22 inclusive = semester ongoing
    if current_week <= 22:
        return f"- Week **{current_week}**."

    # It's been a long time since we updated this file... Is it a mistake?
    if current_week > 25:
        url = (
            "https://github.com/world-class/REPL/issues/new?labels=bug"
            "&title=%5BBUG%5D%20Start%20date%20of%20next%20semester%20should%20be"
            "%20displayed%20in%20the%20README"
        )
        return (
            f"- Week **{current_week}**. Did we forget to specify when the next semester"
            f" is starting? Please [let us know by filing an issue]({url})!"
        )

    # Semester done but next semester date not set yet (will be week ≤ 25)
    return f"- Semester done/ending :tada:. [Week: **{current_week}**]"


def write_text_to_display_in_readme(
    text_to_display: str, file_path: str = "README.md"
) -> None:
    """
    Rewrite the line below the heading "Current week" in the README.

    Args:
        text_to_display (str): What should be written in the README
                               (replace existing line).
        file_path (str, optional): Defaults to "README.md".
    """
    skip_lines = 2  # So we leave whitespace intact around the line to change
    current_week_line = False

    # Read each line of the README. When we get to the heading "Current week",
    # we know the line to change will be two lines below (skipping a blank
    # line). Here, "printing" writes to the file in place.
    for line in fileinput.input(file_path, inplace=True):
        line = str(line.rstrip())
        if "# Current week" in line:
            print(line)
            print(f"\n{text_to_display}")
            current_week_line = True
        # If we don't skip lines, we will add new blank lines to the file
        elif current_week_line and skip_lines > 0:
            skip_lines -= 1
            continue
        # Any other original line should be kept
        else:
            print(line)


if __name__ == "__main__":
    main()
