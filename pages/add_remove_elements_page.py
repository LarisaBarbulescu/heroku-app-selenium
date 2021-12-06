from selenium.webdriver.common.by import By


class AddRemoveElementsPage:
    #locators
    TITLE_TEXT = (By.CSS_SELECTOR,'div h3')
    ADD_ELEMENT_BUTTON = (By.CSS_SELECTOR,'button[onclick="addElement()"]')
    DELETE_BUTTON = (By.CSS_SELECTOR,'button[onclick="deleteElement()"]')
    #GREEN_MESSAGE = (By.CLASS_NAME, 'flash success')
    #sau GREEN_MESSAGE = (By.CSS_SELECTOR, 'flash.success')

    #URL
    URL = 'https://the-internet.herokuapp.com/add_remove_elements/'

    def __init__(self, browser):
        self.browser = browser

    def loadPage(self): #deschide pagina
        self.browser.get(self.URL)

    def clickAddButton(self): #click pe butonul de ADD Element
        self.browser.find_element(*self.ADD_ELEMENT_BUTTON).click()

    def clickDeleteButton(self): #click pe butonul de Delete
        self.browser.find_element(*self.DELETE_BUTTON).click()

    def getTitlePage(self): #get si return pt a returna ceva
        return self.browser.find_element(*self.TITLE_TEXT).text

    def isDeleteButtonDisplayed(self): #is cand verificam ceva
        return self.browser.find_element(*self.DELETE_BUTTON).is_displayed()

    def getNumberOfDeleteButton(self):
        return len(self.browser.find_elements(*self.DELETE_BUTTON))



#get - returneaza un text
#is - returneaza true/false
#len - returneaza lungimea listei -adica nr de butoane delete care sunt pe pagina

    