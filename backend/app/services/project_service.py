from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.project import Project
from app.schemas.project import ProjectCreate


def create_project_service(
    project: ProjectCreate,
    db: Session
):

    new_project = Project(
        name=project.name,
        description=project.description,
        created_by=project.created_by
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


def get_projects_service(
    db: Session
):

    projects = db.query(Project).all()

    return projects


def get_single_project_service(
    project_id: int,
    db: Session
):

    project = db.query(Project).filter(
        Project.id == project_id
    ).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project


def update_project_service(
    project_id: int,
    project_data: ProjectCreate,
    db: Session
):

    project = db.query(Project).filter(
        Project.id == project_id
    ).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    project.name = project_data.name
    project.description = project_data.description
    project.created_by = project_data.created_by

    db.commit()
    db.refresh(project)

    return project


def delete_project_service(
    project_id: int,
    db: Session
):

    project = db.query(Project).filter(
        Project.id == project_id
    ).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    db.delete(project)
    db.commit()

    return {
        "message": "Project deleted successfully"
    }