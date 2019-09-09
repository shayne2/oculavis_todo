#!/usr/bin/env python3

from data_structs.tasks import TaskType, ReminderType, Reminder, TodoTask
from datetime import datetime
from typing import Dict, Optional


class TodoList:
    def __init__(self) -> None:
        self.all_tasks = []

    def lookup_task_by_id(self, id: int) -> TodoTask:

        return TodoTask(
            id=0,
            name='Buy Printen',
            description='You need to buy Printen to send as a gift',
            deadline=datetime.now(),
            type=TaskType.CHORE,
            reminders=[
                Reminder(point_in_time=datetime.now(), type=ReminderType.CARRIER_PIDEON)
            ]
        )