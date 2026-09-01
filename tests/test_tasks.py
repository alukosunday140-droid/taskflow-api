def test_create_task(client):
    response = client.post(
        "/api/v1/tasks",
        json={
            "title": "Learn Flask",
            "description": "Build a production API",
        },
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["title"] == "Learn Flask"
    assert data["description"] == "Build a production API"
    assert data["completed"] is False


def test_create_task_requires_title(client):
    response = client.post(
        "/api/v1/tasks",
        json={
            "description": "Missing title",
        },
    )

    assert response.status_code == 400


def test_get_tasks(client):
    client.post(
        "/api/v1/tasks",
        json={"title": "First task"},
    )

    response = client.get("/api/v1/tasks")

    assert response.status_code == 200

    data = response.get_json()

    assert data["pagination"]["total"] == 1
    assert data["pagination"]["page"] == 1
    assert data["pagination"]["per_page"] == 10
    assert data["tasks"][0]["title"] == "First task"


def test_get_single_task(client):
    create_response = client.post(
        "/api/v1/tasks",
        json={"title": "Test task"},
    )

    task_id = create_response.get_json()["id"]

    response = client.get(f"/api/v1/tasks/{task_id}")

    assert response.status_code == 200
    assert response.get_json()["title"] == "Test task"


def test_update_task(client):
    create_response = client.post(
        "/api/v1/tasks",
        json={"title": "Old title"},
    )

    task_id = create_response.get_json()["id"]

    response = client.patch(
        f"/api/v1/tasks/{task_id}",
        json={
            "title": "New title",
            "completed": True,
        },
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["title"] == "New title"
    assert data["completed"] is True


def test_delete_task(client):
    create_response = client.post(
        "/api/v1/tasks",
        json={"title": "Delete me"},
    )

    task_id = create_response.get_json()["id"]

    response = client.delete(f"/api/v1/tasks/{task_id}")

    assert response.status_code == 204

    get_response = client.get(f"/api/v1/tasks/{task_id}")

    assert get_response.status_code == 404


def test_create_task_rejects_invalid_completed_value(client):
    response = client.post(
        "/api/v1/tasks",
        json={
            "title": "Invalid task",
            "completed": "yes",
        },
    )

    assert response.status_code == 400


def test_create_task_rejects_invalid_description(client):
    response = client.post(
        "/api/v1/tasks",
        json={
            "title": "Invalid task",
            "description": 123,
        },
    )

    assert response.status_code == 400


def test_update_task_rejects_invalid_completed_value(client):
    create_response = client.post(
        "/api/v1/tasks",
        json={"title": "Test task"},
    )

    task_id = create_response.get_json()["id"]

    response = client.patch(
        f"/api/v1/tasks/{task_id}",
        json={"completed": "yes"},
    )

    assert response.status_code == 400


def test_get_missing_task_returns_404(client):
    response = client.get("/api/v1/tasks/9999")

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Not Found"
    assert data["status"] == 404


def test_task_list_pagination(client):
    for number in range(12):
        client.post(
            "/api/v1/tasks",
            json={"title": f"Task {number}"},
        )

    response = client.get("/api/v1/tasks?page=2&per_page=5")

    assert response.status_code == 200

    data = response.get_json()

    assert data["pagination"]["page"] == 2
    assert data["pagination"]["per_page"] == 5
    assert data["pagination"]["total"] == 12
    assert len(data["tasks"]) == 5
    assert data["pagination"]["has_next"] is True
    assert data["pagination"]["has_previous"] is True
def test_task_list_pagination_handles_invalid_values(client):
    response = client.get(
        "/api/v1/tasks?page=0&per_page=500"
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["pagination"]["page"] == 1
    assert data["pagination"]["per_page"] == 100
