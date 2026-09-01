from flask import jsonify

from app.api import api_bp


@api_bp.get("/health")
def health_check():
    return jsonify(
        {
            "status": "ok",
            "service": "taskflow-api",
        }
    ), 200
