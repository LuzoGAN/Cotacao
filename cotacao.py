import requests
import json
 
cotações = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotações = cotações.json()

n = int(input('Informe a moeda que deseja ver a cotação: \n1 Para dolar\n2 para Euro\n3 para Bitcoin\n'))

if n == 1:
  
  cotação_nome = cotações['USDBRL']['name']
  cotação_dolar = cotações['USDBRL']['bid']
  cotação_data = cotações['USDBRL']['create_date']
  cotação_menorvalor = cotações['USDBRL']['low']
  cotação_maiorvalor = cotações['USDBRL']['high']
if n == 2:
  cotação_nome = cotações['EURBRL']['name']
  cotação_dolar = cotações['EURBRL']['bid']
  cotação_data = cotações['EURBRL']['create_date']
  cotação_menorvalor = cotações['EURBRL']['low']
  cotação_maiorvalor = cotações['EURBRL']['high']
if n == 3:
  cotação_nome = cotações['BTCBRL']['name']
  cotação_dolar = cotações['BTCBRL']['bid']
  cotação_data = cotações['BTCBRL']['create_date']
  cotação_menorvalor = cotações['BTCBRL']['low']
  cotação_maiorvalor = cotações['BTCBRL']['high']




print(f'O valor do {cotação_nome} está na data de {cotação_data} o valor de {cotação_dolar}, \n seu menor preço esteve em {cotação_menorvalor} e seu maior valor de {cotação_maiorvalor}')
