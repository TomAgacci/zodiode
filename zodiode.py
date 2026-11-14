#!/usr/bin/env python3
"""Zodiode: birthday-to-zodiac horoscope CLI.

Uses common tropical Western zodiac date ranges and a fixed set of
entertainment-oriented Zodiode readings. No network connection required.
"""

from __future__ import annotations

from datetime import date, datetime

SIGN_DATA = [
    ("Capricorn", (12, 22), (1, 19), "Practical judgment leads. Put resources toward recurring needs and lasting value; give temporary wants time to cool."),
    ("Aquarius", (1, 20), (2, 18), "Innovation can attract you. New tools and technology are strongest when they genuinely improve your routine."),
    ("Pisces", (2, 19), (3, 20), "Separate emotional appeal from lasting usefulness. Favor choices that support everyday well-being after the first attraction fades."),
    ("Aries", (3, 21), (4, 19), "Put your energy toward what solves a real need. Immediate usefulness matters more than an impulsive purchase."),
    ("Taurus", (4, 20), (5, 20), "Value, comfort, and quality lead. Choose things you will use often, and let durability beat novelty."),
    ("Gemini", (5, 21), (6, 20), "Choices compete for attention. Compare options before spending and keep curiosity from becoming unnecessary accumulation."),
    ("Cancer", (6, 21), (7, 22), "Home and everyday stability come first. Favor food, household needs, health, and comfort that strengthen your routine."),
    ("Leo", (7, 23), (8, 22), "Presentation and enjoyment may stand out. Choose what you genuinely value rather than what simply attracts attention."),
    ("Virgo", (8, 23), (9, 22), "Utility is your filter. Compare cost, maintenance, durability, and how often you will actually use something."),
    ("Libra", (9, 23), (10, 22), "Balance pleasure with practical value. Enjoyment can have a place in the budget, but make each choice earn that place."),
    ("Scorpio", (10, 23), (11, 21), "Look beneath the immediate price. Consider recurring costs, durability, and whether a purchase remains useful later."),
    ("Sagittarius", (11, 22), (12, 21), "Leave room for discovery without losing your priorities. Spend where an experience or useful tool genuinely expands your options."),
]


def parse_birthday(raw: str) -> date:
    formats = ("%Y-%m-%d", "%m/%d/%Y", "%m-%d-%Y")
    for fmt in formats:
        try:
            return datetime.strptime(raw.strip(), fmt).date()
        except ValueError:
            pass
    raise ValueError("Use YYYY-MM-DD, MM/DD/YYYY, or MM-DD-YYYY.")


def zodiac_sign(birthday: date) -> str:
    month_day = (birthday.month, birthday.day)
    if month_day >= (12, 22) or month_day <= (1, 19):
        return "Capricorn"
    for sign, start, end, _reading in SIGN_DATA[1:]:
        if start <= month_day <= end:
            return sign
    raise RuntimeError("Unable to determine zodiac sign.")


def sign_reading(sign: str) -> str:
    for name, _start, _end, reading in SIGN_DATA:
        if name == sign:
            return reading
    raise KeyError(sign)


def sign_legend() -> str:
    labels = [
        "Aries: Mar 21-Apr 19", "Taurus: Apr 20-May 20",
        "Gemini: May 21-Jun 20", "Cancer: Jun 21-Jul 22",
        "Leo: Jul 23-Aug 22", "Virgo: Aug 23-Sep 22",
        "Libra: Sep 23-Oct 22", "Scorpio: Oct 23-Nov 21",
        "Sagittarius: Nov 22-Dec 21", "Capricorn: Dec 22-Jan 19",
        "Aquarius: Jan 20-Feb 18", "Pisces: Feb 19-Mar 20",
    ]
    return "\n".join(labels)


def all_horoscopes() -> str:
    ordered = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces",
    ]
    return "\n\n".join(f"{name.upper()}\n{sign_reading(name)}" for name in ordered)


def main() -> None:
    print("ZODIODE")
    print("Birthday-to-zodiac horoscope\n")
    raw = input("Enter your birthday (YYYY-MM-DD): ")

    try:
        birthday = parse_birthday(raw)
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    sign = zodiac_sign(birthday)
    print(f"\nYour sign: {sign}")
    print(f"Your Zodiode: {sign_reading(sign)}")

    print("\n--- SIGN LEGEND ---")
    print(sign_legend())

    print("\n--- ALL ZODIODE HOROSCOPES ---")
    print(all_horoscopes())

    print("\nFor entertainment only. Zodiode is not financial advice.")


if __name__ == "__main__":
    main()
