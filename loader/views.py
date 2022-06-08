import logging
from flask import Blueprint, render_template, request, current_app
from classes.data_manager import DataManager
from loader.exeptions import OutOfFreeNamesError, PictureNotLoadedError
from loader.upload_manager import UploadManager

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')
logger = logging.getLogger("basic")


@loader_blueprint.route('/post', methods=['GET'])
def page_by_upload_form():
    """ Создается представления для отображения формы загрузки контента на сайт с методом GET """
    return render_template("loader_html/load_form.html")


@loader_blueprint.route('/post', methods=['POST'])
def page_by_created_new_post():
    """ Создается представление для с методом POST """

    path = current_app.config.get("POST_PATH")
    data_manager = DataManager(path)
    upload_manager = UploadManager()

    # Получение данных
    picture = request.files.get('picture', None)
    content = request.values.get('content', '')

    # Сохранение изображения с помощью менеджера загрузки
    filename_saved = upload_manager.save_with_random_name(picture)

    # Получение web - пути для клиента
    web_path = f"/uploads/images/{filename_saved}"

    # Создаем данные для записи в файл
    post = {"pic": web_path, "content": content}

    # Добавляем данные в json файл
    data_manager.add_post(post)

    return render_template("loader_html/post_uploaded.html", pic=web_path, content=content)


@loader_blueprint.errorhandler(OutOfFreeNamesError)
def error_for_save_to_names(e):
    """ Создаем функцию для обработки ошибок лимит генерации имен для изображений
     с последующей записью в logger"""
    logger.error("Достигнут лимит генерации имен изображений")
    return "Лимит для сохранения изображений исчерпан , обратитесь администратору сайта" \
           "или попробуйте позже"


@loader_blueprint.errorhandler(PictureNotLoadedError)
def picture_not_loaded_error(e):
    """ Создаем функцию для обработки ошибок при загрузке изображения
         с последующей записью в logger"""
    logger.error("Ошибка при загрузке изображения")
    return "Ошибка загрузки изображения," \
            "попробуйте еще раз или обратитесь к администратору"
