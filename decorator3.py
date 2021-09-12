import json
from Decorator2 import path, get_path

wiki_url = 'https://ru.wikipedia.org/wiki/'
@get_path(path)
class Country_w:
    def __init__(self, path, start):
        self.file = open(path, encoding='utf-8')
        self.json = json.load(self.file)
        self.start = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        country_url = {}
        self.start += 1
        if self.start == len(self.json):
            raise StopIteration

        country = self.json[self.start]['name']['common']
        country_link = f'{wiki_url}{country}'
        country_url[country] = country_link


        return country_url

if __name__ == '__main__':
    data = Country_w('countries.json', 0)
    with open('country_link.json', 'w', encoding='utf-8') as f:
        for item in data:
            json.dump(item, f, ensure_ascii=False, indent=2)

    print('Данные сохранены в файл "country_link.json"')