from flask import Flask, render_template, request, redirect
import os, random, math
app = Flask(__name__)

imgFiles = os.listdir("static/images")

@app.route("/")
def index():
    #print(imgFiles)
    return render_template("index.html", num = -1, imgFiles = imgFiles)

@app.route("/<x>")
def show_images(x):
    return render_template("index.html", num = int(x), imgFiles = imgFiles)

@app.route("/danger")
def danger():
    print("*" * 42)
    print("***** A user accessed 'danger' page! *****")
    print("*" * 42)
    return redirect("/")

@app.route("/random/<x>")
def getRandom(x):
    #print(imgFiles)
    idx = len(imgFiles) - 1
    for i in range(len(imgFiles)):
        rnd = math.floor(random.random() * idx)
        imgFiles[rnd], imgFiles[idx] = imgFiles[idx], imgFiles[rnd]
        idx -= 1
    #print(imgFiles)

    return render_template("index.html", num = int(x), imgFiles = imgFiles)
    

if __name__ == "__main__":
    app.run(debug = True)
