"""
Day 9 - 2026-10-15
Tool: Date Difference Calculator
What it does: Works out how many days, weeks and months are between two
dates, which day of the week a date falls on, and what date it will be
after adding a number of days.
Who it helps: Anyone counting down to an exam, a visa or passport expiry,
a project deadline, a birthday, or a delivery date.
"""

from datetime import date, timedelta


def _parse(day_text):
    """Turn a 'YYYY-MM-DD' string into a date object."""
    parts = day_text.strip().split("-")
    if len(parts) != 3:
        raise ValueError("Use the format YYYY-MM-DD, for example 2026-10-15.")
    year, month, day = (int(p) for p in parts)
    return date(year, month, day)


def days_between(start_text, end_text):
    """Return the number of days from start to end (always positive)."""
    start, end = _parse(start_text), _parse(end_text)
    return abs((end - start).days)


def describe_difference(start_text, end_text):
    """Return the gap as days, whole weeks + days, and rough months."""
    total = days_between(start_text, end_text)
    weeks, extra_days = divmod(total, 7)
    months = round(total / 30.44, 1)  # average month length
    return {
        "days": total,
        "weeks_and_days": f"{weeks} weeks, {extra_days} days",
        "about_months": months,
    }


def add_days(day_text, number_of_days):
    """Return the date (YYYY-MM-DD) that is N days after the given date."""
    return (_parse(day_text) + timedelta(days=number_of_days)).isoformat()


def weekday_of(day_text):
    """Return the day of the week, for example 'Thursday'."""
    return _parse(day_text).strftime("%A")


if __name__ == "__main__":
    # Example 1: counting down from today to an exam date
    print("2026-10-15 to 2026-12-01:", describe_difference("2026-10-15", "2026-12-01"))

    # Example 2: what date is 90 days from now (like a visa validity check)?
    print("90 days after 2026-10-15:", add_days("2026-10-15", 90))

    # Example 3: which day of the week is a birthday this year?
    print("2026-10-15 is a", weekday_of("2026-10-15"))
