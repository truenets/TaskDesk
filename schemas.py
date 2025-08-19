"""Shemas"""

from pydantic import BaseModel


class STaskAdd(BaseModel):
    """schema task add"""
    name: str
    description: str | None

class STask(STaskAdd):
    """schema task"""
    id: int

class STaskId(BaseModel):
    """schema task_id"""
    ok: bool = True
    task_id: int
