import json
import logging

import azure.functions as func

RESPONSES = {
    "1": "It's great that you're so happy!",
    "2": "I'm sorry that you're unhappy.",
}
UNEXPECTED_RESPONSE = "I'm sorry, I don't understand that feedback."

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        return func.HttpResponse(json.dumps([
            {
                'action': 'talk',
                'text': RESPONSES.get(req_body['dtmf'], UNEXPECTED_RESPONSE),
            },
        ]), mimetype='application/json')
    except ValueError:
        return func.HttpResponse(
            "Could not parse request body.",
            status_code=400
        )
