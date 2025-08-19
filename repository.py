"""repo"""
from sqlalchemy import select
from database import new_session, TasksTable
from schemas import STaskAdd, STask


class TaskRepository:
    """TaskRepository"""
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        """add_one"""
        async with new_session()  as session:
            data_dict = data.model_dump()
            task = TasksTable(**data_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        """find_all"""
        async with new_session()  as session:
            query = select(TasksTable)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return task_schemas
