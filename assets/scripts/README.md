# Using this script

Install dependencies (preferably inside a [virtual environment](https://docs.python.org/3/library/venv.html)):

    cd assets/scripts
    pip install -r requirements.txt

    # or:
    pip install -r assets/scripts/requirements.txt

Run the test suite:

    cd assets/scripts
    pytest

    # or:
    pytest assets/scripts

Update the next semester start date:

- Set the `semester_start_date` parameter of the `main` function to a new date.
- Execute the script from the root directory:

      python assets/scripts/update_week.py
