#!/usr/bin/env python3

from data_structs.tasks import TaskType, ReminderType, Reminder, TodoTask, enum_to_string, todo_task_to_dict
from datetime import datetime

def test_enum_to_string():
    for en, expected in [
        (TaskType.HOMEWORK, 'HOMEWORK'),
        (TaskType.ERRAND, 'ERRAND'),
        (TaskType.CHORE, 'CHORE'),
        (ReminderType.CARRIER_PIDEON, 'CARRIER_PIDEON')
    ]:
        assert enum_to_string(en) == expected


def test_enum_to_string():
    expected_task_id = 0
    expected_task_name = 'Buy Printen'
    expected_task_description = 'You need to buy Printen to send as a gift'
    expected_task_deadline = datetime.now()
    expected_task_type = TaskType.CHORE
    expected_task_type_str = 'CHORE'
    expected_task_reminders = [
        Reminder(point_in_time=expected_task_deadline, type=ReminderType.CARRIER_PIDEON)
    ]
    expected_task_reminders_dict = [
        (expected_task_deadline.strftime("%m/%d/%Y, %H:%M:%S"), 'CARRIER_PIDEON')
    ]
    dummy_task = TodoTask(
        id=expected_task_id,
        name=expected_task_name,
        description=expected_task_description,
        deadline=expected_task_deadline,
        type=expected_task_type,
        reminders=expected_task_reminders
    )
    expected = {
        'id': expected_task_id,
        'name': expected_task_name,
        'desc': expected_task_description,
        'deadline': expected_task_deadline.strftime("%m/%d/%Y, %H:%M:%S"),
        'type': expected_task_type_str,
        'reminders': expected_task_reminders_dict
    }
    assert todo_task_to_dict(dummy_task) == expected


