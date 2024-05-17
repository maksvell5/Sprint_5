from selenium import webdriver
import pytest
import time
from locators import BurgerLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestBurgerLogin:

    def test_login_centr_page(self, driver):
        
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*BurgerLocators.BUTTON_LOGIN_START_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.EMAIL_FIALD_LOGIN)))

        driver.find_element(*BurgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*BurgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*BurgerLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.BUTTON_LOGIN_START_PAGE)))


        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert driver.find_element(*BurgerLocators.BUTTON_LOGIN_START_PAGE).text == 'Оформить заказ'


    def test_login_personal_page(self, driver):
        
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*BurgerLocators.BUTTON_PERSONAL_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.EMAIL_FIALD_LOGIN)))

        driver.find_element(*BurgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*BurgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*BurgerLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.BUTTON_LOGIN_START_PAGE)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert driver.find_element(*BurgerLocators.BUTTON_LOGIN_START_PAGE).text == 'Оформить заказ'

    
    def test_login_registration_page(self, driver):
        
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*BurgerLocators.LOGIN_REGISTRATION_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.EMAIL_FIALD_LOGIN)))

        driver.find_element(*BurgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*BurgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*BurgerLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.BUTTON_LOGIN_START_PAGE)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert driver.find_element(*BurgerLocators.BUTTON_LOGIN_START_PAGE).text == 'Оформить заказ'


    def test_login_password_forget_page(self, driver):
        
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*BurgerLocators.REFRESH_PASSWORD).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.LOGIN_REFRESH_PASSWORD)))

        driver.find_element(*BurgerLocators.LOGIN_REFRESH_PASSWORD).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.EMAIL_FIALD_LOGIN)))

        driver.find_element(*BurgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*BurgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*BurgerLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.BUTTON_LOGIN_START_PAGE)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert driver.find_element(*BurgerLocators.BUTTON_LOGIN_START_PAGE).text == 'Оформить заказ'









