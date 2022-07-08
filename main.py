from sqlite3 import Error

from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sqlite3


# base.py
def conexion():
    try:
        conn = sqlite3.connect('database.db')
        return conn
    except Error:
        print("o rayos! :(")


def tabla_grupos(conn):
    '''
    crear tabla para los grupos de facebook
    :param conn: conexion a la base de datos
    :return: no return
    '''
    print("Creando base de datos para las ventas")
    cursor = conn.cursor()
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS [grupos] (
[prupoId] INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
[NombreGrupo] VARCHAR(50)  NULL,
[UrlGrupo] VARCHAR(50)  NULL,
[TipoGrupo] VARCHAR(50)  NULL,
[VolumenGrupo] VARCHAR(50)  NULL,
[ActividadGrupo] VARCHAR(50)  NULL,
[ActividadEstadistica] FLOAT  NULL
);
    """)
    conn.commit()


# consulta_grupo.py
def insertar_base_grupo(conn, grupo):
    '''
    Guarda un grupo a la base de datos
    :param conn: conexion a base de datos
    :param grupo: [prupoId,NombreGrupo,UrlGrupo,TipoGrupo,VolumenGrupo,ActividadGrupo,ActividadEstadistica]
    :return: no return
    '''


if __name__ == '__main__':
    # inicio()
    print("iniciando codigo")

    xpathMas = '//*[@id="mount_0_0_gB"]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[4]/span/div/a/span/svg'
    xpathGrupos = '//*[@id="mount_0_0_3W"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div[1]/ul/li[' \
                  '3]/div/a/div[2] '
    driver = webdriver.Chrome()
    driver.get('http://www.facebook.com')  # futura variable
    user = "gstncontacto@gmail.com"  # futura variable
    pwd = "Hm(Mb4c$4c27"  # futura variable
    botonGrupos = "//a[@role='link'][10]"
    elem = driver.find_element(By.ID, "email")
    elem.send_keys(user)
    driver.implicitly_wait(3)
    elem = driver.find_element(By.NAME, "pass")
    elem.send_keys(pwd)
    driver.find_element(By.XPATH, "//div/button").click()
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, "//a[@aria-label='Grupos']").click()
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, "//input[@aria-label='Buscar grupos']").send_keys('Compra Venta', Keys.ENTER)  #
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, "//input[@aria-label='Buscar grupos']").send_keys('Compra Venta', Keys.ESCAPE)  #
    # elem = driver.find_elements(By.XPATH, "//div[@role='listitem']/div[@data-visualcompletion='ignore-dynamic']/a")[1].click()

    # elem = driver.find_elements(By.XPATH, "//div[@role='listitem']/div/a[@role='link']")[1].click()
    driver.find_elements(By.XPATH, "//div[@role='listitem']/div/a[@role='link']")[1].click()

    # $x("//div[@role='listitem']/div/a[@role='link']")[1] boton grupos

    # elem = driver.find_elements(By.XPATH, "//div[@role='article']")[0]
    # $x("//div[@role='article'][1]//div[@class='qzhwtbm6 knvmm38d']//a")
    # elem1 = driver.find_element(By.XPATH, "//div[@role='article'][0]//div[@class='qzhwtbm6 knvmm38d'][0]//a").text
    elem1 = driver.find_element(By.XPATH,
                                "//div[@role='article'][1]/div/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/span/div/a").text
    print(elem1)

    elem2 = driver.find_element(By.XPATH,
                                "//div[@role='article'][1]/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/span/span").text
    print(elem2)

    cantidadElementos = len(driver.find_elements(By.XPATH, "//div[@role='article']"))
    print(cantidadElementos)

    for i in list(range(1, cantidadElementos + 1)):
        print(i)
        pathNombreGrupo = "//div[@role='article'][{}]/div/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/span/div/a".format(i)
        print(pathNombreGrupo)
        elem1 = driver.find_element(By.XPATH,pathNombreGrupo).text
        print(elem1)
        pathDetalleGrupo = "//div[@role='article'][{}]/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/span/span".format(i)
        print(elem2)

    #driver.quit()

    # $x("//div[@role='article'][1]//div[@class='qzhwtbm6 knvmm38d'][2]/span")
    # elem2 = driver.find_element(By.XPATH, "//div[@role='article'][0]//div[@class='qzhwtbm6 knvmm38d'][1]/span").text
    # elem1=elem.find_elements(By.XPATH,"//div[@role='article'][1]//div[@class='qzhwtbm6 knvmm38d'][1]")
    # elem2=elem.find_elements(By.XPATH,"//div[@class='qzhwtbm6 knvmm38d']")[2].text

    # print(elem2)

    # elem[1].click()
    # driver.implicitly_wait(5)
    #
    # elem=driver.find_elements(By.XPATH,"//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gpro0wi8 oo9gr5id lrazzd5p']")
    # try:
    #
    #     for i in elem:
    #         driver.implicitly_wait(5)
    #         elem1 = i.text
    #
    #         print(elem1)
    #
    # except:
    #     print('error')
    #
    # print('fin')
    # driver.quit()
