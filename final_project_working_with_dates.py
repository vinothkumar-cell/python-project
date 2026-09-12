"""
Final Project - Working with Dates
"""

import datetime


def days_in_month(year, month):
    """
    Inputs:
        year - an integer between datetime.MINYEAR and datetime.MAXYEAR
                representing the year
        month - an integer between 1 and 12 representing the month

    Returns:
        The number of days in the input month.
    """
    if month == 12:
        date1 = datetime.date(year, month, 1)
        date2 = datetime.date(year + 1, 1, 1)
    else:
        date1 = datetime.date(year, month, 1)
        date2 = datetime.date(year, month + 1, 1)

    return (date2 - date1).days


def is_valid_date(year, month, day):
    """
    Inputs:
        year - an integer representing the year
        month - an integer representing the month
        day - an integer representing the day

    Returns:
        True if year-month-day is a valid date.
        False otherwise.
    """
    if year < datetime.MINYEAR or year > datetime.MAXYEAR:
        return False

    if month < 1 or month > 12:
        return False

    if day < 1 or day > days_in_month(year, month):
        return False

    return True


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
        year1, month1, day1 - the first date
        year2, month2, day2 - the second date

    Returns:
        The number of days from the first date to the second date.
        Returns 0 if either date is invalid or the second date
        is before the first date.
    """
    if not is_valid_date(year1, month1, day1):
        return 0

    if not is_valid_date(year2, month2, day2):
        return 0

    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)

    if date2 < date1:
        return 0

    return (date2 - date1).days


def age_in_days(year, month, day):
    """
    Inputs:
        year - an integer representing the birthday year
        month - an integer representing the birthday month
        day - an integer representing the birthday day

    Returns:
        The age of a person with the input birthday as of today.
        Returns 0 if the input date is invalid or if the input
        date is in the future.
    """
    if not is_valid_date(year, month, day):
        return 0

    birthday = datetime.date(year, month, day)
    today = datetime.date.today()

    if birthday > today:
        return 0

    return days_between(year, month, day,
                        today.year, today.month, today.day)
    