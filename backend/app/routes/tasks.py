from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.schemas.task import TaskCreate
from app.models.task import Task
from app.models.project import Project
from app.models.user import User
from app.core.database import SessionLocal
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE TASK
@router.post("/")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = db.query(Project).filter(
        Project.id == task.project_id,
        Project.created_by == current_user.id
    ).first()

    if not project:
        raise HTTPException(
            status_code=403,
            detail="Not authorized"
        )

    new_task = Task(
        title=task.title,
        description=task.description,
        status=task.status,
        project_id=task.project_id,
        assigned_to=task.assigned_to or current_user.id,
        due_date=task.due_date
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


# LIST TASKS WITH FILTERS
@router.get("/")
def list_tasks(
    project_id: int = Query(None),
    status: str = Query(None),
    assigned_to: int = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    query = db.query(Task)

    # ONLY OWN TASKS
    query = query.filter(
        Task.assigned_to == current_user.id
    )

    if project_id:
        query = query.filter(Task.project_id == project_id)

    if status:
        query = query.filter(Task.status == status)

    if assigned_to:
        query = query.filter(Task.assigned_to == assigned_to)

    return query.all()


# UPDATE TASK STATUS
@router.put("/{task_id}/status")
def update_task_status(
    task_id: int,
    status: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.assigned_to == current_user.id
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


# ASSIGN TASK
@router.put("/{task_id}/assign/{user_id}")
def assign_task(
    task_id: int,
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    task.assigned_to = user_id

    db.commit()
    db.refresh(task)

    return task
