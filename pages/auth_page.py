from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru'

        super().__init__(web_driver, url)



    tab_phone = WebElement(id='t-btn-tab-phone'),
    tab_email = WebElement(id='t-btn-tab-mail'),
    tab_login = WebElement(id='t-btn-tab-login'),
    tab_ls = WebElement(id='t-btn-tab-ls'),
    text_ls = WebElement(LINK_TEXT='Лицевой счёт')


    input_aut = WebElement(id='username')
    input_password = WebElement(id='password')

    captcha = WebElement(id='captcha')

    btn_aut = WebElement(id='kc-login')


    forgot_password = WebElement(XPATH='//*[@id="forgot_password"]')# 'Забыл пароль'

    btn_Continue = WebElement(id='reset')
    code_input = WebElement(XPATH=' // *[ @ id = "page-right"] / div / div / div / form / div / div')#поле ввода кода из смс
    btn_back = WebElement(XPATH='// *[ @ id = "page-right"] / div / div / div / form / button')#кнопка вернуться назад


    form_error_message = WebElement(LINK_TEXT='Неверный логин или пароль')

    forgot_password_orange = WebElement(class_name='rt-link--orange')

    text_ls_error = WebElement(LINK_TEXT='Проверьте, пожалуйста, номер лицевого счета')
