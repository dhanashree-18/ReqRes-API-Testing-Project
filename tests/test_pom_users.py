import pytest

@pytest.mark.get
def test_users(users_api):
    response = users_api.get_all_users(page=1)
    data = response.json()
    assert response.status_code ==200
    assert  data["page"] ==1
    assert len(data["data"]) == 6
    assert response.elapsed.total_seconds() < 5

@pytest.mark.get
def test_get_single_user(users_api):
    response = users_api.get_single_user(user_id=2)
    data = response.json()
    assert response.status_code ==200
    assert response.elapsed.total_seconds() < 5
    assert data["data"]["id"] == 2

@pytest.mark.post
def test_create_user(users_api):
    payload = {
    "name": "Mini",
    "job": "QA Tester"
    }
    response = users_api.create_user(payload)
    data = response.json()
    assert response.status_code == 201
    assert "id" in data
    assert data["name"] == "Mini"
    assert data["job"] == "QA Tester"


@pytest.mark.put
def test_update_user(users_api):
    payload = {
        "name": "Mini",
        "job": "senior QA Tester"
    }
    response = users_api.update_user(2, payload)
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Mini"
    assert data["job"] == "senior QA Tester"
    assert "updatedAt" in data

@pytest.mark.delete
def test_delete_user(users_api):
    response = users_api.delete_user(2)
    assert response.status_code == 204

@pytest.mark.get
def test_get_invalid_user(users_api):
    response = users_api.get_single_user(user_id=999)
    data = response.json()
    assert response.status_code == 404