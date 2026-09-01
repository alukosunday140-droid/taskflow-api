from flask import jsonify, request

from app.api import api_bp
from app.extensions import db
from app.models.task import Task


@api_bp.post("/tasks")
def create_task():
    data = request.get_json(silent=True) or {}

    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return jsonify(
            {
                "error": "Bad Request",
                "message": "Title is required.",
                "status": 400,
            }
        ), 400

    description = data.get("description")

if description is not None and not isinstance(description, str):
    return jsonify(
        {
            "error": "Bad Request",
            "message": "Description must be a string.",
            "status": 400,
        }
    ), 400

completed = data.get("completed", False)

if not isinstance(completed, bool):
    return jsonify(
        {
            "error": "Bad Request",
            "message": "Completed must be a boolean.",
            "status": 400,
        }
    ), 400

task = Task(
    title=title.strip(),
    description=description.strip() if description else None,
    completed=completed,
)

    db.session.add(task)
    db.session.commit()

    return jsonify(task.to_dict()), 201


@api_bp.get("/tasks")
def get_tasks():
    tasks = Task.query.order_by(Task.created_at.desc()).all()

    return jsonify(
        {
            "tasks": [task.to_dict() for task in tasks],
            "count": len(tasks),
        }
    ), 200
@api_bp.get("/tasks/<int:task_id>")
def get_task(task_id):
    task = db.get_or_404(Task, task_id)

    return jsonify(task.to_dict()), 200


@api_bp.patch("/tasks/<int:task_id>")
def update_task(task_id):
    task = db.get_or_404(Task, task_id)
    data = request.get_json(silent=True) or {}

    if "title" in data:
        title = data["title"]

        if not isinstance(title, str) or not title.strip():
            return jsonify(
                {
                    "error": "Bad Request",
                    "message": "Title cannot be empty.",
                    "status": 400,
                }
            ), 400

        task.title = title.strip()

    if "description" in data:
    description = data["description"]

    if description is not None and not isinstance(description, str):
        return jsonify(
            {
                "error": "Bad Request",
                "message": "Description must be a string.",
                "status": 400,
            }
        ), 400

    task.description = description.strip() if description else None

    if "completed" in data:
        if not isinstance(data["completed"], bool):
            return jsonify(
                {
                    "error": "Bad Request",
                    "message": "Completed must be a boolean.",
                    "status": 400,
                }
            ), 400

        task.completed = data["completed"]

    db.session.commit()

    return jsonify(task.to_dict()), 200


@api_bp.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    task = db.get_or_404(Task, task_id)

    db.session.delete(task)
    db.session.commit()

    return "", 204
