import os
import random
import logging
from loader.exeptions import PictureFormatNotSupported, PictureNotLoadedError, OutOfFreeNamesError
logger = logging.getLogger("basic")


class UploadManager:

    def get_check_filename(self, folder, file_type):
        """ Создание / Проверка имен изображения"""

        attemps = 0
        RANGE_OF_IMAGE_NUMBERS = 100000
        LIMITS_ATTEMPS_NAME = 1000000

        while True:
            pic_name = str(random.randint(0, RANGE_OF_IMAGE_NUMBERS))
            filename_to_save = f"{pic_name}.{file_type}"
            os_path = os.path.join(folder, filename_to_save)
            is_name_occupied = os.path.exists(os_path)

            if not is_name_occupied:
                return filename_to_save
            attemps += 1
            if attemps > LIMITS_ATTEMPS_NAME:
                raise OutOfFreeNamesError("No free name for save files")

    def is_file_type_valid(self, file_type):
        """ Проверка на валидность изображения """
        if file_type.lower() in ["jpg", "jpeg", "gif", "png", "webp", "tiff"]:
            return True
        return False

    def save_with_random_name(self, picture):
        """ Обработка загружаемого изображения """
        # Получение изображения
        filename = picture.filename
        file_type = filename.split('.')[-1]

        # Проверка формата изображения
        if not self.is_file_type_valid(file_type):
            raise PictureFormatNotSupported(f"Формат {file_type}, не поддерживается")

        # Генерация имени для изображения
        folder = os.path.join(".", "uploads", "images")
        filename_to_save = self.get_check_filename(folder, file_type)

        # Сохранение изображение под полученным именем
        try:
            picture.save(os.path.join(folder, filename_to_save))
        except FileNotFoundError:
            raise PictureNotLoadedError(f"{folder}, {filename_to_save}")
        return filename_to_save
