import pytest
from pages.auth_page import AuthPage
from pages.registr_page import RegistrPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password, valid_phone, val_login, va_ls
from settings import noValid_email, noValid_phone, noV_login, noV_ls, namE, last_name
base_url = 'https://b2c.passport.rt.ru'

# TK _02-05
@pytest.mark.positive
@pytest.mark.parametrize('ls', [valid_phone, valid_email, val_login, va_ls],
                         ids=['phone', "email", 'login', 'ls'])
def test_authorization(web_browser, ls):
    """функционал  авторизации  по мобильному телефону, кнопка "Телефон" с валидными данными
    функционал  авторизации по электронной почте, кнопка "Почта"с  валидными данными
    функционал  авторизации по логину, кнопка "Логин"с  валидными данными
    функционал  авторизации по лицевому счету, кнопка "Лицевой счет"с  валидными данными"""

    page = AuthPage(web_browser)
    page.input_aut.send_keys(ls)
    page.input_password.send_keys(valid_password)
    page.btn_aut.click()
    if page.captcha:
        print('Введите символы с картинки')
    else:
        # Если авторизация прошла успешно отображения  страница kличный кабинет
        assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


# TK-6-9
@pytest.mark.negative
@pytest.mark.parametrize('ls_no', [noValid_phone, noValid_email, noV_login, noV_ls],
                         ids=['nov_phone', "nov_email", 'nov_login', 'nov_ls'])
def test_authorization_negative(web_browser, ls_no):
    """функционал  авторизации  по мобильному телефону, кнопка "Телефон" с невалидными данными
    функционал  авторизации по электронной почте, кнопка "Почта"с  невалидными данными
    функционал  авторизации по логину, кнопка "Логин"с  невалидными данными
    функционал  авторизации по лицевому счету, кнопка "Лицевой счет"с  невалидными данными"""
    page = AuthPage(web_browser)
    page.input_aut.send_keys(ls_no)
    page.input_password.send_keys(valid_password)
    page.btn_aut.click()
    # if page.captcha:
    #     print('Введите символы с картинки')
    # else:
    assert page.forgot_password == 'Забыл пароль' or 'Неверный логин или пароль'


def generate_string(n):
   return "я" * n
def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыь' #эюя'

# Здесь мы взяли 20 популярных китайских иероглифов
def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'

def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


# TK-10-16
@pytest.mark.negative
@pytest.mark.parametrize('N_p', [""
                            , generate_string(255)
                            , generate_string(1001)
                            , russian_chars()
                            , russian_chars().upper()
                            , chinese_chars()
                            , special_chars()
                            ]
   , ids=['empty string'
          , '255 symbols'
          , 'more than 1000 symbols'
          , 'russian'
          , 'RUSSIAN'
          , 'chinese'
          , 'specials'
          ])

def test_authorization_negative_pass(web_browser, N_p):
    """функционал поля ввода пароль с негативные проверки"""
    page = AuthPage(web_browser)
    page.input_aut.send_keys(valid_email)
    page.input_password.send_keys(N_p)
    page.btn_aut.click()
    if web_browser.current_url != base_url:
        # Если переход в kличный кабинет не удался, то сделать скриншот
        web_browser.save_screenshot('result_roselecom.png')
    else:
        pass

    assert page.forgot_password == 'Забыл пароль' or 'Неверный логин или пароль'


# TK--019-020
@pytest.mark.positive
@pytest.mark.parametrize('ls', [valid_phone, valid_email],
                         ids=['phone', "email"])
def test_registration(web_browser, ls):
    """Регистрация на веб приложении Ростелеком с помощью  email или телефона"""
    page = RegistrPage(web_browser)
    page.kc_register.scroll_to_element()
    page.kc_register.click()
    page.input_name.send_keys(namE)
    page.input_last.send_keys(last_name)
    # page.input_region.send_keys('Москва')
    page.my_email.send_keys(ls)
    page.my_pass.send_keys(valid_password)
    page.pass_confirm.send_keys(valid_password)
    page.register_btn.click()
    if page.card_container_title:
        print('Подтверждение регистрации')
    else:
        raise Exception("ошибка заполнения данных")


# TK-021-27
@pytest.mark.negative
@pytest.mark.parametrize('Data', ["Г"
                            , generate_string(29)
                            , generate_string(31)
                            , russian_chars()
                            , russian_chars().upper()
                            , chinese_chars()
                            , special_chars()
                            ]
   , ids=['Г'
          , '29 symbols'
          , '31 symbols'
          , '30 russian'
          , 'RUSSIAN'
          , 'chinese'
          , 'specials'
          ])
def test_Personal_data(web_browser, Data):
    """Функцианал поля ввода имени и фамилии в форме регистрации"""
    page = RegistrPage(web_browser)
    page.kc_register.scroll_to_element()
    page.kc_register.click()
    page.input_name.send_keys(Data)
    page.input_last.send_keys(Data)

    if page.meta_error_1:
        try:
            page.bad_el = WebDriverWait(web_browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '// *[ @ id = "page-right"] / div[1] / div[1] / div[1] / form[1] / div[1] / div[1] / span[1]')))
        except Exception as e:
            pass




