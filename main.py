#!/usr/bin/env python3

import json as json_lib


from data_structs.tasks import todo_task_to_dict
from sanic import Sanic, request, response
from sanic.exceptions import abort
from sanic.response import json
from sanic_cors import CORS, cross_origin
from todo_list.todo_list import TodoList
from typing import Dict


app = Sanic()
CORS(app)

todo_list = TodoList()

@app.route('/task', methods=['GET', 'OPTIONS'])
async def get_endpoint(request: request) -> response:
    try:
        task_id = int(request.args['id'][0])
        ret = await lookup_task(task_id)
    except Exception as e:
        abort(400)
        text(str(e))

    return response.json(ret, status=200)

async def lookup_task(task_id: int) -> Dict:
    task = todo_list.lookup_task_by_id(task_id)
    return todo_task_to_dict(task)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)