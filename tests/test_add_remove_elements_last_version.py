#pipenv run python -m pytest

from time import sleep
from selenium.webdriver.common.by import By
from pages.add_remove_elements_page import AddRemoveElementsPage
from tests.conftest import browser

'''Scenarii

1. verifica ca titlul din pagina este corect
2. butonul de AddElement este functional -> apare Delete button
3. butonul de delete dispare cand dam click pe el
4. 10 ori click -> 10 butoane de delete'''

#1. verifica ca titlul din pagina este corect
#click title page is correct Add/Remove Elements
def test_page_title_is_corect(browser):
    add_remove_page = AddRemoveElementsPage(browser)
#load the page - deschide pagina
    add_remove_page.loadPage()
#check title is correct
    assert add_remove_page.getTitlePage() == "Add/Remove Elements", 'Page title is not correct'
#assert verifica ceva mereu

#2. butonul de AddElement este functional -> apare Delete button
def test_add_element_button(browser):
    add_remove_page = AddRemoveElementsPage(browser)
#load the page - deschide pagina
    add_remove_page.loadPage()
#click add
    add_remove_page.clickAddButton()
#check delete button is displayed
    assert add_remove_page.isDeleteButtonDisplayed(), 'Delete button is not displayed'

#3. butonul de delete dispare cand dam click pe el
def test_delete_button(browser):
    add_remove_page = AddRemoveElementsPage(browser)
# load the page - deschide pagina
    add_remove_page.loadPage()
# click add
    add_remove_page.clickAddButton()
# click delete button
    add_remove_page.clickDeleteButton()
#check delete button is not displayed
    assert add_remove_page.getNumberOfDeleteButton() == 0, 'Button is dispayed on page'

#4. 10 ori click -> 10 butoane de delete
def test_buttonX10(browser):
    add_remove_page = AddRemoveElementsPage(browser)
# load the page - deschide pagina
    add_remove_page.loadPage()
#click add button
    for i in range(10):
        add_remove_page.clickAddButton()
    assert add_remove_page.getNumberOfDeleteButton() == 10, 'There are less or more then 10'

