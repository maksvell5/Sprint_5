from selenium import webdriver
import pytest
import time
import math
import random
from locators import BurgerLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class TestBurgerRegistrationTest:

    def test_lenght_password(self, driver):
        
        driver.get('https://stellarburgers.nomoreparties.site/register')
        email = driver.find_element(*BurgerLocators.EMAIL_FIALD).send_keys('eroninmax8000@yandex.ru')
        password = driver.find_element(*BurgerLocators.PASSWORD_FIALD).send_keys('12345')
        name = driver.find_element(*BurgerLocators.NAME_FIALD).send_keys('max')

        button_registration = driver.find_element(*BurgerLocators.BUTTON_REGISTRATION).click()

        assert driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/form/fieldset[3]/div/p').is_displayed()
        assert driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/form/fieldset[3]/div/p').text == 'Некорректный пароль'


    def test_name_fiald_empty(self, driver):
        
        driver.get('https://stellarburgers.nomoreparties.site/register')
        email = driver.find_element(*BurgerLocators.EMAIL_FIALD).send_keys('eroninmax8000@yandex.ru')
        password = driver.find_element(*BurgerLocators.PASSWORD_FIALD).send_keys('123456')

        button_registration = driver.find_element(*BurgerLocators.BUTTON_REGISTRATION).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'
        assert driver.find_element(*BurgerLocators.EMAIL_FIALD).get_attribute('value') == 'eroninmax8000@yandex.ru'
        assert driver.find_element(*BurgerLocators.PASSWORD_FIALD).get_attribute('value') == '123456'
        


    def test_no_valid_email(self, driver):
        
        driver.get('https://stellarburgers.nomoreparties.site/register')
        email = driver.find_element(*BurgerLocators.EMAIL_FIALD).send_keys('eroninmax')
        password = driver.find_element(*BurgerLocators.PASSWORD_FIALD).send_keys('123456')
        name = driver.find_element(*BurgerLocators.NAME_FIALD).send_keys('max')

        button_registration = driver.find_element(*BurgerLocators.BUTTON_REGISTRATION).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div/main/div/p')))

        assert driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/p').is_displayed()
        assert driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/p').text == 'Такой пользователь уже существует'

        








    def test_signup(self, driver):
        rand = math.ceil(random.uniform(0, 999))
      
        driver.get('https://stellarburgers.nomoreparties.site/register')
        email = driver.find_element(*BurgerLocators.EMAIL_FIALD).send_keys(f'eroninmax8{rand}@yandex.ru')
        password = driver.find_element(*BurgerLocators.PASSWORD_FIALD).send_keys('123456')
        name = driver.find_element(*BurgerLocators.NAME_FIALD).send_keys('max')

        button_registration = driver.find_element(*BurgerLocators.BUTTON_REGISTRATION).click()
        time.sleep(5)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'



