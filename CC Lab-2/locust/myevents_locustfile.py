from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    wait_time = between(0.5, 1)

    @task
    def view_my_events(self):
        with self.client.get(
            "/my-events",
            params={"user": "PES2UG23CS289"},
            name="GET /my-events",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Unexpected status {response.status_code}")
