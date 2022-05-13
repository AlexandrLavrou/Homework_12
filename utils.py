import json


from main.posts import Posts
from config import POSTS_FILE_PATH


def load_posts_from_json(post_path):
    with open(post_path, "r", encoding="utf-8") as file:
        posts = json.load(file)
        return posts


def convert_posts_to_class(posts):
    temp_posts = []
    for _post in posts:
        pic = _post.get("pic")
        content = _post.get("content")

        temp_post = Posts(pic, content)
        temp_posts.append(temp_post)
    return temp_posts


def upload_posts_to_json(posts):
    with open(POSTS_FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(posts, file, ensure_ascii=False, indent=4)


def get_posts_by_content(posts, subcontent):
    posts_ = convert_posts_to_class(posts)
    filtered_posts = []
    for post in posts_:
        if subcontent.lower() in post.content.lower():
            filtered_posts.append(post)

    return filtered_posts


