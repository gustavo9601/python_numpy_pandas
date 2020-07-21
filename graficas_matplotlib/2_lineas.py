# pip install matplotlib

import matplotlib.pyplot as plt
from matplotlib import style

# seteamos el estilo
style.use('ggplot')

# Grafica de barras
plt.plot(
    [1,2,3,4,5],
    [4,2,2,4,1],
    label="Gustavo"
)

plt.plot(
    [9,2,3,4,5],
    [5,2,2,2,1],
    label="Meliza"
)
plt.title = 'Resultados'
plt.xlabel('Semestre')
plt.ylabel('Notas')
plt.legend()


plt.show()