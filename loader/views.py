import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from functions import add_post
from loader.utils import save_picture

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


"""
Вьюшка страницы для создания поста
"""
@loader_blueprint.route('/post')
def post_page():
    return render_template('post_form.html')


"""
Вьюшка страницы для создания поста и добавления поста и картинки
"""
@loader_blueprint.route('/post', methods=['POST'])
def add_post_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:  # Если не добавил файл или пост, вылетает сообщение
        return 'Нет картинки или текста'

    if picture.filename.split('.')[-1] not in ['jpeg', 'png']:  # Поддерживаемый формат загрузки файлов
        logging.info('Загружаемый файл не картинка')  # неверный файл загружается
        return 'Неверное расширение файла'
    try:
        picture_path = '/' + save_picture(picture)
    except FileNotFoundError:  # Обработка ошибки
        logging.error('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:  # Обработка ошибки
        return 'Не читаемый файл'
    post = add_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post=post)
