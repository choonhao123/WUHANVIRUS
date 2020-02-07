from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    if text.isdigit() == True:
        if int(text) >= 38:
            return render_template("wuhan.html")

        else:
            return render_template("nowuhan.html")
    else:
        return "Enter a Temperature"