import json


from main.posts import Posts
from config import POSTS_FILE_PATH

# path = "../posts.json"


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
    searched_post = []
    for _ in posts_:
        if subcontent.lower() in _.content.lower():
            searched_post.append(_)
        else:
            continue
    return searched_post

# "../posts.json"

# print(get_posts_by_content("../posts.json", "Ага"))
