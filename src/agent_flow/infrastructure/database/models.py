
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.schema import Table, MetaData, Column
from sqlalchemy.types import Integer, String, DateTime
from src.agent_flow.domain.tasks.models import TaskModel

metadata = MetaData()

task = Table(
    'task', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('status', String(10), nullable=False),
    Column('created_at', DateTime),
    Column('started_at', DateTime, nullable=True),
    Column('finished_at', DateTime, nullable=True),
    Column('result', String(10), nullable=False),
    Column('error', String(255)),
)

def start_mapper():
    task_mapper = mapper(TaskModel, task)
