from flask import Flask, request
import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd
import datetime

app = Flask(__name__)

import base64
import requests


@app.route("/acces_token")
def access():
    return 'hi'


@app.route("/callback")
def test():
    CLIENT_ID = '22D5TC'
    CLIENT_SECRET = '77e03cdf3389696430af37becf5c8291'
    base = base64.b64encode(CLIENT_ID + ":" + CLIENT_SECRET)
    code = request.args['code']
    response = requests.post("https://api.fitbit.com/oauth2/token",
                             data={"Authorization": "Basic " + base,
                                   'grant_type': 'authorization_code',
                                   'client_id': CLIENT_ID,
                                   'redirect_uri': "https://sherlie.iqube.io/access_token",
                                   'code': code})
    return 'Hello'


@app.route('/')
def hello_world():
    CLIENT_ID = '22D5TC'
    CLIENT_SECRET = '77e03cdf3389696430af37becf5c8291'

    server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET, redirect_uri="https://sherlie.iqube.io/callback")
    server.browser_authorize()
    ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
    REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
    auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN,
                                 refresh_token=REFRESH_TOKEN)

    return 'Hello World!'


if __name__ == '__main__':
    app.run()
