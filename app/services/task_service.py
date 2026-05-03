from app.models.task import Task

def create_task_service(db, task):
    new_task = Task(
        title=task.title,
        description=task.description,
        project_id=task.project_id,
        assigned_to=task.assigned_to
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_tasks_service(db, user_id):
    return db.query(Task).filter(Task.assigned_to == user_id).all()


def update_task_status_service(db, task_id, status):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.status = status
        db.commit()
        db.refresh(task)
    return task