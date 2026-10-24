# models
from dataclasses import dataclass
from enum import Enum, auto
from datetime import datetime


class TaskStatus(Enum):
    NEW = auto()
    STARTED = auto()
    FINISH = auto()
    
    
class TaskResult(Enum):
    SUCCESS = auto()
    FAIL = auto()

class InvalidTaskTransition(Exception):
    ... 


@dataclass
class TaskModel:
    id: int
    status: TaskStatus
    created_at: datetime
    started_at: datetime | None = None
    finished_at: datetime | None = None
    result: TaskResult | None = None
    error: str | None = None
    
    
    def start(self) -> None:
        if self.status != TaskStatus.NEW:
            raise InvalidTaskTransition(f"Not valid status task '{self.status.name}'")
        
        self.status = TaskStatus.STARTED
        self.started_at = datetime.now()
        
    def succeed(self) -> None:
        if self.status != TaskStatus.STARTED:
            raise InvalidTaskTransition
        
        self.status = TaskStatus.FINISH
        self.result = TaskResult.SUCCESS
        self.finished_at = datetime.now()
        
    def fail(self, error: str) -> None:
        if self.status != TaskStatus.STARTED:
            raise InvalidTaskTransition
        
        if not error:
            raise ValueError
        
        self.status = TaskStatus.FINISH
        self.result = TaskResult.FAIL
        self.error = error
        self.finished_at = datetime.now()