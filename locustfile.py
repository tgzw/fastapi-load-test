from locust import HttpUser, task, between

class FastAPIUser(HttpUser):
    wait_time = between(1, 3)  # Simulate a wait time between 1 and 3 seconds between tasks

    @task
    def hit_endpoint1(self):
        self.client.get("/endpoint1")  # Simulates a GET request to "/endpoint1"

    @task
    def hit_endpoint2(self):
        self.client.get("/endpoint2")  # Simulates a GET request to "/endpoint2"

    @task
    def hit_endpoint3(self):
        self.client.get("/endpoint3")  # Simulates a GET request to "/endpoint3"
        
    @task
    def hit_endpoint4(self):
        self.client.get("/endpoint4")  # Simulates a GET request to "/endpoint3"
