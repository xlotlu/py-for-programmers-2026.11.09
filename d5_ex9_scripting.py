#!/usr/bin/python

# ^^ "shebang": valabil doar pentru unix-uri
# și tot pentru unix-uri, facem fișierul executabil
# (chmod +x)

"""
Parses a timespec and runs a payload at the given time.
"""


# acesta este un modul hibrid, ce funcționează ca executabil Python
# dar și ca library, sursă de import

import datetime as dt
import sys
from time import sleep
import subprocess


def get_seconds_from_now(timespec):
    now = dt.datetime.now()
    target_time = dt.time.strptime(timespec, "%H:%M")
    target = dt.datetime.combine(now.date(), target_time)

    if target <= now:
        target += dt.timedelta(days=1)

    return (target - now).total_seconds()

def wait(seconds, countdown=False):
    if countdown:
        # TODO: to a countdown timer
        pass
    sleep(seconds)

def execute_payload(cmd):
    print('executing', cmd)
    # TODO:
    #subprocess.run(cmd.split())

if __name__ == '__main__':
    # fac treaba ce o face un executabil

    # the manual way:
    # try:
    #     timespec = sys.argv[1]
    # except IndexError:
    #     print("Wrong usage", file=sys.stderr)
    #     sys.exit(1)

    # the simple, automated, clean way:
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("timespec",
                        help="Time specification in HH:MM format")

    parser.add_argument("--payload",
                        required=False, default=None,
                        help="Optional payload command")

    parser.add_argument("--countdown",
                        required=False, default=False,
                        help="Write a countdown timer")


    args = parser.parse_args()

    seconds = get_seconds_from_now(args.timespec)
    wait(seconds)
    if args.payload:
        execute_payload(args.payload)
