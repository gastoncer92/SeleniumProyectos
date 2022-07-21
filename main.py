import time
import database
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from text import *
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys


def buscar(correo, password, filter, busqueda, cantidadDeRegistros):
    print('usuario: ' + correo)
    print('password: ' + "********")
    print('filter: ' + filter)
    print('busqueda: ' + busqueda)

    driver = webdriver.Chrome()
    # driver.maximize_window()
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
        # Buscador: $x('//a[@role="presentation"]')
        wait.until(EC.presence_of_element_located((By.XPATH, '//a[@role="presentation"]')))
        ListaDeTitulos = driver.find_elements(By.XPATH, '//a[@role="presentation"]')

        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='article']")))
        ListaDeArticulos = driver.find_elements(By.XPATH, "//div[@role='article']")

        # def good_list():
        #     my_list = [value for value in range(elements)]
        #
        #
        # def bad_list():
        #     my_list = []
        #     for value in range(elements):
        #         my_list.append(value)
        print('inicio codigo')
        # lista = []
        try:

            for i in ListaDeTitulos:
                print('====Titulos====')
                print(i.text)
                # print(i.get_property('innerText'))
                # print(i.find_elements(By.XPATH, '//a[@role="presentation"]').get_property('innerText'))
                # print(i.find_elements(By.XPATH, '//a[@role="presentation"]'))
                # print(i.find_elements(By.XPATH, '//a[@role="presentation"]'))
                # innerText: "Pepe🥺🐥🥺🐥\nGrupo público · 10 mil miembros · 20 publicaciones a la semana\nUnirte"

                #buscando solo titulos $x('//div[@role="article"]//div[@class="qzhwtbm6 knvmm38d"][1]')
                #buscando solo contenidos $x('//div[@role="article"]//div[@class="qzhwtbm6 knvmm38d"][1]')

        except:
            print_error()
            driver.quit()
        # lista=[]

        # for i in range(len(ListaDeArticulos)):
        #     lista.append(i)
        # print(lista)
        # print('fin codigo')
        # for i in ListaDeArticulos:
        #     lista.append(i.get_attribute(inner_text))

        # codigos = [element.text for element in ListaDeArticulos]
        # print(codigos)
        # <selenium.webdriver.remote.webelement.WebElement (session="79a0abc6d9a8d97dbe74406937e69dbc", element="43e4f27b-d522-43d9-926c-1a62e47f84fc")>

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        print('fin')

    driver.quit()


if __name__ == '__main__':
    print('inicio')
    buscar('gstncontacto@gmail.com', 'Hm(Mb4c$4c27', 'grupos', 'pepe', 1)

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
