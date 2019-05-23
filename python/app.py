from flask import Flask , render_template

app  = Flask(__name__)

@app.route("/")
def index():
    names = ["Alice", "Dave","Tom"]
    return render_template("index.html",names = names)


@app.route("/<string:name>")
def hello(name):
    name = name.capitalize();
    return f"hello! {name}"