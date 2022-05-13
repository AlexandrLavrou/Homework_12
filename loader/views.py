import os

from flask import Blueprint, render_template, request


from config import POSTS_FILE_PATH, UPLOAD_FOLDER
from utils import load_posts_from_json, upload_posts_to_json


loader_blueprint = Blueprint('loader_blueprint', __name__, url_prefix="/post", static_folder="/static/css/", template_folder="templates")

@loader_blueprint.route('/')
def main_page():
    return render_template("post_form.html")

@loader_blueprint.route('/', methods=["POST"])
def upload_page():

    file = request.files['picture']
    filename = file.filename
    content = request.values['content']
    try:
        posts = load_posts_from_json(POSTS_FILE_PATH)
    except FileNotFoundError:
        return "<h1>Файл json не найден</h1>"
    # try:
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    # except PermissionError:
    #     return "<h1>Что за пост без фото?</h1>"
    posts.append({'pic': f"{os.path.join(UPLOAD_FOLDER, filename)}", 'content': content})
    upload_posts_to_json(posts)

    pic = f"{os.path.join(UPLOAD_FOLDER, filename)}"
    return render_template("post_uploaded.html", pic=pic, content=content)
