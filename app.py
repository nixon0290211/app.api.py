from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route("/")
def api():
    return render_template("index.html")


@app.route("/post", methods=["POST"])
def api2():
    answer = request.form["change_js"]
    if answer == "cat":
        res = requests.get("https://api.thecatapi.com/v1/images/search")
        photo = json.loads(res.text)[0]["url"]

    elif answer == "dog":
        res = requests.get("https://dog.ceo/api/breeds/image/random")
        photo = json.loads(res.text)["message"]
    else:
        res = requests.get("https://randomfox.ca/floof/")
        photo = json.loads(res.text)["image"]

    return render_template("upload.html", outfile=photo)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5002)

# If 猫
# 　return “猫”
# ElseIf 犬
#    Return “犬”
# Else  狐
#    Return “狐”
