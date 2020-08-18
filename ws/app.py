from flask import (
    Flask,
    jsonify,
    request
)
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return "ok"


@app.route('/search', methods=['POST', 'GET'])
def search():
    print("/search")
    print(request.get_json())
    print(f"USERNAME: {request.authorization.username}")
    print(F"PASSWORD: {request.authorization.password}")
    print("Custom Header: {}".format(request.environ["HTTP_X_CARLOS_HEADER"]))
    if request.get_json()['target'] == 'equips':
        return jsonify(['a', 'b', 'c', 'd', 'e'])
    if request.get_json()['target'] == 'test':
        return jsonify([1, 2, 3, 4, 5])


@app.route('/query', methods=['POST', 'GET'])
def query():
    print("/query")
    print(request.get_json())
    print(f"USERNAME: {request.authorization.username}")
    print(F"PASSWORD: {request.authorization.password}")
    print("Custom Header: {}".format(request.environ["HTTP_X_CARLOS_HEADER"]))

    if request.get_json()['targets'][0]['target'] == 'a':
        return jsonify(
            [
                {
                    "columns": [
                        {
                            "text": "Time",
                            "type": "time"
                        },
                        {
                            "text": "Country",
                            "type": "string"
                        },
                        {
                            "text": "Number",
                            "type": "number"
                        }
                    ],
                    "rows": [
                        [
                            1234567,
                            "SE",
                            123
                        ],
                        [
                            1234567,
                            "DE",
                            231
                        ],
                        [
                            1234567,
                            "US",
                            321
                        ]
                    ],
                    "type": "table"
                }
            ]
        )
    elif request.get_json()['targets'][0]['target'] == 'b':
        return jsonify(
            [
                {
                    "columns": [
                        {
                            "text": "XXX",
                            "type": "time"
                        },
                        {
                            "text": "AAA",
                            "type": "string"
                        },
                        {
                            "text": "PPP",
                            "type": "number"
                        }
                    ],
                    "rows": [
                        [
                            1234567,
                            "SE",
                            123
                        ],
                        [
                            1234567,
                            "DE",
                            231
                        ],
                        [
                            1234567,
                            "US",
                            321
                        ]
                    ],
                    "type": "table"
                }
            ]
        )

app.run(host="0.0.0.0", port=8000)
