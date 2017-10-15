"""
lazy-teacher
"""

from flask import Flask, jsonify, redirect, render_template, request, session, url_for
from oauth2client import client

from lazy_teacher.drive import Drive
from lazy_teacher.process import sanitize, count

app = Flask(__name__)

@app.route('/')
def index():
    """
    Default Route
    """

    return render_template('index.html')

@app.route('/oauth2callback')
def oauth2callback():
    flow = client.flow_from_clientsecrets(
        'client_secret.json',
        scope='https://www.googleapis.com/auth/drive.readonly',
        redirect_uri=url_for('oauth2callback', _external=True))
    if 'code' not in request.args:
        auth_uri = flow.step1_get_authorize_url()
        return redirect(auth_uri)
    else:
        auth_code = request.args.get('code')
        credentials = flow.step2_exchange(auth_code)
        session['google_credentials'] = credentials.to_json()
        return redirect(url_for('grade'))

@app.route('/grade')
def grade():
    """
    Grade Route
    """

    if 'google_credentials' not in session:
        return redirect(url_for('oauth2callback'))
    credentials = client.OAuth2Credentials.from_json(session['google_credentials'])
    if credentials.access_token_expired:
        return redirect(url_for('oauth2callback'))
        

    drive = Drive(credentials)
    files = drive.get_files()
    doc = files[0]['id']
    text = drive.get_text(doc, 'text/plain')

    clean_text = sanitize(text)
    index = count(clean_text)

    return jsonify(index)

if __name__ == '__main__':
    import uuid
    app.secret_key = str(uuid.uuid4())
    app.run(host='0.0.0.0',debug=True)
