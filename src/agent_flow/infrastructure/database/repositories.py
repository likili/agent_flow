from models import task
from src.agent_flow.domain.tasks.models import TaskModel
from typing import List


class TaskRepositories:
    def add(self, task: TaskModel):
        ...
    
        
    def get(self, id_: int) -> TaskModel | None:
        ...
        
    def list(self) -> List[TaskModel] | None:
        ...
        