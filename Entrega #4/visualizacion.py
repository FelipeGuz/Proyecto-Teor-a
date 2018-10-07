#-*-coding: utf-8-*-
# Edgar Andrade, Septiembre 2018

# Visualizacion de tableros de ajedrez 4x4 a partir de
# una lista de literales. Cada literal representa una casilla;
# el literal es positivo sii hay un caballo en la casilla.

# Formato de la entrada: - las letras proposionales seran: 1, ..., 9;
#                        - solo se aceptan literales (ej. 1, ~2, 3, ~4, etc.)
# Requiere tambien un numero natural, para servir de indice del tablero,
# toda vez que puede solicitarse visualizar varios tableros.

# Salida: archivo tablero_%i.png, donde %i es un numero natural


def dibujar_tablero(f, n):
    # Visualiza un tablero dada una formula f
    # Input:
    #   - f, una lista de literales
    #   - n, un numero de identificacion del archivo
    # Output:
    #   - archivo de imagen tablero_n.png

    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    axesL = []

    #fig, axes = plt.figure()
    fig.subplots_adjust(bottom=0.02, left=0.03, top = 0.6, right=0.97)

    n = 4
    k = 10

    axes1 = plt.subplot(n, k, 1)
    plt.xticks(())
    plt.yticks(())
    axesL.append(axes1)

    axes2 = plt.subplot(n, k, 2)
    plt.xticks(())
    plt.yticks(())
    axesL.append(axes2)

    axes3 = plt.subplot(n, k, 3)
    plt.xticks(())
    plt.yticks(())
    axesL.append(axes3)

    axes4 = plt.subplot(n, k, 4)
    plt.xticks(())
    plt.yticks(())
    axesL.append(axes4)

    axes5 = plt.subplot(n, k, 5)
    plt.xticks(())
    plt.yticks(())
    axesL.append(axes5)

    axes6 = plt.subplot(n, k, 6)
    plt.xticks(())
    plt.yticks(())
    axesL.append(axes6)

    axes7 = plt.subplot(n, k, 7)
    plt.xticks(())
    plt.yticks(())
    axesL.append(axes7)

    axes8 = plt.subplot(n, k, 8)
    plt.xticks(())
    plt.yticks(())
    axesL.append(axes8)

    axes9 = plt.subplot(n, k, 9)
    plt.xticks(())
    plt.yticks(())
    axesL.append(axes9)

    axes10 = plt.subplot(n, k, 10)
    plt.xticks(())
    plt.yticks(())
    axesL.append(axes10)


    # Cargando imagen de caballo
    arr_img = plt.imread("bomba.png", format='png')
    imagebox = OffsetImage(arr_img, zoom=0.13)
    #imagebox.image.axes = axes

    cot = 0
    for l in f:
        if '~' not in l:
            ab = AnnotationBbox(imagebox, [0.5, 0.5], frameon=False)
            axesL[int(l)-1].add_artist(ab)
            cot = cot+1

    plt.show()
    #fig.savefig("tablero_" + str(n) + ".png")


#################
# importando paquetes para dibujar
print "Importando paquetes..."
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import csv
from sys import argv
print "Listo!"

data_archivo = "tableros.csv"
with open(data_archivo) as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    contador = 1
    for l in data:
        print "Dibujando tablero:", l
        dibujar_tablero(l, contador)
        contador += 1
        
        

csv_file.close()
