from datetime import datetime


def upper_case(old_func):
    def new_func(*args, **kwargs):
        result = old_func(*args, **kwargs)
        return result.upper()

    return new_func


def param_log(param):
    def logger(oldfunc):
        date = datetime.now()

        def newfunc(*args, **kwargs):
            result = oldfunc(*args, **kwargs)
            with open(param, 'a', encoding='utf-8') as fi:
                fi.write(f'Вызвали функцию с именем "{oldfunc.__name__}"\n'
                         f'c аргументами "{args}" и "{kwargs}"\n'
                         f'Время старта: {date}\n'
                         f'Возвращаемое значение: "{result}"\n'
                         f'________________________________\n')
                return result

        return newfunc

    return logger


@param_log(param=None)
def function():
    pass