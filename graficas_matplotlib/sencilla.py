# pip install matplotlib

import matplotlib.pyplot as plt
from matplotlib import style

# seteamos el estilo
style.use('ggplot')
print("estilos disponibles | style.available", style.available)

# proporcionamos 2 listas [x, y]
plt.plot(
    [1,2,3,4,5],
    [23,22,12,32,5]
)
plt.title('Resultados')
plt.xlabel('Semestre')
plt.ylabel('Notas')

plt.show()
