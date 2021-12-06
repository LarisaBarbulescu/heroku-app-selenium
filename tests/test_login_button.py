#pipenv run python -m pytest
import time
from time import sleep
from selenium.webdriver.common.by import By
from pages.login_button_page import LoginPage
from tests.conftest import browser

'''Scenarii

1. User:tomsmith, pass: SuperSecretPassword!, login success
2. User:ana, Pass:para, click Login, fail login
3. 
4. 
5
6'''

'''1. User:tomsmith, pass: SuperSecretPassword!, login success'''

def test_login_button_succes(browser):
    login = LoginPage(browser)
    login.loadPage() #incarca pag
    login.insertUsernameField() #completeaza user
    time.sleep(3)
    login.insertPasswordField() #completeaza parola
    time.sleep(3)
    login.clickLoginButton() #click pe buton login

'''2. User:ana, Pass:para, click Login, fail login'''
'''
def test_login_button_fail(browser):
    login = LoginPage(browser)
    login.loadPage() #incarca pag
    login.insertUsernameField() #completeaza user
    time.sleep(3)
    login.insertPasswordField() #completeaza parola
    time.sleep(3)
    login.clickLoginButton() #click pe buton login
    time.sleep(3)
    assert login.getInvalidloginMsg() == "Your username is invalid!"
    '''




