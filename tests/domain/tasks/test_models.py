# test_models
from src.agent_flow.domain.tasks.models import TaskStatus, TaskModel, TaskResult, InvalidTaskTransition
from datetime import datetime
import pytest


def make_task() -> TaskModel:
    return TaskModel(id=1,  status=TaskStatus.NEW, created_at=datetime.now())


def test_task_can_be_started():
    task = make_task()
    
    task.start()
    
    assert task.status == TaskStatus.STARTED

def tests_task_can_succeed():
    task = make_task()
    task.start()
    task.succeed()
    
    assert task.status == TaskStatus.FINISH
    assert task.result == TaskResult.SUCCESS

def test_task_fail_retry():
    task = make_task()
    
    task.start()
    task.succeed()
    with pytest.raises(InvalidTaskTransition):
        task.start()
    
def test_task_fail_start():
    task = make_task()
    
    task.status = TaskStatus.STARTED
    
    with pytest.raises(InvalidTaskTransition):
        task.start()
            