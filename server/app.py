from flask import Flask, request
from logging import getLogger

import redis

app = Flask(__name__)
logger = getLogger(__name__)

redis_client = redis.Redis(host='redis', port=6379)


def _set_value(key: str, value: str):
    redis_client.set(key, value)


def _get_value(key: str):
    return redis_client.get(key)


@app.route('/motion/<motion_id>', methods=['GET', 'POST'])
def motion(motion_id: str):
    if request.method == 'POST':
        motion_data = request.data
        _set_value(motion_id, motion_data)
        return 'ok'
    else:
        value = _get_value(motion_id)
        if not value:
            return 'error: no value', 404
        else:
            return value


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
