import os
import logging

from flask import Blueprint, render_template, request


from config import POSTS_FILE_PATH, UPLOAD_FOLDER
from utils import load_posts_from_json, upload_posts_to_json

# url_prefix="/post",

loader_blueprint = Blueprint('loader_blueprint', __name__, static_folder="/static/css/", template_folder="templates")
logger = logging.getLogger("basic")


@loader_blueprint.route('/post/')
def main_page():
    logger.debug("пеерход на старницу добавление поста")
    return render_template("post_form.html")

@loader_blueprint.route('/post/', methods=["POST"])
def upload_page():

    file = request.files['picture']
    filename = file.filename
    logger.debug(f"запрос файла имя: {filename}")
    content = request.values['content']
    logger.debug(f"запрос содержание поста: {content}")
    try:
        posts = load_posts_from_json(POSTS_FILE_PATH)
        logger.debug(f"загрузка из json файла {POSTS_FILE_PATH}")
    except FileNotFoundError:
        error_decipher = " Файл json не найден "
        return render_template("error_page.html", error_decipher=error_decipher)
    # try:
    if not filename.split('.')[-1] in ["jpg", "png"]:
        logger.debug(f"картинка с расширением {filename.split('.')[-1]}")
        error_decipher = "Картинка должна иметь расширение jpg или png "
        return render_template("error_page.html", error_decipher=error_decipher)
    if file == None or content == "":
        error_decipher = "Пост должен содержать картинку и текст"
        return render_template("error_page.html", error_decipher=error_decipher)
    else:
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        logger.debug(f"Сохрание файла {os.path.join(UPLOAD_FOLDER, filename)}")
        # except PermissionError:
        #     return "<h1>Что за пост без фото?</h1>"
        posts.append({'pic': f"/{os.path.join(UPLOAD_FOLDER, filename)}", 'content': content})
        logger.debug(f"Добавление поста в json файл")
        upload_posts_to_json(posts)

        pic = f"/{os.path.join(UPLOAD_FOLDER, filename)}"
        return render_template("post_uploaded.html", pic=pic, content=content)
