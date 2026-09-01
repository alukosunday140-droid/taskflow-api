from flask import jsonify

from app.api import api_bp
from app.extensions import db


@api_bp.get("/health")
def health_check():
    try:
        db.session.execute(db.text("SELECT 1"))

        return jsonify(
            {
                "status": "ok",
                "service": "taskflow-api",
                "database": "ok",
            }
        ), 200

    except Exception:
        return jsonify(
            {
                "status": "error",
                "service": "taskflow-api",
                "database": "unavailable",
            }
        ), 503
