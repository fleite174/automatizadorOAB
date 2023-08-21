from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
# entrar no site da - https://pje-consultapublica.tjdft.jus.br/
driver =  webdriver.Chrome()
driver.get('https://pje-consultapublica.tjdft.jus.br/')
sleep(30)
# digitar número oab e selecionar estado
# clicar em pesquisar
# entrar em cada um dos processos
# extrair o número do processo e data da distribuição
# extrair e guardar todas as ultimas movimentações
# guardar tudo no excel, separados por processo