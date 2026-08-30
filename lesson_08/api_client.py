import requests


class YouGileAPI:
    BASE_URL = "https://ru.yougile.com"

    def __init__(self, token):
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def create_project(self, title):
        return requests.post(
            f"{self.BASE_URL}/api-v2/projects",
            headers=self.headers,
            json={"title": title},
        )

    def get_project(self, project_id):
        return requests.get(
            f"{self.BASE_URL}/api-v2/projects/{project_id}",
            headers=self.headers,
        )

    def update_project(self, project_id, title):
        return requests.put(
            f"{self.BASE_URL}/api-v2/projects/{project_id}",
            headers=self.headers,
            json={"title": title},
        )
