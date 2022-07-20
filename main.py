import time
import database
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys


def buscar(correo, password, filter, busqueda, cantidadDeRegistros):
    print('usuario: ' + correo)
    print('password: ' + password)
    print('filter: ' + filter)
    print('busqueda: ' + busqueda)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://www.facebook.com')  # futura variable

    wait = WebDriverWait(driver, 30)
    # elem = WebDriverWait(driver,100).until(EC.presence_of_element_located(By.ID, "email"))
    # elem = driver.find_element(By.ID, "email")
    # elem = WebDriverWait(driver,100).until(EC.element_to_be_clickable(By.ID,'email'))

    # Ingreso al correo
    correo1 = wait.until(EC.presence_of_element_located((By.ID, 'email')))
    correo1.send_keys(correo)
    contra = wait.until(EC.presence_of_element_located((By.ID, 'pass')))
    contra.send_keys(password)
    driver.find_element(By.XPATH, "//div/button").click()

    # elem = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Grupos']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Grupos']"))).click()
    # driver.find_element(By.XPATH, "//a[@aria-label='Grupos']").click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Buscar grupos']"))).send_keys(busqueda,
                                                                                                             Keys.ENTER)
    # driver.find_element(By.XPATH, "//input[@aria-label='Buscar grupos']").send_keys(busqueda, Keys.ENTER)  #

    # ======================================================================== #

    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Buscar grupos']"))).send_keys(busqueda,
                                                                                                             Keys.ESCAPE)
    # driver.find_element(By.XPATH, "//input[@aria-label='Buscar grupos']").send_keys(busqueda, Keys.ESCAPE)  #
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='listitem']/div/a[@role='link']")))

    if filter == 'todo':
        index = 0

    elif filter == 'grupos':
        index = 1

    elif filter == 'publicaciones de grupos':
        index = 2

    # print("index: " + str(index))
    # wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='listitem']/div/a[@role='link']")[index])).click()
    # botones=wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='listitem']/div/a[@role='link'][1]"))).click()

    # boton = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='listitem']/div/a[@role='link']"))[index])
    # boton.click()
    button = driver.find_elements(By.XPATH, "//div[@role='listitem']/div/a[@role='link']")[index]
    button.click()

    for i in range(0, cantidadDeRegistros):
        # ListaDeArticulos = driver.find_elements(By.XPATH, "//div[@role='article']")

        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='article']")))
        ListaDeArticulos = driver.find_elements(By.XPATH, "//div[@role='article']")

        for i in ListaDeArticulos:
            print('guardo el articulo')
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        print('fin')

    driver.quit()


if __name__ == '__main__':
    print('inicio')
    buscar('gstncontacto@gmail.com', 'Hm(Mb4c$4c27', 'grupos', 'pepe', 2000)



# """
# <span   class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w
#                 c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q
#                 a3bd9o3v b1v8xokw m9osqain oqcyycmt" dir="auto">
# 	Fin de los resultados
# </span>
# Fin de los resultados
#
# https://python.hotexamples.com/es/examples/selenium.webdriver.support.wait/WebDriverWait/send_keys/python-webdriverwait-send_keys-method-examples.html


# https://selenium-python.readthedocs.io/getting-started.html

# https://selenium-python.readthedocs.io/waits.html
# Fin de los resultados"""