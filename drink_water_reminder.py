# Write a simple drink water reminder in Python that reminds the user to drink water at regular intervals.
# The reminder should be customizable, allowing the user to set the interval time in minutes.
# The program should run in the console and display a message reminding the user to drink water at the specified intervals.
# The reminder should run every 15 minutes and ignore notifications during sleeping time (11 PM to 6 AM).

import datetime
import time


SLEEP_START_HOUR = 23
SLEEP_END_HOUR = 6
DEFAULT_INTERVAL_MINUTES = 15


def is_sleeping_time(now: datetime.datetime) -> bool:
    return now.hour >= SLEEP_START_HOUR or now.hour < SLEEP_END_HOUR


def format_time(now: datetime.datetime) -> str:
    return now.strftime("%Y-%m-%d %H:%M:%S")


def remind():
    now = datetime.datetime.now()
    if is_sleeping_time(now):
        print(f"[{format_time(now)}] Sleeping time active. Reminder skipped.")
    else:
        print(f"[{format_time(now)}] Drink water reminder: Please drink a glass of water.")


def main(interval_minutes: int = DEFAULT_INTERVAL_MINUTES):
    print("Drink Water Reminder")
    print(f"Reminders every {interval_minutes} minutes, except between {SLEEP_START_HOUR}:00 and {SLEEP_END_HOUR}:00.")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            remind()
            time.sleep(interval_minutes * 60)
    except KeyboardInterrupt:
        print("\nReminder stopped. Stay hydrated!")


if __name__ == "__main__":
    main()