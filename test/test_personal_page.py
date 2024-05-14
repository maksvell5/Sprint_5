from selenium import webdriver
import pytest
import time
from locators import burgerLocators
from selenium.webdriver.common.by import By


class personalPage:

    def test_login_personal_page(self):
        driver=webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login')

        driver.find_element(*burgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*burgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*burgerLocators.BUTTON_LOGIN).click()
        time.sleep(2)

        driver.find_element(*burgerLocators.BUTTON_PERSONAL_PAGE).click()
        time.sleep(2)

        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul/li[1]/div/div/input').get_attribute('value') == 'maax'
        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul/li[2]/div/div/input').get_attribute('value') == 'eroninmax8001@yandex.ru'
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_personal_page_click_constructor(self):
        driver=webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login')

        driver.find_element(*burgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*burgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*burgerLocators.BUTTON_LOGIN).click()
        time.sleep(2)

        driver.find_element(*burgerLocators.BUTTON_PERSONAL_PAGE).click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a').click()
        time.sleep(2)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1').text == 'Соберите бургер'


    def test_personal_page_click_stellar_burger(self):
        driver=webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login')

        driver.find_element(*burgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*burgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*burgerLocators.BUTTON_LOGIN).click()
        time.sleep(2)

        driver.find_element(*burgerLocators.BUTTON_PERSONAL_PAGE).click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/div/a').click()
        time.sleep(2)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1').text == 'Соберите бургер'


        




    