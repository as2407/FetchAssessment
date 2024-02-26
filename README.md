# Fetch Reward Receipt Processor

Problem Statement: [Link](https://github.com/fetch-rewards/receipt-processor-challenge)

## Key Decisions

These are the key decisions that I took while developing the system.

- I have used Python with Flask as the Backend Framework
- I have not used any Database as the problem statement states that the value need not be persistent
- I have used an internal in-memory dictionary (map) variable to store the Receipt IDs (key) and Points Earned (values)
- The Flask server runs on Port 5000 inside the Docker network by default. However, locally, I have mapped it to Port 8000. So, for testing, all the HTTP requests should be made on `localhost:8000`
- My codebase is divided into separate Python Repositories. The `models` repository contains the logic to validate the `Receipt` object and `Item` object, and the `service` repository contains the logic to calculate the reward points. The `app.py` file acts like a Controller and handles all the HTTP requests
- I have provided the necessary docker commands to run the system
 
## How to Run

You will need to have Docker installed and running. Navigate to the directory in the terminal and run the following commands.

```docker build --tag fetch-docker .```
<br>
```docker run -p 8000:5000 fetch-docker```


