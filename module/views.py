from flask import jsonify
from module import app

@app.route('/healthcheck')
def healthcheck():
    response = {
        'status': 'OK',
        'message': 'Application is healthy'
    }
    return jsonify(response), 200
