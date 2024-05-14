from selenium.webdriver.common.by import By

class burgerLocators:
    EMAIL_FIALD=(By.XPATH,'//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    PASSWORD_FIALD=(By.XPATH,'//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')
    NAME_FIALD=(By.XPATH,'//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    BUTTON_REGISTRATION = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    BUTTON_LOGIN_START_PAGE = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
    EMAIL_FIALD_LOGIN = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    PASSWORD_FIALD_LOGIN = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    BUTTON_LOGIN = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    BUTTON_PERSONAL_PAGE = (By.XPATH, '//*[@id="root"]/div/header/nav/a')
    BUTTON_LOGOUT = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')
    BULKI = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]')
    SOUSE = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]')
    NACHINKA = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]')

