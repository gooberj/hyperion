from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/text")
def hello_world():
    return 

@app.route('/serverfiles/<filename>')
def download_file(filename):
    return send_from_directory(directory='serverfiles', path=filename, as_attachment=True)
app.run(debug=True, port=80)