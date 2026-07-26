import requests

class UsersAPI:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def get_all_users(self, page=1):
        return requests.get(self.base_url + f"/api/users?page={page}", 
                            headers=self.headers)

    def get_single_user(self, user_id):
        return requests.get(self.base_url + f"/api/users/{user_id}" ,
                            headers= self.headers)

    def create_user(self, payload):
        return requests.post(self.base_url + f"/api/users",
                            headers= self.headers, json=payload)

    def update_user(self, user_id, payload):
        return requests.put(self.base_url + f"/api/users/{user_id}", 
                            headers=self.headers, json=payload)

    def delete_user(self, user_id):
        return requests.delete(self.base_url +f"/api/users/{user_id}",
                               headers= self.headers)