import os

from flask import Flask, request, jsonify, Blueprint
from marshmallow import ValidationError

from bulider import build_query
from models import RequestSchema

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query")
def perform_query():
    data = request.json
    try:
        RequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400
    first_result = build_query(
        cmd=data['cmd1'],
        value=data['value1'],
        file_name=data['file_name'],
        data=None
    )
    second_result = build_query(
        cmd=data['cmd1'],
        value=data['value1'],
        file_name=data['file_name'],
        data=first_result
    )
    return jsonify(second_result)
    return app.response_class('', content_type="text/plain")
