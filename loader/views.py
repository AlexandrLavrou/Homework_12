from flask import Blueprint, render_template, request


from config import POSTS_FILE_PATH
from utils import load_posts_from_json, upload_posts_to_json

import logging

logger = logging.getLogger("basic")
logger.setLevel("DEBUG")

stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

file_handler = logging.FileHandler("logs/basic.txt")
logger.addHandler(file_handler)

file_handler_2 = logging.FileHandler("logs/basic_2.txt")
logger.addHandler(file_handler_2)

formatter = logging.Formatter("%(levelname)s %(asctime)s : %(message)s  %(pathname)s >> %(funcName)s")
stream_handler.setFormatter(formatter)


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

    posts.append({'pic': f'/uploads/images/{filename}', 'content': content})
    upload_posts_to_json(posts)
    try:
        file.save(f'uploads/{filename}')
    except PermissionError:
        return "<h1>Что за пост без фото?</h1>"
    else:
        return render_template("post_uploaded.html", pic=f'/uploads/images/{filename}', content=content)
