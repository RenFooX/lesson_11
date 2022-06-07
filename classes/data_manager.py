import json
from classes.exeptions import DataSourceBrokenEx


class DataManager:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        """ Загружает/получает данные с файла """
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            raise DataSourceBrokenEx("The data file is corrupted")
        return data

    def save_data(self, data):
        """ Перезаписывает/ сохраняет данные """
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def get_all(self):
        """ Отдает все полученные данные """
        data = self.load_data()
        return data

    def get_by_search(self, substring):
        """ Отдает данные по критерию поиска (substring) """
        posts = self.load_data()
        substring = substring.lower()
        coincidences = [post for post in posts if substring in post['content'].lower()]
        return coincidences

    def add_post(self, post):
        """ Добавляет новый пост """
        if type(post) != dict:
            raise TypeError("Ошибка типа данных")

        posts = self.load_data()
        posts.append(post)
        self.save_data(posts)
