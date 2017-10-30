"""
lazy-teacher
"""
import os
from flask import Flask, jsonify, redirect, request, session
from oauth2client import client

from lazy_teacher.drive import Drive
from lazy_teacher.process import sanitize, count

DOMAIN = os.environ['DOMAIN']
app = Flask(__name__)

@app.route('/')
def index():
    """
    Default Route
    """

    hello = {
        "msg": "Hello World"
    }

    return jsonify(hello)

@app.route('/oauth2callback')
def oauth2callback():
    flow = client.flow_from_clientsecrets(
        'client_secret.json',
        scope='https://www.googleapis.com/auth/drive.readonly',
        redirect_uri=f'http://{DOMAIN}/api/oauth2callback')
    if 'code' not in request.args:
        auth_uri = flow.step1_get_authorize_url()
        return redirect(auth_uri)
    else:
        auth_code = request.args.get('code')
        credentials = flow.step2_exchange(auth_code)
        session['google_credentials'] = credentials.to_json()
        return redirect(f'http://{DOMAIN}/api/folders')

@app.route('/folders')
def folders():
    """
    List all folders
    """

    if 'google_credentials' not in session:
        return redirect(f'http://{DOMAIN}/api/oauth2callback')
    credentials = client.OAuth2Credentials.from_json(session['google_credentials'])
    if credentials.access_token_expired:
        return redirect(f'http://{DOMAIN}/api/oauth2callback')

    drive = Drive(credentials)
    folders = drive.get_folders()

    for folder in folders['files']:
        folder_name = folder['name']
        folder['grade_url'] = f'http://{DOMAIN}/api/grade?folder_name={folder_name}'
        
    return jsonify(folders['files'])

@app.route('/grade')
def grade():
    """
    Grade Route
    """

    if 'google_credentials' not in session:
        return redirect(f'http://{DOMAIN}/api/oauth2callback')
    credentials = client.OAuth2Credentials.from_json(session['google_credentials'])
    if credentials.access_token_expired:
        return redirect(f'http://{DOMAIN}/api/oauth2callback')

    if 'folder_name' not in request.args:
        return "folder_name parameter missing!"

    drive = Drive(credentials)
    files = drive.get_files(request.args['folder_name'])

    index = {'count': 0}
    for doc in files:
        text = drive.get_text(doc['id'], 'text/plain')
        clean_text = sanitize(text)
        local_index = count(clean_text)
        local_index['grade'] = None

        index[doc['name']] = local_index
        index['count'] += 1

    return jsonify(index)

if __name__ == '__main__':
    import uuid
    app.secret_key = str(uuid.uuid4())
    app.run(host='0.0.0.0',debug=True)
