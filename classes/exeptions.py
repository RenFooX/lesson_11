class DataSourceBrokenEx(Exception):
    """ Класс для ошибки при открытии/чтении json файла"""
    pass


class OutOfFreeNamesError(Exception):
    """ Класс для ошибки при генерации имен изображения"""
    pass
