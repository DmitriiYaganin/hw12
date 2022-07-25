import json

"""
Загрузка всех постов из posts.json
"""
def load_posts() -> list[dict]:
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


"""
Поиск постов по ключу
"""
def get_posts_by_word(word: str) -> list[dict]:
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


"""
Добавление поста и картинки
"""
def add_post(post: dict) -> dict:
    posts = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)
    return post
