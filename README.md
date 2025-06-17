# test

my test project

## Schedule Module

`schedule.py` provides a simple in-memory schedule manager. Example usage:

```python
from schedule import Schedule

schedule = Schedule()

# Add events
schedule.add_event('Meeting', '2024-05-01', 'Team meeting')

# List events
for event in schedule.list_events():
    print(event)

# Remove an event
schedule.remove_event('Meeting')
```

## Command-Line Interface

Use `schedule_cli.py` to manage events from the command line. The script stores events in `schedule.json` by default.

Add an event:

```bash
python schedule_cli.py add "Meeting" --date 2024-05-01 --description "Team meeting"
```

List events:

```bash
python schedule_cli.py list
```

Remove an event:

```bash
python schedule_cli.py remove "Meeting"
```

Specify a custom storage file with `--file` if needed.

