import numpy as np
import matplotlib.pyplot as plt

# 1. Crear los arreglos
datos_semestres = [
    ("Semestre 1", 1),
    ("Semestre 2", 2),
    ("Semestre 3", 3),
    ("Semestre 4", 4),
    ("Semestre 5", 5),
    ("Semestre 6", 6),
    ("Semestre 7", 7),
    ("Semestre 8", 8)
]

promedios = [8.5, 7.8, 9.2, 8.0, 7.5, 8.3, 8.9, 9.0]

# Extraer los números de semestre y nombres
nombres_semestres = [d[0] for d in datos_semestres]
numeros_semestres = [d[1] for d in datos_semestres]

# 2. Calcular media y mediana
media = np.mean(promedios)
mediana = np.median(promedios)

print(f"Media de promedios: {media:.2f}")
print(f"Mediana de promedios: {mediana:.2f}")

# 3. Graficar los arreglos
plt.figure(figsize=(10,5))
plt.plot(numeros_semestres, promedios, marker='o', linestyle='-', color='b', label='Promedio por semestre')
plt.axhline(y=media, color='r', linestyle='--', label=f'Media: {media:.2f}')
plt.axhline(y=mediana, color='g', linestyle='-.', label=f'Mediana: {mediana:.2f}')
plt.xticks(numeros_semestres, nombres_semestres, rotation=45)
plt.xlabel("Semestres")
plt.ylabel("Promedio")
plt.title("Promedios por semestre")
plt.legend()
plt.grid()
plt.show()
