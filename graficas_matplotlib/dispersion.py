# pip install matplotlib

import matplotlib.pyplot as plt
from matplotlib import style

# seteamos el estilo
style.use('ggplot')
print("estilos disponibles | style.available", style.available)

plt.plot(
    [1,2,3,4],
    [1,66,222,100],
    "bo"
)

# .axis([]) x min x max y min y max
plt.axis([0,4.5,0,222])
plt.show()
