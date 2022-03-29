#
import requests
import pandas as pd
from sqlalchemy import create_engine


price = requests.get('https://api.binance.com/api/v3/ticker/price') # Ativos e preços.
lista_precos = []


if price.status_code == 200:
   data = price.json()
   for i in data:
      lista_precos.append([i['symbol'], i['price']])
else:
   erro = price.raise_for_status()
   print(f'Ocorreu o seguinte erro no acesso da API: {erro}')

# Transformando a lista de endereços em um DataFrame

df_lista_precos = pd.DataFrame(lista_precos, columns=['symbol', 'price'])  #Tratando Dados com pandas.
print(df_lista_precos)


for c in lista_precos:
   print(c)

# Preparando a conexão e gravando em uma tabela no banco de dados.

db_connection = 'mysql+pymysql://user:password@host:port/database'  
db_connection = create_engine(db_connection)
df_lista_precos.to_sql(con=db_connection, name='enderecos', if_exists='replace', index=False)