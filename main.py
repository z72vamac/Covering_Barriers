import gurobipy as gp
from gurobipy import GRB
import numpy as np
from itertools import product, permutations, chain
import random
import matplotlib.pyplot as plt
# from matplotlib.patches import Circle, Polygon
from matplotlib.collections import PatchCollection
from data import *
import neighborhood as neigh
import copy
import estimacion_M as eM
import auxiliar_functions as af
import networkx as nx

from spp_barriers import hspp_b

# from HTSPS_without_prepro import HTSPS_without_prepro
# 50-3

# segments = np.genfromtxt('./instancias/segmentos50-3.csv', delimiter = ',')

# barriers = []
# for lista in segments:
#     barriers.append([[lista[0], lista[1]], [lista[2], lista[3]]])

# bolas = np.genfromtxt('./instancias/bolas50-3.csv', delimiter = ',')
# sources = [neigh.Circle(center = [centro1, centro2], radii = radio, col = 'blue') for centro1, centro2, radio in bolas]

# targets = [neigh.Circle(center = [centro1, centro2], radii = radio, col = 'red') for centro1, centro2, radio in bolas]
#
# k = 3
#
# resultados = h_kmedian_n(barriers, sources, targets, k, time_limit=3600, prepro=True, log=False, picture=True)

# from h_kmedian_n_moresubindex import h_kmedian_n
# from h_kmedian_n import h_kmedian_n
#
## EXAMPLE NON-VISIBLE

barrier1 = [[0, 90], [30, 60]]
barrier2 = [[10, 50], [40, 50]]
barrier3 = [[0, 30], [10, 40]]
barrier4 = [[10, 30], [30, 5]]
barrier5 = [[40, 10], [70, 40]]
barrier6 = [[60, 20], [100, 10]]
barrier7 = [[30, 70], [70, 95]]
barrier8 = [[70, 90], [60, 50]]
barrier9 = [[70, 80], [90, 60]]
barrier10 = [[74, 33], [98, 60]]

barriers = [barrier1, barrier2, barrier3, barrier4, barrier5, barrier6, barrier7, barrier8, barrier9, barrier10]
# barriers = [barrier3, barrier5, barrier6, barrier7, barrier8]

N1s = neigh.Circle(center=[70, 55], radii=4, col = 'green')
N2s = neigh.Circle(center=[50, 70], radii=8, col = 'green')
N3s = neigh.Circle(center=[30, 35], radii=10, col = 'green')
N4s = neigh.Circle(center=[5, 40], radii= 12, col = 'green')

sources = [N1s, N2s, N3s, N4s]
# sources = [N1s]

N1t = neigh.Circle(center=[10, 15], radii=6, col = 'blue')
N2t = neigh.Circle(center=[65, 10], radii=7, col = 'blue')
N3t = neigh.Circle(center=[10, 65], radii=5, col = 'blue')
N4t = neigh.Circle(center=[90, 35], radii=6, col = 'blue')
N5t = neigh.Circle(center=[90, 85], radii=6, col = 'blue')
N6t = neigh.Circle(center=[30, 90], radii=10, col = 'blue')

targets = [N1t, N2t, N3t, N4t, N5t, N6t]
targets = [N1t]

k = 3

endurance = 1000

wE = 1

wL = 0

# 279.88
# resultados = hspp_b(barriers, sources=sources, targets=targets, k=k, wL=wL, lazy=False, A4=False, time_limit=1800, picture=True, init = False)

# resultados = hspp_b(barriers, sources, targets, wL = 0, A4 = True, log=False, picture=True, time_limit=7200, init=False)

# print(resultados)


# fig, ax = plt.subplots()

x_coords = list(np.linspace(0, 100, 1001))
y_coords = list(np.linspace(0, 100, 1001))

distancias = np.zeros((1000, 1000))

# for b in barriers:
#     ax.plot([b[0][0], b[1][0]], [b[0][1], b[1][1]], c='red')

for s in range(len(sources)):
    for i in range(1000):
        for j in range(1000):
            targets = [neigh.Circle(center=[x_coords[i], y_coords[j]], radii=0.01, col = 'blue')]
            resultados = hspp_b(barriers, [sources[s]], targets, wL = 0, A4 = False, log=False, picture=False, time_limit=7200, init=False)

            distancias[i, j] = resultados[1]

            # if resultados[1] < radii:
            #     ax.scatter(xcor, ycor, color = 'blue')
            # else:
            #     ax.scatter(xcor, ycor, color = 'red')

        np.savetxt('distancias_' + str(s) + '.csv', distancias, delimiter=',')
# ax.scatter(sources[0].center[0], sources[0].center[1], c='green')

# plt.axis([0, 100, 0, 100])

# ax.set_aspect('equal')
# plt.show()




# radii = 30

# for i in range(100):
#     for j in range(100):
#         if distancias[i, j] < radii:
#             ax.scatter(x_coords[i], y_coords[j], color = 'blue')
#         else:
#             ax.scatter(x_coords[i], y_coords[j], color = 'red')

# for b in barriers:
#     ax.plot([b[0][0], b[1][0]], [b[0][1], b[1][1]], c='red')

# plt.axis([0, 100, 0, 100])

# ax.set_aspect('equal')
# plt.show()

# import seaborn as sns

# distancias = np.genfromtxt('distancias.csv', delimiter = ',').T

# fig, ax = plt.subplots()

# sns.heatmap(distancias[::-1, :], cmap = 'Greys')

# plt.show()

