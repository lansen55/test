import argparse
import json
import os
from typing import Optional

from schedule import Schedule, Event

DEFAULT_FILE = "schedule.json"


def load_schedule(path: str) -> Schedule:
    schedule = Schedule()
    if os.path.exists(path):
        with open(path, "r") as fh:
            data = json.load(fh)
        for item in data:
            schedule.add_event(item["title"], item.get("date"), item.get("description"))
    return schedule


def save_schedule(schedule: Schedule, path: str) -> None:
    with open(path, "w") as fh:
        json.dump([event.__dict__ for event in schedule.list_events()], fh)


def main(argv: Optional[list[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Manage scheduled events")
    parser.add_argument("--file", default=DEFAULT_FILE, help="Path to schedule file")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add an event")
    add_parser.add_argument("title")
    add_parser.add_argument("--date")
    add_parser.add_argument("--description")

    subparsers.add_parser("list", help="List events")

    remove_parser = subparsers.add_parser("remove", help="Remove an event")
    remove_parser.add_argument("title")

    args = parser.parse_args(argv)
    schedule = load_schedule(args.file)

    if args.command == "add":
        event = schedule.add_event(args.title, args.date, args.description)
        save_schedule(schedule, args.file)
        print(f"Added: {event}")
    elif args.command == "list":
        for ev in schedule.list_events():
            print(ev)
    elif args.command == "remove":
        event = schedule.remove_event(args.title)
        save_schedule(schedule, args.file)
        print(f"Removed: {event}")


if __name__ == "__main__":
    main()
