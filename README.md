

## How to use
With python 3.11, make a virtual environment and install dependencies
```
virtualenv .venv
.\venv\scripts\activate
pip install -r requirements
```

Deploy the fastapi app
```
uvicorn app:app --port 9900 --reload
```

Deploy the locust service
```
locust -f locustfile.py --host=http://127.0.0.1:9900
```

Open the Locust Web Interface going to `http://localhost:8089`
You’ll see the following fields:

- Number of users to simulate: This is the total number of users that will be simulating load.
- Spawn rate: The number of new users spawned per second.
- Host: The base URL for the FastAPI app (it should already be set based on your earlier command).

Example:  
If you set 100 users and a spawn rate of 10:
- Locust will add 10 new users every second until it reaches a total of 100 users.
- So, in this case, after 10 seconds, there will be 100 users actively sending requests to your FastAPI app.