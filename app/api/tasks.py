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

    task = Task(
        title=title.strip(),
        description=data.get("description"),
        completed=bool(data.get("completed", False)),
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
