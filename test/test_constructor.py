from selenium import webdriver
import pytest
import time
from locators import burgerLocators
from selenium.webdriver.common.by import By


class burgerConstructor:
    SELECT_CLASS = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
    NO_SELECT_CLASS = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'

    def test_constructor_check_bulki(self):
        driver=webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*burgerLocators.BUTTON_LOGIN_START_PAGE).click()
        time.sleep(2)

        driver.find_element(*burgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*burgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*burgerLocators.BUTTON_LOGIN).click()
        time.sleep(5)

        

        assert driver.find_element(*burgerLocators.BULKI).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        assert driver.find_element(*burgerLocators.SOUSE).get_attribute('class') == 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'
        assert driver.find_element(*burgerLocators.NACHINKA).get_attribute('class') == 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'


    def test_constructor_check_souse(self):
        driver=webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*burgerLocators.BUTTON_LOGIN_START_PAGE).click()
        time.sleep(2)

        driver.find_element(*burgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*burgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*burgerLocators.BUTTON_LOGIN).click()
        time.sleep(5)

        driver.find_element(*burgerLocators.SOUSE).click()
        time.sleep(2)

        assert driver.find_element(*burgerLocators.SOUSE).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        assert driver.find_element(*burgerLocators.BULKI).get_attribute('class') == 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'
        assert driver.find_element(*burgerLocators.NACHINKA).get_attribute('class') == 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'


    def test_constructor_check_nachinka(self):
        driver=webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*burgerLocators.BUTTON_LOGIN_START_PAGE).click()
        time.sleep(2)

        driver.find_element(*burgerLocators.EMAIL_FIALD_LOGIN).send_keys('eroninmax8001@yandex.ru')
        driver.find_element(*burgerLocators.PASSWORD_FIALD_LOGIN).send_keys('123456')
        driver.find_element(*burgerLocators.BUTTON_LOGIN).click()
        time.sleep(5)

        driver.find_element(*burgerLocators.NACHINKA).click()
        time.sleep(2)

        assert driver.find_element(*burgerLocators.NACHINKA).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        assert driver.find_element(*burgerLocators.BULKI).get_attribute('class') == 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'
        assert driver.find_element(*burgerLocators.SOUSE).get_attribute('class') == 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'

