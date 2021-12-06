import pytest
import selenium.webdriver

@pytest.fixture #face legatura intre teste
def browser():
    #initializam instanta de Chromedriver, se deschide tab-ul de chrome
    driver = selenium.webdriver.Chrome('C:/Users/Larisa/Selenium/chromedriver.exe')
    driver.implicitly_wait(10) #asteapta maxim 10 sec, dar daca face actiunea mai repede, se inchide mai repede
    yield driver #executa liniile din fata inaintea testelor(inainte de deschidere tab)
    driver.quit()