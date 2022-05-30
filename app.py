from flask import Flask, render_template, send_from_directory

from main.main import main_blueprint
from loader.loader import loader


app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(loader)

app.config["POST_PATH"] = "data/posts.json"
app.config["UPLOAD_FOLDER"] = "uploads/images.json"


# @app.route('/')
# def main_page(s):
#     """Главная страница (поиск постов)"""
#     return render_template('main.html', s=s)
#     pass
#
#
# @app.route('/search/?s=поиск')
# def main_page():
#     """Страничка ленты по тегу"""
#     pass
#
#
# @app.route('/post', methods=["GET"])
# def main_page():
#     """Страничка добавления поста"""
#     pass
#
#
# @app.route('/post', methods=["POST"])
# def main_page():
#     """Страничка после добавления поста"""
#     pass


if __name__ == "__main__":
    app.run(debug=True)
