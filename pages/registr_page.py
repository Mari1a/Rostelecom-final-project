from pages.base import WebPage
from pages.elements import WebElement
import random

class RegistrPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru'

        super().__init__(web_driver, url)



    kc_register = WebElement(id='kc-register')
    input_name = WebElement(name='firstName')
    input_last = WebElement(name='lastName')
    input_region = WebElement(XPAH='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]')

    aut_touch =WebElement(CSS_CILEKTOR='body > apm_do_not_touch')

    region = WebElement(LINK_TEXT='Москва г')
    my_email = WebElement(id="address")
    my_pass = WebElement(id="password")
    pass_confirm = WebElement(id="password-confirm")
    register_btn = WebElement(name="register")

    card_container_title = WebElement(XPATH='//*[@id="page-right"]/div/div/h1')

    meta_error_1 = WebElement(XPATH='// *[ @ id = "page-right"] / div[1] / div[1] / div[1] / form[1] / div[1] / div[1] / span[1]')

    meta_error_2 = WebElement(XPATH='// *[ @ id = "page-right"] / div[1] / div[1] / div[1] / form[1] / div[1] / div[2] / span[1]')