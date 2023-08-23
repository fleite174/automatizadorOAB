from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import openpyxl

numero_oab = 133864

# entrar no site da - https://pje-consulta-publica.tjmg.jus.br/
driver =  webdriver.Chrome()
driver.get('https://pje-consulta-publica.tjmg.jus.br/')
sleep(30)
# digitar número oab 
campo_oab = driver.find_element(By.XPATH,"//input[@id='fPP:Decoration:numeroOAB']")
campo_oab.send_keys(numero_oab)
# selecionar estado
dropdown_estados = driver.find_element(By.XPATH,"//select[@id='fPP:Decoration:estadoComboOAB']")
opcoes_estados = Select(dropdown_estados)
opcoes_estados.select_by_visible_text('SP')
# clicar em pesquisar
botao_pesquisar = driver.find_element(By.XPATH,"//input[@id='fPP:searchProcessos']")
botao_pesquisar.click()
sleep(10)
# entrar em cada um dos processos
link_processos = driver.find_elements(By.XPATH,"//b[@class='btn-block']")
for link_processo  in link_processos:
    link_processo.click()
    sleep(10)
    janelas = driver.window_handles
    driver.switch_to.window(janelas[-1])
    driver.set_window_size(1920, 1080)
# extrair o número do processo e data da distribuição
    numero_processo = driver.find_elements(By.XPATH,"//div[@class='col-sm-12 ']")
    numero_processo = numero_processo[0]
    numero_processo = numero_processo.text

    data_distribuicao = driver.find_elements(By.XPATH,"//div[@class='value col-sm-12 ']")
    data_distribuicao = data_distribuicao[1]
    data_distribuicao = data_distribuicao.text
# extrair e guardar todas as ultimas movimentações
movimentacoes = driver.find_elements(By.XPATH,"//div[@id='j_id132:processoEventoPanel_body']//tr[contains(@class,'rich-table-row ')]//td//div//div//span")
lista_movimentacoes = []
for movimentacao in movimentacoes:
    lista_movimentacoes.append(movimentacao.text)
# guardar tudo no excel, separados por processo
openpyxl.load_workbook('dados.xlsx')