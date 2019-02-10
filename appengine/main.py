# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]


from flask import Flask, render_template, request
from flask_basicauth import BasicAuth
from datetime import datetime
import urllib.request
import os
from google.cloud import firestore

from utils import standard_logger


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__, static_url_path="/static")

app.config['BASIC_AUTH_USERNAME'] = os.getenv("BASIC_AUTH_USERNAME")
app.config['BASIC_AUTH_PASSWORD'] = os.getenv("BASIC_AUTH_PASSWORD")
app.config['BASIC_AUTH_FORCE'] = True
# or decorate a route with @basic_auth.required

basic_auth = BasicAuth(app)
logger = standard_logger(__name__, debug=True)
db = firestore.Client()


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('index.html', api_key=os.getenv("NEWSAPI_KEY"))


@app.route('/api/newsapi/v2/everything')
def newsapi_v2_everything():
    api_url = "https://newsapi.org/v2/everything?" + str(request.query_string, "utf-8")
    logger.debug("Retrieving from %s" % api_url)
    response = urllib.request.urlopen(api_url)
    logger.debug("HTTP %d %s, %s" % (response.status, response.msg, response.getheader('Content-Type')))
    #header = "".join(["%s: %s\n" % (h, v) for (h, v) in response.getheaders()])
    response = app.response_class(
        response=response.read(),
        status=response.status,
        mimetype=response.getheader('Content-Type')
    )
    return response


@app.route('/firestore')
def firestore():
    doc_ref = db.collection(u'articles').document(u'brexit')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815,
        u'date': datetime.now()
    })
    return "YEEESSS"


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
