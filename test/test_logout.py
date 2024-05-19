from selenium import webdriver
import pytest
import time
from locators import BurgerLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestBurgerLogout:

    def test_logout(self, driver):
        
        driver.get('https://stellarburgers.nomoreparties.site/login')

        driver.find_element(*BurgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*BurgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*BurgerLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.BUTTON_PERSONAL_PAGE)))

        driver.find_element(*BurgerLocators.BUTTON_PERSONAL_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.BUTTON_LOGOUT)))

        driver.find_element(*BurgerLocators.BUTTON_LOGOUT).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.EMAIL_FIALD_LOGIN)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        assert driver.find_element(*BurgerLocators.BUTTON_LOGIN).text == 'Войти'

