#pipenv run python -m pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_add_element():
    driver = webdriver.Chrome('C:/Users/Larisa/Selenium/chromedriver.exe')
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    title = driver.find_element(By.CSS_SELECTOR,'div h3')
    assert title.text == "Add/Remove Elements", "Title is not correct"
    driver.quit()
    print('test add element')

def test_add_element():
    driver = webdriver.Chrome('C:/Users/Larisa/Selenium/chromedriver.exe')
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    # click add element
    add_button = driver.find_element(By.CSS_SELECTOR,'button[onclick="addElement()"]')
    add_button.click()
    time.sleep(4)
    #check delete button is displayed
    delete_button = driver.find_element(By.CSS_SELECTOR,'button[onclick="deleteElement()"]')
    assert delete_button.is_displayed() is True, "Delete button is not displayed"
    delete_button.click()
    time.sleep(6)
    list = driver.find_elements(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')
    assert len(list) == 0, 'Delete button is displayed'
    driver.quit()

#pt a inchide browser-ul, cu prea multe deschise moare laptopul, close se foloseste pt tab, quit inchide tot

