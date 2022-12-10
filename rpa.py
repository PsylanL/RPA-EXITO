from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver= webdriver.Chrome(executable_path="driver/chromedriver.exe")
driver.maximize_window()
time.sleep(1)
driver.get("https://www.viajesexito.com/")
viajes=driver.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[2]/a')
viajes.click()

ciudad_destino=driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div/div/input').send_keys("Punta Cana, Republica Dominicana (PUJ)")

#ciudad_destino_txt="Punta Cana, Republica Dominicana (PUJ)"
time.sleep(2)

ida=driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]')
ida.click()
time.sleep(2)

ida2=driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/table/tbody/tr[3]/td[3]/a')
ida2.click()
time.sleep(2)

ida3=driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/table/tbody/tr[4]/td[4]/a')
ida3.click()
time.sleep(2)

habitacion=driver.find_element(By.XPATH, '//*[@id="txtNumPassengersPaquetesComplete"]')
habitacion.click()
time.sleep(2)
habitacion2=driver.find_element(By.XPATH,   '//*[@id="roomonepaquetes"]/div/div[3]/div/span[2]/button/span')
habitacion2.click()
time.sleep(2)
aplicar_habitacion=driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/button')
aplicar_habitacion.click()
time.sleep(5)

buscar=driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[4]/a')
buscar.click()
time.sleep(15)

precio1=driver.find_element(By.XPATH,  '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio2=driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[2]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio3=driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[3]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio4=driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[4]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio5=driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[5]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio6=driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[6]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio7=driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[7]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio8=driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[8]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio9=driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[9]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio10=driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[10]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text

print("-------PRECIOS DE VUELO SEGUN BUSQUEDA-------")
print("Esta es tu mejor opcion:")
print(precio1)
print("---------------------------------------------")
print(precio2)
print("---------------------------------------------")
print(precio3)
print("---------------------------------------------")
print(precio4)
print("---------------------------------------------")
print(precio5)
print("---------------------------------------------")
print(precio6)
print("---------------------------------------------")
print(precio7)
print("---------------------------------------------")
print(precio8)
print("---------------------------------------------")
print(precio9)
print("---------------------------------------------")
print(precio10)
print("---------------------------------------------")


avanzadas=driver.find_element(By.XPATH, '//*[@id="txtAirlineCode"]').send_keys("Copa Airlines (CM)")
time.sleep(2)
avanzadas_buscar=driver.find_element(By.XPATH, '//*[@id="ulNewSearch"]/div[8]/input')
avanzadas_buscar.click()

time.sleep(20)
driver.quit()

