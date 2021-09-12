from datetime import datetime
import json

def decorator_logger(function):
    def get_log(*args, **kwargs):
        date = datetime.now().replace(second=0, microsecond=0)
        new_function = function(*args, **kwargs)
        log_str = f'{date}, {decorator_logger.__name__}, {args}, {kwargs}'
        with open('logger.json', 'w', encoding='utf-8') as f:
            json.dump(log_str, f, ensure_ascii=False)
        print(f'Данные записаны в файл')
        return new_function
    return get_log

@decorator_logger
def logger(first_name, last_name):
    return first_name, last_name

logger('Jon', 'Snow')