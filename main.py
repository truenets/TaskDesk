""" General modul"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables, delete_tables
from router import router as task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load the ML model"""
    await delete_tables()
    print("Clean up resourses")
    await create_tables()
    print("Ready resourses")
    yield
    print("Exit")


app  = FastAPI(lifespan=lifespan)

app.include_router(task_router)
