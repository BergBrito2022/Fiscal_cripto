#
import requests
import pandas as pd
from sqlalchemy import create_engine

price = requests.get('https://api.binance.com/api/v3/ticker/price') # Ativos e preços.
price_list = []

if price.status_code == 200:
   data = price.json()
   for i in data:
      price_list.append(        
         [
            i['symbol'], 
            i['price']
         ]
      )
else:
   erro = price.raise_for_status()
   print(f'Ocorreu o seguinte erro no acesso da API: {erro}')
   
for c in price_list:
   print(c)

   # Transformando price_list em um DataFrame (Tatando dados com pandas.)

df_price_list = pd.DataFrame(
   price_list, 
   columns=[
               'symbol', 
               'price'
           ]
    )
print(df_lista_precos)

# Preparando a conexão e gravando em uma tabela no banco de dados.

db_connection = 'mysql+pymysql://user:password@host:port/database'  
db_connection = create_engine(db_connection)
df_price_list.to_sql(con=db_connection, name='price_list_binanc', if_exists='replace', index=False)
