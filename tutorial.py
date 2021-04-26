from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime
import requests
import os

app = Flask(__name__)
img_path = ""

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        if request.form['submit_button'] == "Generate with URL":
            return redirect(url_for("url"))
        elif request.form['submit_button'] == "Upload Your Own Image":
            return redirect(url_for("upload"))
        elif request.form['submit_button'] == 'Home':
            return render_template("index.html")
    else:
        return render_template("index.html")

@app.route("/url", methods=["POST", "GET"])
def url():
    if request.method == "POST":
        imgurl = request.form["imgurl"]
        ttext = request.form["ttext"]
        btext = request.form["btext"]
        result = f"https://api.memegen.link/images/custom/{ttext}/{btext}.png?background={imgurl}"
        response = requests.get(result)
        timestamp = datetime.now()
        img_name = str(timestamp)+".png"
        img_path = img_name
        full_fname = os.path.join('static',img_name)
        with open(full_fname,"wb") as file:
            file.write(response.content)
        return render_template("meme.html", user_image = full_fname)
    else:
        return render_template("form.html")

@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        if request.form['submit_button'] == "Generate with URL":
            return redirect(url_for("url"))
        elif request.form['submit_button'] == "Upload Your Own Image":
            return redirect(url_for("upload"))
        elif request.form['submit_button'] == 'Home':
            return redirect(url_for("home"))
    else:
        return render_template("mode.html")

if __name__ == "__main__":
    app.run()

