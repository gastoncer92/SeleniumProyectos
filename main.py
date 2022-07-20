import time
import database
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def buscar(usuario, password, filter, busqueda, cantidadDeRegistros):
    print('usuario: ' + usuario)
    print('password: ' + password)
    print('filter: ' + filter)
    print('busqueda: ' + busqueda)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://www.facebook.com')  # futura variable
    elem = driver.find_element(By.ID, "email")
    elem.send_keys(usuario)
    elem = driver.find_element(By.NAME, "pass")
    elem.send_keys(password)
    driver.find_element(By.XPATH, "//div/button").click()
    driver.find_element(By.XPATH, "//a[@aria-label='Grupos']").click()
    driver.find_element(By.XPATH, "//input[@aria-label='Buscar grupos']").send_keys(busqueda, Keys.ENTER)  #
    driver.find_element(By.XPATH, "//input[@aria-label='Buscar grupos']").send_keys(busqueda, Keys.ESCAPE)  #

    if filter == 'todo':
        index = 0
    elif filter == 'grupos':
        index = 1
    elif filter == 'publicaciones de grupos':
        index = 2
    print("index: " + str(index))

    driver.find_elements(By.XPATH, "//div[@role='listitem']/div/a[@role='link']")[index].click()

    for i in range(0, cantidadDeRegistros):
        ListaDeArticulos = driver.find_elements(By.XPATH, "//div[@role='article']")
        for i in ListaDeArticulos:
            print('guardo el articulo')
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


if __name__ == '__main__':
    print('inicio')
    buscar('gstncontacto@gmail.com', 'Hm(Mb4c$4c27', 'grupos', 'pepe', 200)
