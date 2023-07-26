from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = 'https://b2c.passport.rt.ru'

# TK-018
def test_Forgot_password(web_browser):
    """функционал ссылки "Забыл пароль"""
    driver = web_browser
    driver.get(base_url)
    driver.implicitly_wait(10)
    forgot_password = driver.find_element(By.LINK_TEXT, 'Забыл пароль')
    forgot_password.click()

    element_2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/h1[1]')))
    if element_2:
        print('мы на странице Восстановление пароля.')

    else:
        pass









