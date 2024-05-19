from selenium import webdriver
import pytest
import time
from locators import BurgerLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestpersonalPage:

    def test_login_personal_page(self, driver):
        
        driver.get('https://stellarburgers.nomoreparties.site/login')

        driver.find_element(*BurgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*BurgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*BurgerLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.BUTTON_PERSONAL_PAGE)))

        driver.find_element(*BurgerLocators.BUTTON_PERSONAL_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.BUTTON_LOGOUT)))

        assert driver.find_element(*BurgerLocators.PERSONAL_PAGE_LOGIN).get_attribute('value') == 'maax'
        assert driver.find_element(*BurgerLocators.PERSONAL_PAGE_EMAIL).get_attribute('value') == 'eroninmax8001@yandex.ru'
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_personal_page_click_constructor(self, driver):
        
        driver.get('https://stellarburgers.nomoreparties.site/login')

        driver.find_element(*BurgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*BurgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*BurgerLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.BUTTON_PERSONAL_PAGE)))

        driver.find_element(*BurgerLocators.BUTTON_PERSONAL_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.BUTTON_LOGOUT)))
        driver.find_element(*BurgerLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.BULKI)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert driver.find_element(*BurgerLocators.MAKE_BURGER).text == 'Соберите бургер'


    def test_personal_page_click_stellar_burger(self, driver):
        
        driver.get('https://stellarburgers.nomoreparties.site/login')

        driver.find_element(*BurgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*BurgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*BurgerLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.BUTTON_PERSONAL_PAGE)))

        driver.find_element(*BurgerLocators.BUTTON_PERSONAL_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.BUTTON_LOGOUT)))
        driver.find_element(*BurgerLocators.STELLAR_BURGER).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.BULKI)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        assert driver.find_element(*BurgerLocators.MAKE_BURGER).text == 'Соберите бургер'


        




    