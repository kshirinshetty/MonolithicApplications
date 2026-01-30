from locust import HttpUser, task, between

class EventsUser(HttpUser):
    wait_time = between(0.5, 1)

    @task
    def view_events(self):
        with self.client.get(
            "/events",
            params={"user": "PES2UG23CS289"},
            name="GET /events",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Unexpected status {response.status_code}")
