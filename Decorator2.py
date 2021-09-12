from datetime import datetime
import json
import os

def get_path(path):

    def decorator_logger(function):
        def get_log(*args, **kwargs):
            date = datetime.today().replace(second=0, microsecond=0)
            new_function = function(*args, **kwargs)
            log_str = f'{date}, {decorator_logger.__name__}, {args}, {kwargs}, {path}'
            with open('log_path.json', 'w', encoding='utf-8') as f:
                json.dump(log_str, f, ensure_ascii=False)
            print(f'Данные записаны в файл', 'log_path.json')
            print(f'Путь к файлу', path)
            return new_function
        return get_log
    return decorator_logger
path = os.path.abspath('log_path.json')

if __name__ == '__main__':
    @get_path(path)
    def logger(first_name, last_name):
        return first_name, last_name
    logger('Jon', 'Snow')