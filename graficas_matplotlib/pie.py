# pip install matplotlib

import matplotlib.pyplot as plt
from matplotlib import style

# seteamos el estilo
style.use('ggplot')
print("estilos disponibles | style.available", style.available)

horas = [8,4]
actividades = ["Trabajo", "Estudio"]
colores = ["r", "orange"]


plt.pie(
    horas,
    labels=actividades,
    colors=colores,
    startangle=90,
    explode=(0,0.1), # separacion de la fraccion del pie
    autopct="%.1f%%"   # para que muestre los porcentajes
)


plt.show()
