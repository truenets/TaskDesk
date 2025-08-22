"""router"""
from typing import Annotated
from fastapi import APIRouter, Depends

from schemas import STask, STaskAdd, STaskId
from repository import TaskRepository


router = APIRouter(
    prefix="/tasks",
    tags=["TASKS"],
)

@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    """add_task"""
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get("")
async def get_tasks() -> list[STask]:
    """ get_tasks """
    tasks = await TaskRepository.find_all()
    return tasks
