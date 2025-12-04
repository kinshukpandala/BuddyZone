import datetime
from zoneinfo import ZoneInfo
from timezone_data import COUNTRY_TIMEZONES
from utils import choose_time_format, list_countries


def get_current_time():
    list_countries()
    country = input("\nEnter country (or 'exit'): ").lower()

    if country == "exit":
        return

    if country not in COUNTRY_TIMEZONES:
        print("❌ Country not found.")
        return

    tz = ZoneInfo(COUNTRY_TIMEZONES[country])
    now = datetime.datetime.now(tz)

    fmt = choose_time_format()
    print("⏰ Current Time:", now.strftime(fmt))


def convert_time():
    list_countries()
    from_c = input("\nConvert FROM (country): ").lower()
    if from_c == "exit":
        return

    to_c = input("Convert TO (country): ").lower()
    if to_c == "exit":
        return

    if from_c not in COUNTRY_TIMEZONES or to_c not in COUNTRY_TIMEZONES:
        print("❌ Invalid country.")
        return

    time_str = input("Enter time (DD-MM-YYYY HH:MM:SS): ")

    try:
        dt = datetime.datetime.strptime(time_str, "%d-%m-%Y %H:%M:%S")
    except ValueError:
        print("❌ Invalid time format.")
        return

    dt = dt.replace(tzinfo=ZoneInfo(COUNTRY_TIMEZONES[from_c]))
    converted = dt.astimezone(ZoneInfo(COUNTRY_TIMEZONES[to_c]))

    fmt = choose_time_format()
    print("\n⏳ Converted Time:", converted.strftime(fmt))
# --- IGNORE ---    