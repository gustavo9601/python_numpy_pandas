# pip install matplotlib

import matplotlib.pyplot as plt
from matplotlib import style

# Grafica de barras
lluvia = [17,22,88]
meses = ["Enero", "Febrero", "Marzo"]

plt.bar(
    meses,
    lluvia,
    color='orange',
    align='center',
)

plt.show()