import pandas as pd
import numpy as np

df_store = pd.read_csv('./store.csv', delimiter=';', encoding="ISO-8859-1",
                       usecols=['Order_ID', 'Order_Date', 'Ship Date', 'Ship Mode', 'Customer ID', 'Customer Name',
                                'City', 'Product ID', 'Category', 'Product_Name', 'Sales', 'Quantity'])
print(df_store.head())

# Setear el tipado de la columna Sales a enter
df_store.Sales = df_store.apply(lambda row: int(row['Sales'].replace(',', '')), axis=1)

# Traer nombre clientes, cantidad, que tengan mas de 4  unidades
print("# Setear el tipado de la columna Sales a enter")
print(df_store.loc[df_store.Quantity > 4, ['Customer Name', 'Quantity']])

# Traer nombre id y nombre clientes, cantidad, venta que tengan mas de 2  unidades y la venta sea mayor o igual a 50 USD
print(
    "# Traer nombre id y nombre clientes, cantidad, venta que tengan mas de 2  unidades y la venta sea mayor o igual a 50 USD")
print(df_store.loc[
          (df_store.Quantity > 2) & (df_store.Sales >= 50), ['Customer ID', 'Customer Name', 'Quantity', 'Sales']])

# Traer Las ordenes que finalicen en 152, el nombre del producto que y empiece en B
print("# Traer Las ordenes que finalicen en 156, el nombre del producto que y empiece en B")
print(df_store.loc[(df_store.Order_ID.str.endswith('156')) & (df_store.Product_Name.str.startswith('B')), ['Order_ID',
                                                                                                           'Product_Name']])

# Traer El modo de envio par todas las ciudades menois para Henderson
print('# Traer El modo de envio par todas las ciudades menos para Henderson')
print(df_store.loc[df_store.City != 'Henderson', ['Ship Mode', 'City']])

# Traer las ordenes id, el cliente para las ciudades de Los Angeles, Madison y Wet Jordan que tengan mas de 2 cantidades los primeros 100 registros
# .isin(lista) verifica si el valor esta dentro de los valores de la lista pasada por parametro
print(
    '# Traer las ordenes id, el cliente para las ciudades de Los Angeles, Madison y Wet Jordan que tengan mas de 2 cantidades los primeros 100 registros')
print(df_store.loc[(df_store.City.isin(['Los Angeles', 'Madison', 'West Jordan'])) & (df_store.Quantity > 2),['Order_ID', 'Customer Name', 'City', 'Quantity']].head(100))

# Traer las 10 ordenes mas viejas
print(df_store[['Order_ID','Order_Date']].sort_values('Order_Date', ascending=False).head(10))

"""
Agrupaciones
"""

# traer la cantidad de unidades  order id
print('# traer la cantidad de unidades  por order id')
# .groupby([lista, de columnas a realizar la agrupacion])
print(df_store.groupby(['Order_ID']).Quantity.sum())



# traer la cantidad de unidades  order id que la sumatoria sea mayor a 10
print('# traer la cantidad de unidades  order id que la sumatoria sea mayor a 10')
"""
df_store.groupby(['Order_ID']).filter(lambda row: row.Quantity.sum() > 10).groupby(['Order_ID']).Quantity.sum()

df_store.groupby(['Order_ID']) # realiza una agrupacion de todo el DF por la columna pasada por parmetro
.filter(lambda row: row.Quantity.sum() > 10)  realiza un filtrado por dato agrupado, y le espeficicamos la funcion de agrupacion sum() para que realice el calculo
# sin embargo listaria de esta forma todo el DF ya que no se a realizado la agrupacion de salida solo del filtro
.groupby(['Order_ID']).Quantity.sum()  # se realiza la agrupacion sobre el filtro, y la variable operando a realizar la sumatoria

"""
print(df_store.groupby(['Order_ID']).filter(lambda row: row.Quantity.sum() > 10).groupby(['Order_ID']).Quantity.sum())
