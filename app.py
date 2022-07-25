import logging

from flask import Flask, request, render_template, send_from_directory

from loader.views import loader_blueprint
from main.views import main_blueprint

POST_PATH = "posts.json"  # Путь файла
UPLOAD_FOLDER = "uploads/images"  # Путь сохранения

app = Flask(__name__)


app.register_blueprint(main_blueprint)  # блюпринт mail->views
app.register_blueprint(loader_blueprint)  # блюпринт loader->views

logging.basicConfig(filename="basic.log", level=logging.INFO)  # Логирование в файл basic.log

"""
Вьюшка для загрузки
"""
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

app.run()
