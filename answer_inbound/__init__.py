import json
import logging
import pprint

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(json.dumps([
        {
            'action': 'talk',
            'text': 'Welcome to the emotion reporting hotline. Please enter 1 if you are happy, or 2 if you are sad.',
            'bargeIn': True,
        },
        {
            'action': 'input',
            'eventUrl': [ f'https://{req.headers["host"]}/api/emotion_feedback' ],
            'maxDigits': 1,
            'timeOut': 10,
        },
    ]), mimetype='application/json')