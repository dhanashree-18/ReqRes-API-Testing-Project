import pytest

@pytest.fixture

def api_setup():
    base_url = "https://reqres.in"
    headers = {
        "x-api-key": "free_user_3GuIDYW6ZMBFGP4ZTg53154sU98"
    }
    yield base_url, headers