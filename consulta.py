import requests
import json
import pandas
import decimal

url = "http://data.fixer.io/api/latest?access_key=96ab84f4d5e05524e6dbdae8df58bdd6"

resposta = requests.get(url)
print(resposta)
if resposta.status_code == 200:   
    print("Acesso realizado com sucesso")
    print("Buscando Informações")
    dados = resposta.json()
    dolar_real = round(dados['rates']['BRL']/dados['rates']['USD'], 2)
    euro_real = round(dados['rates']['BRL']/dados['rates']['EUR'], 2)
    bitcoin_real = round(dados['rates']['BRL']/dados['rates']['BTC'], 2)

    print ('1 Dolar vale:', dolar_real, 'reais')
    print ("1 Euro vale:", euro_real, 'reais')
    print ("1 Bitcoin vale:", bitcoin_real, 'reais')
    print("Exportando resultados em tabela excell...")
    tela = pandas.DataFrame({'moedas':['Dolar', 'Euro', 'Bitcoin'], 'valores':[dolar_real, euro_real, bitcoin_real]})
    tela.to_csv('valores.csv', index=False, sep=";", decimal=",")
    print("Arquivo exportado com sucesso")
else:
    print("Erro na base de dados")
