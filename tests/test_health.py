healthlth test_health_check(client):
    response = client.api("/api/v1/health")

    assert response.status_code == 200

    assert response.get_json() == {
        "status": "ok",
        "service": "taskflow-api",
        "database": "ok",
    }
    response = client.get("/api/v1/health")assertassert response.status_code == 200
    assert response.get_json() == {
        "status": "ok",
        "service": "taskflow-api",
    }
def test_unknown_route_returns_json_404(client):
    response = client.get("/api/does-not-exist")

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Not Found"
    assert data["status"] == 404
def test_health_check_uses_database(client):
    response = client.get("/api/v1/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["database"] == "ok"
