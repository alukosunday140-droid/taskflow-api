def test_create_task(client):
    response = client.post(
        "/api/tasks",
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
        "/api/tasks",
        json={
            "description": "Missing title",
        },
    )

    assert response.status_code == 400


def test_get_tasks(client):
    client.post(
        "/api/tasks",
        json={"title": "First task"},
    )

    response = client.get("/api/tasks")

    assert response.status_code == 200

    data = response.get_json()

    assert data["count"] == 1
    assert data["tasks"][0]["title"] == "First task"


def test_get_single_task(client):
    create_response = client.post(
        "/api/tasks",
        json={"title": "Test task"},
    )

    task_id = create_response.get_json()["id"]

    response = client.get(f"/api/tasks/{task_id}")

    assert response.status_code == 200
    assert response.get_json()["title"] == "Test task"


def test_update_task(client):
    create_response = client.post(
        "/api/tasks",
        json={"title": "Old title"},
    )

    task_id = create_response.get_json()["id"]

    response = client.patch(
        f"/api/tasks/{task_id}",
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
        "/api/tasks",
        json={"title": "Delete me"},
    )

    task_id = create_response.get_json()["id"]

    response = client.delete(f"/api/tasks/{task_id}")

    assert response.status_code == 204

    get_response = client.get(f"/api/tasks/{task_id}")

    assert get_response.status_code == 404
