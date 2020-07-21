# pip install matplotlib

import matplotlib.pyplot as plt
from matplotlib import style

# seteamos el estilo
style.use('ggplot')

# Grafica de barras
plt.bar(
    [1,2,3,4,5],
    [4,5,6,7,8],
    label="Gustavo",
    color='m',
    align='center',
)
plt.title = 'Resultados'
plt.xlabel('Semestre')
plt.ylabel('Notas')
plt.legend()
plt.grid(True, color="y")


plt.show()