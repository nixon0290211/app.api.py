from flask import Flask, render_template, request, redirect, flash, request_finished
from process import paste_frame
import secrets,json

app = Flask(__name__)
# セッション情報を暗号化するためのキー設定
app.secret_key = secrets.token_urlsafe(32)


def cat():
    response = requests.get("https://thecatapi.com/”)
    # 返ってきたデータ(文字)をそのまま表示
    print(response.text)
    #jsonデータとしてロードして特定のデータのみ
    print(json.loads(response.text)[“results”][0][“address1”])
def dog():
    response = requests.get("https://dog.ceo/api/breeds/image/random”)
    # 返ってきたデータ(文字)をそのまま表示
    print(response.text)
    #jsonデータとしてロードして特定のデータのみ
    print(json.loads(response.text)[“results”][0][“address1”])
def fox():
    response = requests.get("https:\/\/randomfox.ca\/?i=22”)
    # 返ってきたデータ(文字)をそのまま表示
    print(response.text)
    #jsonデータとしてロードして特定のデータのみ
    print(json.loads(response.text)[“results”][0][“address1”])

@app.route("/")
def show_from():
    return render_template("index.html")

@app.route("/post", methods=["GET,POST"])
def upload_image():
    if request.method == "POST":
        animal = request.form["animal"]
        if animal == "cat":
            outanimal = api_get.cat()

        elif animal == "dog":
            outanimal = api_get.dog()

        elif animal == "fox":
            outanimal = api_get.fox()

        else:
            outanimal = ""

        return render_template("post.html", outanimal=outanimal)

    # return redirect("/")
    # if request.method == "GET":
    #     posts = Post.query.all() 
    # return redirect(index.html,post =post)

    #     file = request.files["file"]
    #     else:title =request.from.get(title)


    #     if file.filename == "":
    #         flash("ファイルが選択されていません")
    #         return redirect(request.url)

    #     if file:
    #         outfile = paste_frame(file)
    #         return render_template("upload.html", outfile=outfile)

    # return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

# If 猫
# 　return “猫”
# ElseIf 犬
#    Return “犬”
# Else  狐
#    Return “狐”
