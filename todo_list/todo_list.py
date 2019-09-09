#!/usr/bin/env python3

from data_structs.tasks import TaskType, ReminderType, Reminder, TodoTask
from datetime import datetime, timedelta
from typing import Dict, List, Optional


def find_space(haystack: List[TodoTask]) -> int:
    if None in haystack:
        return haystack.index(None)
    return -1

class TodoList:
    def __init__(self) -> None:
        self.all_tasks = []
        self.dummy_task = TodoTask(
            id=0,
            name='Buy Printen',
            description='You need to buy Printen to send as a gift',
            deadline=datetime.now(),
            type=TaskType.CHORE,
            reminders=[
                Reminder(point_in_time=datetime.now(), type=ReminderType.CARRIER_PIDEON)
            ]
        )

    def lookup_task_by_id(self, id: int) -> TodoTask:
        if len(self.all_tasks) + 1 <= id and self.all_tasks[id]:
            raise ValueError('Task with id {} could not be found'.format(id))
        return self.all_tasks[id]
    
    def get_all_tasks(self) -> List[TodoTask]:
        return list(filter(lambda x: x, self.all_tasks))

    def insert_task(self, task_name: str, desc: str, task_deadline: datetime, task_type: TaskType) -> TodoTask:
        space_idx = find_space(self.all_tasks)

        if space_idx >= 0:
            new_task_id = space_idx

            new_task = TodoTask(
                id=new_task_id,
                name=task_name,
                description=desc,
                deadline=task_deadline,
                type=task_type,
                reminders=[
                    Reminder(point_in_time=task_deadline - timedelta(hours=4), type=ReminderType.CARRIER_PIDEON)
                ]   
            )
            self.all_tasks[space_idx] = new_task
            return self.all_tasks[space_idx]
        else:
            new_task_id = len(self.all_tasks)

            new_task = TodoTask(
                id=new_task_id,
                name=task_name,
                description=desc,
                deadline=task_deadline,
                type=task_type,
                reminders=[
                    Reminder(point_in_time=task_deadline - timedelta(hours=4), type=ReminderType.CARRIER_PIDEON)
                ]   
            )
            self.all_tasks.append(new_task)
            
            return self.all_tasks[-1]