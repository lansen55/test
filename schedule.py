from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Event:
    title: str
    date: Optional[str] = None
    description: Optional[str] = None

class Schedule:
    """Simple in-memory schedule manager."""

    def __init__(self) -> None:
        self.events: List[Event] = []

    def add_event(self, title: str, date: Optional[str] = None, description: Optional[str] = None) -> Event:
        """Add a new event to the schedule."""
        event = Event(title=title, date=date, description=description)
        self.events.append(event)
        return event

    def list_events(self) -> List[Event]:
        """Return a list of all scheduled events."""
        return list(self.events)

    def remove_event(self, title: str) -> Event:
        """Remove the first event matching the given title."""
        for index, event in enumerate(self.events):
            if event.title == title:
                return self.events.pop(index)
        raise ValueError(f"Event '{title}' not found")
