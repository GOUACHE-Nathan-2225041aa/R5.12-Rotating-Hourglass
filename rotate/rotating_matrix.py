import matplotlib.pyplot as plt
import numpy as np

# Exemple de matrice 2D
matrix = np.array([[1, 1, 1],
                   [4, 5, 6],
                   [7, 8, 9]])

# Dimensions de la matrice
rows, cols = matrix.shape

# Parcourir la matrice pour tracer les points
for i in range(rows):
    for j in range(cols):
        plt.plot(j, -i, 'o', label=f'Value: {matrix[i, j]}' if i == 0 and j == 0 else "") # -i pour inverser les axes

# Ajouter des axes et une grille
plt.xticks(range(cols))
plt.yticks([-i for i in range(rows)])
plt.grid(True)

# Afficher la figure
plt.title("Matrice affichée avec matplotlib.plot")
plt.xlabel("Colonnes")
plt.ylabel("Lignes")
plt.show()
