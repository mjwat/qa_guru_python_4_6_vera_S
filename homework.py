import inspect
from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)

    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    is_dark_theme = True

    if time(hour=6, minute=0, second=0) < current_time < time(hour=22, minute=0, second=0):
        is_dark_theme = False

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    is_dark_theme = None

    if dark_theme_enabled_by_user is True or \
            time(hour=22, minute=0, second=0) <= current_time < time(hour=24, minute=0, second=0) or \
            time(hour=00, minute=0, second=0) <= current_time <= time(hour=6, minute=0, second=0):
        is_dark_theme = True
    else:
        is_dark_theme = False

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_user = [user for user in users if user["name"] == "Olga"][0]
    assert suitable_user == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_user = [user for user in users if user["age"] < 20]
    assert suitable_user == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def print_readable_function(func, *args):
    readable = f'{func.__name__}'.replace('_', ' ').title() + f" [{', '.join(args)}]"
    print(readable)
    return readable


def open_browser(browser_name):
    actual_result = print_readable_function(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_readable_function(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_readable_function(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"

