from  flask import  Flask , render_template

app = Flask(__name__)

@app.route("/")
def Index():
    return render_template("index.html") 

text=["This the first line on the first page","This is the first line on the second page","This is the first line on third page"]
@app.route("/first")
def first():
    return text[0]

@app.route("/second")
def second():
    return text[1]

@app.route("/third")
def  third(): 
    return text[2]
    