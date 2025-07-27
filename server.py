from flask import Flask, request, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save('files/' + uploaded_file.filename)
    return 'Success'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/downloads/<path:filename>')
def download_from_directory(filename):
    directory = 'files/'  # Replace with your directory
    return send_from_directory(directory, filename, as_attachment=True)

@app.route("/files")
def files():
    files = ''
    for i in os.listdir("files/"):
        files = files + f"<li><a href="f"downloads/{i}>{i}</a></li>\n"
    return files
app.run(debug=True, port=80)