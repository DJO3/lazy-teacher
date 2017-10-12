"""
lazy-teacher
"""

import os
from flask import Flask, jsonify, render_template, request

from lazy_teacher.drive import Drive
from lazy_teacher.process import sanitize, count

app = Flask(__name__)

@app.route('/')
def index():
    """
    Default Route
    """

    drive = Drive()
    files = drive.get_files()
    doc = files[0]['id']
    text = drive.get_text(doc, 'text/plain')

    clean_text = sanitize(text)
    index = count(clean_text)

    return jsonify(index)
    # return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
