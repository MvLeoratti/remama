import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://books.toscrape.com/index.html"
driver.get(url)
time.sleep(5)

links = driver.find_elements(By.TAG_NAME, "a")
print(links)
print(len(links))

# Os livros comecao no 54 e terminam no 94 de 2 em 2
x = driver.find_elements(By.TAG_NAME, "a")[54].text
print(x)

y = driver.find_elements(By.TAG_NAME, "a")[54].get_attribute("title")
print(y)

print(driver.find_elements(By.TAG_NAME,"a")[54:94:2])

elementostitulos =driver.find_elements(By.TAG_NAME, "a")[54:94:2]

lista_titulo = [title.get_attribute("title") for title in elementostitulos]
print(lista_titulo)

elementostitulos[1].click()
time.sleep(1)

stok = driver.find_element(By.CLASS_NAME, "instock").text

print(stok)

time.sleep(1)
estoque = int(stok.replace("In stock (","").replace(" available)",""))
print(estoque)

driver.back()

listaStok = []

for titulo in elementostitulos:
    titulo.click()
    time.sleep(1)
    qtd =int(driver.find_element(By.CLASS_NAME, "instock").text.replace("In stock (","").replace(" available)",""))
    listaStok.append(qtd)
    driver.back()
    time.sleep(1)
print(listaStok)

data = {"Titulo" : lista_titulo, estoque:listaStok}
print()

dados = pd.DataFrame(data)

dados.to_excel("Dados.xlsx")