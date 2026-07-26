import requests
import pytest

@pytest.mark.get
def test_users(api_setup):
    base_url, headers = api_setup
    response = requests.get(base_url + "/api/users?page=1", 
                            headers=headers)
    data = response.json()
    assert response.status_code ==200
    assert  data["page"] ==1
    assert len(data["data"]) == 6
    assert response.elapsed.total_seconds() < 2
    
@pytest.mark.get
def test_get_single_user(api_setup):
    base_url, headers = api_setup
    response = requests.get(base_url + "/api/users/2" , 
                            headers=headers)
    data = response.json()
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2
    assert data["data"]["id"] == 2

@pytest.mark.post
def test_create_user(api_setup):
    base_url, headers = api_setup
    payload = {
        "name": "Mini",
        "job": "QA Tester"
        }   
    response = requests.post(base_url + "/api/users", 
                        headers= headers , json = payload)
    data = response.json()
    assert response.status_code == 201
    assert "id" in data
    assert data["name"] == "Mini"
    assert data["job"] == "QA Tester"

@pytest.mark.put
def test_update_user(api_setup):
    base_url, headers = api_setup
    payload = {
        "name": "Mini",
        "job": "senior QA Tester"
        }
    response = requests.put(base_url + "/api/users/2", 
                            headers= headers, json = payload)
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Mini"
    assert data["job"] == "senior QA Tester"
    assert "updatedAt" in data

@pytest.mark.delete
def test_delete_user(api_setup):
    base_url, headers = api_setup
    response = requests.delete(base_url+ "/api/users/2",
                               headers= headers)
    assert response.status_code == 204

@pytest.mark.get
def test_get_invalid_user(api_setup):
    base_url, headers = api_setup
    response = requests.get(base_url+ "/api/users/999",
                            headers= headers)
    data = response.json()
    assert response.status_code == 404