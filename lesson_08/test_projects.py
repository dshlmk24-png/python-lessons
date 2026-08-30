import os

from api_client import YouGileAPI


TOKEN = os.getenv("YOUGILE_TOKEN")

if not TOKEN:
    raise RuntimeError("Не задан YOUGILE_TOKEN")


api = YouGileAPI(TOKEN)


def test_create_project_positive():
    response = api.create_project("Test project")

    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative():
    response = api.create_project("")

    assert response.status_code >= 400


def test_get_project_positive():
    create_response = api.create_project("Project for GET")
    project_id = create_response.json()["id"]

    response = api.get_project(project_id)

    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_get_project_negative():
    response = api.get_project("invalid-project-id")

    assert response.status_code >= 400


def test_update_project_positive():
    create_response = api.create_project("Project for PUT")
    project_id = create_response.json()["id"]

    response = api.update_project(
        project_id,
        "Updated project",
    )

    assert response.status_code == 200


def test_update_project_negative():
    response = api.update_project(
        "invalid-project-id",
        "Updated project",
    )

    assert response.status_code >= 400
