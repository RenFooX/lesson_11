from flask import Blueprint, render_template, request, current_app
from cls.data_class import DataManager
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template("")


@main_blueprint.route('/search/')
def search_page():

    path = current_app.config.get("POST_PATH")
    dataclasses = DataManager(path)

    s = request.values.get("s", None)
    if s in None or s == "":
        posts = dataclasses.get_all()
    else:
        posts = dataclasses.search(s)
    return render_template("", s=s, posts=posts)
