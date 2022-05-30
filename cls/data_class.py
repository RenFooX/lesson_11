import json


class DataManager:

    def __int__(self, path):
        self.path = path

    def data_load(self):
        """ Загружает данных с файла """
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def data_save(self, data):
        """ Перезаписывает/ сохраняет данные """
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def give_all(self):
        """ Отдает все полученные данные """
        data = self.data_load()
        return data

    def give_by_search(self, substring):
        """ Отдает данные по критерию поиска (substring) """
        data = self.data_load()
        substring = substring.lower()
        coincidences = [post for post in data if substring in post["content"].lower()]
        return coincidences

    def add_posts(self, post):
        """ Добавляет новый пост """
        if type(post) != dict:
            raise TypeError("Ошибка типа данных")
        data = self.data_load()
        data.append(post)
        self.data_save(post)
