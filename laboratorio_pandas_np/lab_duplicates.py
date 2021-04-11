import pandas as pd

df = pd.DataFrame({'a': ['w'] * 4 + ['x'] * 3 + ['y'] * 2 + ['z'] + ['v'],
                   'b': [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5]})

df.duplicated()  # Ver duplicados
df.duplicated(keep='first')  # marca solo la primera ocurrencia
df.duplicated(keep='last')  # marca solo la última ocurrencia
df[~ df.duplicated()]  # Filtra aquellos casos que no tienen duplicados, el ~ es negación
df.duplicated(keep=False)  # Marca todos los registros duplicados
df.drop_duplicates()  # descarta los registros duplicados, tiene por defecto el keep = first
df.drop_duplicates(['a'], keep='last')  # elimina los duplicados teniendo en cuenta una sola columna
