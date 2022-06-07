import logging
from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint
import logg

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

app.config["POST_PATH"] = "data/posts.json"
app.config["UPLOAD_FOLDER"] = "uploads/images"

logg.create_logger()
logger = logging.getLogger("all")


@app.route("/uploads/<path:path>")
def statistic_dir(path):
    logger.info("Приложение запускается")
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()
