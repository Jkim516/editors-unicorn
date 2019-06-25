#!/usr/bin/env python
"""Tells us the day of the week."""

from datetime import datetime
import calendar
DAYS = list(calendar.day_name)

def find_day_if_week():
    """Returns the day of week as a string, e.g. 'Monday'"""
    now = datetime.now()
    weekday = now.weekday()
    return DAYS[weekday]
    

def main():
    """Sends the day of the week to stdout."""
    day = find_day_if_week()
    print(f"It's {day}!")
    print("test")

if __name__ == "__main__":
    main()