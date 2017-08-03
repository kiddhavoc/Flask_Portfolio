from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/Projects")
def projects():
    return render_template("projects.html")

@app.route("/About")
def about():
    return render_template("about.html")

app.run(debug=True)