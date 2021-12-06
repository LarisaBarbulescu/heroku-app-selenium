#pipenv run python -m pytest

from selenium import webdriver
#se fac gri pana le folosim
from selenium.webdriver.common.by import By
from pages.add_remove_elements_page import AddRemoveElementsPage
#din pachet pages, folder add_remove_elements_page importa clasa AddRemoveElementsPage
import time


def test_add_elements(browser):
    browser.get('https://the-internet.herokuapp.com/add_remove_elements/')
    '''title = browser.find_element(By.CSS_SELECTOR,'div h3')
    assert title.text == "Add/Remove Elements", "Title is not correct"
    print('test add element')'''

def test_add_element(browser): #legat cu inceputul din fisier conftest denumit in interior browser
    add_page = AddRemoveElementsPage(browser)
    add_page.loadPage()
    #browser.get('https://the-internet.herokuapp.com/add_remove_elements/')
    #punem browser in loc de driver peste tot
    # click add element
    add_page.clickAddButton()
    #check delete button is displayed
    add_page.clickDeleteButton()


    '''delete_button = browser.find_element(By.CSS_SELECTOR,'button[onclick="deleteElement()"]')
    assert delete_button.is_displayed() is True, "Delete button is not displayed"
    delete_button.click()
    list = browser.find_elements(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')
    assert len(list) == 0, 'Delete button is displayed'

pt a inchide browser-ul, cu prea multe deschise moare laptopul, close se foloseste pt tab, quit inchide tot'''

