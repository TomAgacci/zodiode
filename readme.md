# Zodiode

Licensed under CCA 4.0

Zodiode is a small, offline Python command-line program. Enter your birthday and it:

1. Determines your tropical Western zodiac Sun sign from the commonly used calendar date ranges.
2. Prints your Zodiode horoscope.
3. Prints the complete zodiac sign/date legend.
4. Prints the Zodiode horoscope for all 12 signs.

The readings are entertainment-oriented and use the practical, everyday consumer-choice style developed for Zodiode. They are not financial advice and the script does not claim that zodiac signs predict personal spending.

## Requirements

- Python 3.10 or newer
- No third-party packages
- No internet connection required

Check your Python version:

```bash
python3 --version
```

## Run

Put `zodiode.py` and `README.md` in the same folder, then run:

```bash
python3 zodiode.py
```

At the prompt, enter a birthday:

```text
Enter your birthday (YYYY-MM-DD): 1990-01-05
```

Example output begins:

```text
Your sign: Capricorn
Your Zodiode: Practical judgment leads. Put resources toward recurring needs and lasting value; give temporary wants time to cool.
```

## Accepted birthday formats

Zodiode accepts:

```text
1990-01-05
01/05/1990
01-05-1990
```

## Sign legend

- Aries: March 21-April 19
- Taurus: April 20-May 20
- Gemini: May 21-June 20
- Cancer: June 21-July 22
- Leo: July 23-August 22
- Virgo: August 23-September 22
- Libra: September 23-October 22
- Scorpio: October 23-November 21
- Sagittarius: November 22-December 21
- Capricorn: December 22-January 19
- Aquarius: January 20-February 18
- Pisces: February 19-March 20

These are the common tropical Western zodiac date ranges. Around sign-transition dates, astronomical Sun-sign boundaries can vary by year, time, and location. This lightweight version intentionally uses calendar ranges so only a birthday is required.

## Files

- `zodiode.py` - executable Zodiode program
- `README.md` - setup and usage documentation
