from selenium import webdriver
import pytest
import time
from locators import burgerLocators
from selenium.webdriver.common.by import By


class burgerLogin:

    def test_login_centr_page(self):
        driver=webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*burgerLocators.BUTTON_LOGIN_START_PAGE).click()
        time.sleep(2)

        driver.find_element(*burgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*burgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*burgerLocators.BUTTON_LOGIN).click()
        time.sleep(2)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').text == 'Оформить заказ'


    def test_login_personal_page(self):
        driver=webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*burgerLocators.BUTTON_PERSONAL_PAGE).click()
        time.sleep(2)

        driver.find_element(*burgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*burgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*burgerLocators.BUTTON_LOGIN).click()
        time.sleep(2)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').text == 'Оформить заказ'

    
    def test_login_registration_page(self):
        driver=webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()
        time.sleep(2)

        driver.find_element(*burgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*burgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*burgerLocators.BUTTON_LOGIN).click()
        time.sleep(2)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').text == 'Оформить заказ'


    def test_login_password_forget_page(self):
        driver=webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a').click()
        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()
        time.sleep(2)

        driver.find_element(*burgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*burgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*burgerLocators.BUTTON_LOGIN).click()
        time.sleep(2)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button').text == 'Оформить заказ'









