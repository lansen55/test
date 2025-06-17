import os
import sys
import pytest

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from schedule import Schedule


def test_add_and_list_event():
    s = Schedule()
    s.add_event('Meeting', '2024-05-01', 'Team meeting')
    events = s.list_events()
    assert len(events) == 1
    assert events[0].title == 'Meeting'
    assert events[0].date == '2024-05-01'
    assert events[0].description == 'Team meeting'


def test_remove_event():
    s = Schedule()
    s.add_event('Task')
    removed = s.remove_event('Task')
    assert removed.title == 'Task'
    assert s.list_events() == []


def test_remove_event_not_found():
    s = Schedule()
    with pytest.raises(ValueError):
        s.remove_event('Missing')
