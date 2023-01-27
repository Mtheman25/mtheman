import os
from flask import Flask, render_template, send_from_directory, redirect#, request#, url_for

app = Flask(__name__)

@app.route("/")
def homeredir():
  return redirect('home')

@app.route("/home")
def home():
  return render_template('index.html')

@app.route("/projects")
def projects():
  return render_template('projects.html')

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=3000)