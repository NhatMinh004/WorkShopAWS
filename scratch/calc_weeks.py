import datetime

start_date = datetime.date(2026, 4, 17)
end_date = datetime.date(2026, 7, 30)

print(f"Start: {start_date} ({start_date.strftime('%A')})")
print(f"End: {end_date} ({end_date.strftime('%A')})")

# Let's see how weeks are currently structured.
# Week 1 started on 2026-04-20 (Monday) and ended on 2026-04-24 (Friday) in the workspace files.
# Let's list the weeks if we align them to Mon-Fri (since April 17 is Friday, maybe it belongs to prep/Week 1 or we start Week 1 on April 20? Wait, the prompt says 'sửa thời gian thực tập bắt đầu từ ngày 17/04 đến ngày 30/7 và chia worklog thành các tuần tương đương trong khoảng thời gian đó' - edit internship duration starting from 17/04 to 30/7 and split worklog into equivalent weeks within that period).
# If the period is 17/04 to 30/07:
# Let's see how many weeks we get. 
# Let's design two options:
# 1. 15 weeks total.
# Let's trace the weeks from 17/04 to 30/07.
# Week 1: 17/04/2026 - 24/04/2026 (or 20/04 - 24/04, since April 17 is Friday)
# Week 2: 27/04/2026 - 01/05/2026
# Let's write a script to generate the Monday-Friday dates for each week.

curr = start_date
# Find the first Monday on or after start_date, or does Week 1 include 17/04 (Friday)?
# If the internship starts on Friday April 17, then Week 1 has Friday April 17, and then the next week is Week 2? Or is Week 1 from Monday April 20 to Friday April 24, and April 17 is just the start date?
# Let's print out both calendar weeks and Mon-Fri weeks.

print("--- Option 1: Calendar 7-day weeks starting from April 17 ---")
curr = start_date
w = 1
while curr <= end_date:
    w_end = curr + datetime.timedelta(days=6)
    if w_end > end_date:
        w_end = end_date
    print(f"Week {w}: {curr.strftime('%d/%m/%Y')} - {w_end.strftime('%d/%m/%Y')}")
    curr += datetime.timedelta(days=7)
    w += 1

print("\n--- Option 2: Business weeks (Mon-Fri) matching HUTECH report style ---")
# Week 1: Mon 20/04/2026 - Fri 24/04/2026 (with Fri 17/04 as the onboarding/first day)
# Let's check how many weeks we need. If we need exactly 15 weeks:
# Week 1: 17/04/2026 - 24/04/2026 (or Monday 20/04 - Friday 24/04)
# Let's print Monday-Friday for each week from 20/04/2026:
# Monday of Week 1 is April 20, 2026.
# Let's calculate:
# Week 1: Mon 20/04 - Fri 24/04
# ...
# Week 15: Mon 27/07 - Thu 30/07 (since July 30 is Thursday)
# Let's check how many weeks that is.
w = 1
curr_mon = datetime.date(2026, 4, 20)
while curr_mon <= end_date:
    curr_fri = curr_mon + datetime.timedelta(days=4)
    if curr_fri > end_date:
        curr_fri = end_date
    # For Week 1, if it starts on 17/04, we can write: 17/04/2026 - 24/04/2026
    # Let's list the range:
    s_str = curr_mon.strftime('%d/%m/%Y')
    if w == 1:
        s_str = "17/04/2026"
    print(f"Week {w}: {s_str} - {curr_fri.strftime('%d/%m/%Y')}")
    curr_mon += datetime.timedelta(days=7)
    w += 1
