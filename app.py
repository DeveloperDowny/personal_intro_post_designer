import base64
from PIL import Image
from flask import Flask, render_template, request, jsonify, url_for
from io import BytesIO
from werkzeug.utils import redirect

from string_util import make_file_safe_name

UPLOAD_FOLDER = "static"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

import os
from flask import send_from_directory


@app.route("/next", methods=["POST", "GET"])
def next():
    return render_template("next.html")


@app.route("/download/<name>", methods=["POST", "GET"])
def download(name):
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, path=name, as_attachment=True)


@app.route("/upload", methods=["POST", "GET"])
def upload():
    image_encoded = request.form.get("image")
    image_name = request.form.get("image_name")

    if image_encoded != None:
        image_parts = image_encoded.split(";base64,")
        image_type_aux = image_parts[0].split("image/")
        image_type = image_type_aux[1]

        file = UPLOAD_FOLDER + "/" + image_name + ".png"
        im = Image.open(BytesIO(base64.b64decode(image_parts[1])))
        im.save(file, quality="keep")
    else:
        print("image is none")

    return jsonify(status="success")


@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("home_page.html")


@app.route("/design", methods=["POST", "GET"])
def design():
    return render_template("design.html")


@app.route("/preview", methods=["POST", "GET"])
def preview():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    insta_id = request.form["insta_id"]
    intro = request.form["intro"]
    full_name = first_name + " " + last_name
    full_name = make_file_safe_name(full_name)
    insta_id = make_file_safe_name(insta_id)
    branch = request.form["branch"]
    image_name = request.form["image_name"]
    print(image_name)
    if image_name != "undefined":
        file = UPLOAD_FOLDER + "/" + image_name + ".png"
        import design_post
        design_post.design_post(insta_id, first_name + " " + last_name, intro, branch, file, app)
    else:
        print("image undefined in py")
        return render_template("preview.html", img_src=f"place_holder.png")

    return render_template("preview.html", img_src=f"{full_name}_{insta_id}.png")