import logging
from flask import Blueprint, render_template, request, current_app
from classes.data_manager import DataManager
from classes.exeptions import DataSourceBrokenEx
from loader.exeptions import PictureFormatNotSupported


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logger = logging.getLogger("basic")


@main_blueprint.route('/')
def main_page():
    return render_template("main_html/main_page.html")


@main_blueprint.route('/search/')
def search_page():
    path = current_app.config.get("POST_PATH")
    data_manager = DataManager(path)
    s = request.values.get("s", None)
    logger.info(f"Выполняется поиск {s}")
    if s is None or s == "":
        posts = data_manager.get_all()
    else:
        posts = data_manager.get_by_search(s)
    return render_template("main_html/search_page.html", s=s, posts=posts)


@main_blueprint.errorhandler(DataSourceBrokenEx)
def data_source_broken_error(e):
    logger.error("Ошибка чтения .json файла")
    return "Страница не доступна, обратитесь к администратору"


@main_blueprint.errorhandler(PictureFormatNotSupported)
def picture_format_not_supported(e):
    logger.error("Ошибка формата загрузки изображения")
    return "Формат изображения не поддерживается, используйте другой формат"
