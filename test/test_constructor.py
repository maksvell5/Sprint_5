from selenium import webdriver
import pytest
import time
from locators import BurgerLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestBurgerConstructor:

    def test_constructor_check_bulki(self, driver):
        
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*BurgerLocators.BUTTON_LOGIN_START_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.EMAIL_FIALD_LOGIN)))

        driver.find_element(*BurgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*BurgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*BurgerLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.BULKI)))

        

        assert driver.find_element(*BurgerLocators.BULKI).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        assert driver.find_element(*BurgerLocators.SOUSE).get_attribute('class') == 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'
        assert driver.find_element(*BurgerLocators.NACHINKA).get_attribute('class') == 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'


    def test_constructor_check_souse(self, driver):
        
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*BurgerLocators.BUTTON_LOGIN_START_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.EMAIL_FIALD_LOGIN)))

        driver.find_element(*BurgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*BurgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*BurgerLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.SOUSE)))

        driver.find_element(*BurgerLocators.SOUSE).click()
        

        assert driver.find_element(*BurgerLocators.SOUSE).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        assert driver.find_element(*BurgerLocators.BULKI).get_attribute('class') == 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'
        assert driver.find_element(*BurgerLocators.NACHINKA).get_attribute('class') == 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'


    def test_constructor_check_nachinka(self, driver):
        
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*BurgerLocators.BUTTON_LOGIN_START_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.EMAIL_FIALD_LOGIN)))

        driver.find_element(*BurgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*BurgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*BurgerLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((BurgerLocators.NACHINKA)))

        driver.find_element(*BurgerLocators.NACHINKA).click()
        

        assert driver.find_element(*BurgerLocators.NACHINKA).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        assert driver.find_element(*BurgerLocators.BULKI).get_attribute('class') == 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'
        assert driver.find_element(*BurgerLocators.SOUSE).get_attribute('class') == 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'

