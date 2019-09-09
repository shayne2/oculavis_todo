#!/usr/bin/env python3

import json as json_lib

from sanic import Sanic, request, response
from sanic.exceptions import abort
from sanic.response import json
from sanic_cors import CORS, cross_origin
from typing import Dict


app = Sanic()
CORS(app)

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
    # Dummy data for initial commit
    return {
        'name': 'this is the name',
        'time': '09/09/2019, 11:59:59',
        'type': 'Meeting',
        'reminders': [
            ('09/09/2019, 11:59:59', 'Email'),
            ('09/09/2019, 11:59:59', 'Notification')
        ] 
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)