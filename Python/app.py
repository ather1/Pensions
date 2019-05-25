import datetime
from flask  import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.day==25 and now.month ==5
    # text = "Yes"  if  new_year  else "No"
    return  render_template("index.html",new_year = new_year)
    