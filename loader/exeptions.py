class OutOfFreeNamesError(Exception):
    """ Класс для ошибки при генерации имен изображения """
    pass


class PictureFormatNotSupported(Exception):
    """ Класс для ошибки не поддерживаемого формата изображения """
    pass


class PictureNotLoadedError(Exception):
    """ Класс для ошибки при загрузке изображения """
    pass
