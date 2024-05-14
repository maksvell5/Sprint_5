from selenium import webdriver
import pytest
import time
from locators import burgerLocators
from selenium.webdriver.common.by import By



class burgerRegistrationTest:

    def test_lenght_password(self):
        driver=webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register')
        email = driver.find_element(*burgerLocators.EMAIL_FIALD).send_keys('eroninmax8000@yandex.ru')
        password = driver.find_element(*burgerLocators.PASSWORD_FIALD).send_keys('12345')
        name = driver.find_element(*burgerLocators.NAME_FIALD).send_keys('max')

        button_registration = driver.find_element(*burgerLocators.BUTTON_REGISTRATION).click()

        assert driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/form/fieldset[3]/div/p').is_displayed()
        assert driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/form/fieldset[3]/div/p').text == 'Некорректный пароль'


    def test_name_fiald_empty(self):
        driver=webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register')
        email = driver.find_element(*burgerLocators.EMAIL_FIALD).send_keys('eroninmax8000@yandex.ru')
        password = driver.find_element(*burgerLocators.PASSWORD_FIALD).send_keys('123456')

        button_registration = driver.find_element(*burgerLocators.BUTTON_REGISTRATION).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'
        assert driver.find_element(*burgerLocators.EMAIL_FIALD).get_attribute('value') == 'eroninmax8000@yandex.ru'
        assert driver.find_element(*burgerLocators.PASSWORD_FIALD).get_attribute('value') == '123456'
        


    def test_no_valid_email(self):
        driver=webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register')
        email = driver.find_element(*burgerLocators.EMAIL_FIALD).send_keys('eroninmax')
        password = driver.find_element(*burgerLocators.PASSWORD_FIALD).send_keys('123456')
        name = driver.find_element(*burgerLocators.NAME_FIALD).send_keys('max')

        button_registration = driver.find_element(*burgerLocators.BUTTON_REGISTRATION).click()

        time.sleep(2)

        assert driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/p').is_displayed()
        assert driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/p').text == 'Такой пользователь уже существует'

        








    def test_signup(self):
        driver=webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register')
        email = driver.find_element(*burgerLocators.EMAIL_FIALD).send_keys('eroninmax8004@yandex.ru')
        password = driver.find_element(*burgerLocators.PASSWORD_FIALD).send_keys('123456')
        name = driver.find_element(*burgerLocators.NAME_FIALD).send_keys('max')

        button_registration = driver.find_element(*burgerLocators.BUTTON_REGISTRATION).click()
        time.sleep(5)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'



