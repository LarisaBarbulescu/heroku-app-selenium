from selenium.webdriver.common.by import By

class LoginPage:
    #locators
    USERNAME_FIELD =(By.ID, 'username')
    PASSWORD_FIELD =(By.ID, 'password')
    #LOGIN_BUTTON =(By.CLASS_NAME, 'fa fa-2x fa-sign-in')
    #BUTTON = (By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR,'button[class="radius"]')
    INVALID_MSG_TEXT = (By.CLASS_NAME,'flash error')

    # URL
    URL = 'https://the-internet.herokuapp.com/login'

    def __init__(self, browser):
        self.browser = browser

    def loadPage(self): #deschide pagina
        self.browser.get(self.URL)

    def insertUsernameField(self): #click pe butonul de ADD Element
        self.browser.find_element(*self.USERNAME_FIELD).send_keys('tomsmith')
        '''elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)'''

    def insertPasswordField(self):
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys('SuperSecretPassword!')

    def clickLoginButton(self):
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def getInvalidloginMsg(self):
        return self.browser.find_element(*self.INVALID_MSG_TEXT).text
