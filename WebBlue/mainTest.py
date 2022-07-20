# from sqlite3 import Error
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def guardar_elemento(indice):
    pathNombreGrupo = "//div[@role='article'][{}]/div/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/span/div/a".format(
        indice)
    elem1 = driver.find_element(By.XPATH, pathNombreGrupo).text
    pathDetalleGrupo = "//div[@role='article'][{}]/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/span/span".format(
        indice)
    elem2 = driver.find_element(By.XPATH, pathDetalleGrupo).text
    print("Guardado:\n{}\n{}".format(elem1, elem2))
def guardar_grupos1():
    indice = 1
    # cantidad = len(driver.find_elements(By.XPATH, "//div[@role='article']"))

    while indice <= len(driver.find_elements(By.XPATH, "//div[@role='article']")):

        print('----------------------')
        print(str(indice))
        print('----------------------')
        guardar_elemento2(indice)
        indice += 1
    else:
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    driver.quit()
def guardar_elemento2(indice):
    pathNombreGrupo = "//div[@role='article'][{}]/div/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/span/div/a".format(indice)
    elem1 = driver.find_element(By.XPATH, pathNombreGrupo).text
    pathDetalleGrupo = "//div[@role='article'][{}]/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/span/span".format(indice)
    elem2 = driver.find_element(By.XPATH, pathDetalleGrupo).text
    print("Guardado:\n{}\n{}".format(elem1, elem2))
    print('indice' + str(indice))

def guardar_elemento3(indice,pathNombreGrupo,pathDetalleGrupo):
    elem1 = driver.find_element(By.XPATH, pathNombreGrupo).text
    elem2 = driver.find_element(By.XPATH, pathDetalleGrupo).text
    print("Guardado:\n{}\n{}".format(elem1, elem2))
    print('indice' + str(indice))


def webScraper(indice):
    articulo = driver.find_elements(By.XPATH, "//div[@role='article']")
    try:
        guardar_elemento(0)
    except:
        try:
            guardar_elemento(1)
            while articulo[indice]:
                guardar_elemento(indice)
                indice += 1
        except:
            driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
            try:
                webScraper(indice)
            except:
                print("fin")

if __name__ == '__main__':
    xpathMas = '//*[@id="mount_0_0_gB"]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[4]/span/div/a/span/svg'
    xpathGrupos = '//*[@id="mount_0_0_3W"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div[1]/ul/li[' \
                  '3]/div/a/div[2] '
    pathNombreGrupo = "//div[@role='article'][{}]/div/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/span/div/a".format(
        indice)
    pathDetalleGrupo = "//div[@role='article'][{}]/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/span/span".format(
        indice)
    driver = webdriver.Chrome()
    driver.get('http://www.facebook.com')  # futura variable
    user = "gstncontacto@gmail.com"  # futura variable
    pwd = "Hm(Mb4c$4c27"  # futura variable
    botonGrupos = "//a[@role='link'][10]"
    busqueda1 = 'Compra Venta'
    busqueda2 = 'vfbawdawddawgnz'
    busqueda3 = 'zxzxzzxzxzx'
    indice=1

    busqueda = busqueda2
    elem = driver.find_element(By.ID, "email")
    elem.send_keys(user)
    driver.implicitly_wait(3)
    elem = driver.find_element(By.NAME, "pass")
    elem.send_keys(pwd)
    driver.find_element(By.XPATH, "//div/button").click()
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, "//a[@aria-label='Grupos']").click()
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, "//input[@aria-label='Buscar grupos']").send_keys(busqueda, Keys.ENTER)  #
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, "//input[@aria-label='Buscar grupos']").send_keys(busqueda, Keys.ESCAPE)  #
    driver.find_elements(By.XPATH, "//div[@role='listitem']/div/a[@role='link']")[1].click()

    #
    #
    #
    # indice = 1
    # # cantidad = len(driver.find_elements(By.XPATH, "//div[@role='article']"))
    #
    #
    # while indice <= len(driver.find_elements(By.XPATH, "//div[@role='article']")):
    #
    #     print('----------------------')
    #     print(str(indice))
    #     print('----------------------')
    #     guardar_elemento2(indice)
    #     indice += 1
    # else:
    #     driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    # driver.quit()
    guardar_elemento3(indice,pathNombreGrupo,pathDetalleGrupo)
