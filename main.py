from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import openpyxl 

def pegar_cnpj():
    sleep(1)
    Nome_empresa = navegador.find_element('xpath', '/html/body/div/table/tbody/tr[6]/td').text
    Endereco_empresa = navegador.find_element('xpath', '/html/body/div/table/tbody/tr[21]/td[1]')
    ComplementoEndereco_empresa = navegador.find_element('xpath', '/html/body/div/table/tbody/tr[21]/td[2]')
    cep_empresa = navegador.find_element('xpath', '/html/body/div/table/tbody/tr[23]/td[1]')
    Bairro_empresa = navegador.find_element('xpath', '/html/body/div/table/tbody/tr[23]/td[2]')
    Estado_empresa = navegador.find_element('xpath', '/html/body/div/table/tbody/tr[23]/td[3]')

    #testar
    print(Nome_empresa)
    print(Estado_empresa)
    print(ComplementoEndereco_empresa)
    print(Bairro_empresa)
    print(cep_empresa)
    print(Endereco_empresa)

#Configurar Chrome

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

#Pegar CNPJ
CNPJ = int(input('DIGITE O CNPJ'))

#Abrir site
navegador.get(f'https://consultacnpj.info/')

#colocar cnpj
sleep(3)
navegador.find_element('xpath', '//*[@id="cnpj"]').send_keys(CNPJ)

navegador.find_element('xpath', '//*[@id="bto"]').click()

input('aperte enter quando realizar o teste')
pegar_cnpj()
#pegar informacoes

