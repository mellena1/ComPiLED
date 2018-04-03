from flask import Flask, request
from .led import CURRENT_CONFIG
import json

app = Flask(__name__)
new_config = False


@app.route('/set-config', methods=['POST'])
def set_config():
    req_data = request.get_json()
    with open(CURRENT_CONFIG, 'w') as f:
        f.write(json.dumps(req_data))
    global new_config
    new_config = True
    return 'Saved new config'


def serve(debug, port, use_reloader, host):
    app.run(debug=debug, port=port, use_reloader=use_reloader, host=host)
