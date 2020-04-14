import json
from functools import wraps


def to_json(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return json.dumps(function(*args, **kwargs))
    return wrapper


@to_json
def get_data(parm):
    return {'data': parm}


