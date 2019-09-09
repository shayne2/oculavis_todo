#!/usr/bin/env python3

from datetime import datetime
from enum import Enum, auto
from typing import Dict, List, NamedTuple


class TaskType(Enum):
    HOMEWORK = auto()
    AUSRAEUMEN = auto()
    MEETING = auto()
    CHORE = auto()
    ERRAND = auto()


class ReminderType(Enum):
    EMAIL = auto()
    NOTIFICATION = auto()
    CARRIER_PIDEON = auto()


class Reminder(NamedTuple):
    point_in_time: datetime
    type: ReminderType 


class TodoTask(NamedTuple):
    id: int
    name: str
    description: str
    deadline: datetime
    type: TaskType
    reminders: List[Reminder]


def enum_to_string(en: Enum) -> str:
    return str(en).split('.')[-1]

def pit_to_str(pit: datetime) -> str:
    """
    Function to get datetime as a string in the desired format
    """
    return pit.strftime("%m/%d/%Y, %H:%M:%S")

def todo_task_to_dict(task: TodoTask) -> Dict:
    ret = {
        'id': task.id,
        'name': task.name,
        'desc': task.description,
        'deadline': pit_to_str(task.deadline),
        'type': enum_to_string(task.type),
        'reminders': [] 
    }

    for reminder in task.reminders:
        ret['reminders'].append(
            (pit_to_str(reminder.point_in_time), enum_to_string(reminder.type))
        )

    return ret