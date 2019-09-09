# Trial day TODO API (Backend)

Simple sanic api to interact with a ToDo list

## Setup

$ pip install -r requirements.txt

## Local Dev

$ python main.py

$ curl 'http://localhost:8000/task?id=1234'

$ curl 'http://localhost:8000/tasks'

$ curl -d '{"name": "Buy Printen", "description": "You need to buy Printen", "deadline": "09/09/2019", "type": "chore"}' 'http://localhost:8000/add_task'