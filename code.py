import requests
from tkinter import *

#pega a api e importa os dados atualizados de moeda
def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,GBP-BRL")
#arquivo json criado a partir da api com resultados
    requisicao_dic = requisicao.json()

#variaveis criadas para armazenar arquivo com resposta do json
    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']
    cotacao_do_gbp = requisicao_dic['GBPBRL']['bid']

#parte de resposta e é o que o usuário tem como resultado
    texto_resposta['text'] = f'''
    Dólar americano: {cotacao_dolar}
    Euro: {cotacao_euro}
    Bitcoin: {cotacao_btc}
    Libra Esterlina: {cotacao_do_gbp}'''

#configuração da janela de exibição TK
janela = Tk()
janela.title("Cotação Atual de Moedas")
janela.geometry('300x210')
texto = Label(janela, text="Clique no botão para ver cotação no momento")
texto.grid(column=0, row=0, padx=20, pady=20)

botao = Button(janela, text="Encontrar cotação atualizada", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=17, pady=17)

#criado para permanecer a janela do TK, deve ser sempre a última tag do código
janela.mainloop()