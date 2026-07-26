import pytest
from api.users_api import UsersAPI

@pytest.fixture
def api_setup():
    base_url = "https://reqres.in"
    headers = {
        "x-api-key": "free_user_3GuIDYW6ZMBFGP4ZTg53154sU98"
    }
    yield base_url, headers

@pytest.fixture
def users_api(api_setup):
    base_url, headers = api_setup
    return UsersAPI(base_url, headers)