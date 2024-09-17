from locust import HttpUser, task, between

class FastAPIUser(HttpUser):
    wait_time = between(0.2, 1)  # Simulate a wait time between 1 and 3 seconds between tasks

    @task
    def hit_1_second_endpoint(self):
        self.client.get("/1_second")  # Simulates a GET request to "/1_second"

