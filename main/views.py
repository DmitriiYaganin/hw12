import logging

from flask import Blueprint, render_template, request

from functions import get_posts_by_word
from json import JSONDecodeError

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


"""
Вьюшка начальной страницы
"""
@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


"""
Вьюшка страницы поиска
"""
@main_blueprint.route('/search/')
def search_page():
    search_query = request.args.get('s', '')
    logging.info('Выполняется поиск')
    try:
        posts = get_posts_by_word(search_query)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Не читаемый файл'

    return render_template('post_list.html', query=search_query, post=posts)
