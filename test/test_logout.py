from selenium import webdriver
import pytest
import time
from locators import burgerLocators
from selenium.webdriver.common.by import By


class burgerLogout:

    def test_logout(self):
        driver=webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login')

        driver.find_element(*burgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*burgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*burgerLocators.BUTTON_LOGIN).click()
        time.sleep(2)

        driver.find_element(*burgerLocators.BUTTON_PERSONAL_PAGE).click()
        time.sleep(2)

        driver.find_element(*burgerLocators.BUTTON_LOGOUT).click()
        time.sleep(2)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/h2').text == 'Вход'

