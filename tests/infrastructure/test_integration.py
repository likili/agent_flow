# сохранение данный в бд
from sqlalchemy.orm import Session
from datetime import datetime
from src.agent_flow.domain.tasks.models import TaskStatus

def insert_task(session: Session):
    session.execute('INSERT INTO task (status, created_at)'
                    f'VALUES ({TaskStatus.NEW}, {datetime.now()})')
    [[task_id]] = session.execute('SELECT id FROM task WHERE id=:id AND status=:stats', dict(id=1, status=TaskStatus.NEW))
    return task_id

