from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.task import Task
from app.schemas.task import TaskCreate


def create_task_service(
    task: TaskCreate,
    db: Session
):

    new_task = Task(
        title=task.title,
        description=task.description,
        status=task.status,
        project_id=task.project_id,
        assigned_to=task.assigned_to,
        due_date=task.due_date
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def get_tasks_service(
    db: Session,
    status=None,
    project_id=None,
    assigned_to=None
):

    query = db.query(Task)

    if status:
        query = query.filter(
            Task.status == status
        )

    if project_id:
        query = query.filter(
            Task.project_id == project_id
        )

    if assigned_to:
        query = query.filter(
            Task.assigned_to == assigned_to
        )

    tasks = query.all()

    return tasks


def get_single_task_service(
    task_id: int,
    db: Session
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


def update_task_status_service(
    task_id: int,
    status: str,
    db: Session
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    task.status = status

    db.commit()
    db.refresh(task)

    return task


def delete_task_service(
    task_id: int,
    db: Session
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    return {
        "message": "Task deleted successfully"
    }