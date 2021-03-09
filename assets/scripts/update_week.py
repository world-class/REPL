from datetime import datetime, timedelta
import fileinput

# This could either be the start date of the current semester or the next one
# if we're already past week 22 in the ongoing semester.
date_start = datetime(2020, 10, 12)

today = datetime.today()

monday_start = date_start - timedelta(days=date_start.weekday())
monday_now = today - timedelta(days=today.weekday())

result = int((monday_now - monday_start).days / 7 + 1)
if result < 1:
    formatted_date = date_start.strftime("%A %-d %B %Y")
    result = (
        "- Semester done/ending :tada:. Start date "
        f"of the next semester: **{formatted_date}**."
    )
elif result > 22:
    result = f"- Semester done/ending :tada:. [Week: **{result}**]"
else:
    result = f"- Week **{result}**."

filename = "README.md"
skip_lines = 2
curr_line = False
for line in fileinput.input(filename, inplace=True):
    line = line.rstrip("\r\n")
    if "# Current week" in line:
        print(line)
        print(f"\n{result}")
        curr_line = True
    elif curr_line and skip_lines > 0:
        skip_lines -= 1
        continue
    else:
        print(line)
