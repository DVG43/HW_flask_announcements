
from views import AnnounView
from errors import HttpError
from flask import Flask, jsonify

app = Flask('app')


@app.errorhandler(HttpError)
def http_error_handler(error: HttpError):
    response = jsonify({
           'status': 'error',
           'reason': error.message
    })
    response.status_code = error.status_code
    return response


announ_view = AnnounView.as_view('announsments')
app.add_url_rule('/announsments/', view_func=announ_view, methods=['POST'])
app.add_url_rule('/announsments/<int:announsment_id>', view_func=announ_view, methods=['GET', 'DELETE'])

app.run()
