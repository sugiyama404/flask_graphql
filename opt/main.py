from graphene import ObjectType, String, Schema, Int
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


class Query(ObjectType):
    hello = String(name=String(default_value="bob"))

    def resolve_hello(root, info, name):
        return f'My name is {name}'


schema = Schema(query=Query)


@app.route('/', methods=['POST'])
def hello():
    data = json.loads(request.data)
    result = schema.execute(data['query']).data
    return json.dumps(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
