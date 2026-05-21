import random
import time
import matplotlib.pyplot as plt

def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


def selection_sort(lista):
    n = len(lista)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if lista[j] < lista[min_index]:
                min_index = j

        lista[i], lista[min_index] = lista[min_index], lista[i]

    return lista

def insertion_sort(lista):
    n = len(lista)

    for i in range(1, n):
        actual = lista[i]
        j = i - 1


        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = actual
        print(lista)
        return lista


tamaños = [500, 1000, 2000, 5000, 10000]

tiempos_bubble = []
tiempos_selection = []
tiempo_insertion = []

for n in tamaños:
    lista_original = [random.randint(0, 10000) for _ in range(n)]

    lista_bubble = lista_original.copy()

    inicio = time.perf_counter()
    bubble_sort(lista_bubble)
    fin = time.perf_counter()

    tiempos_bubble.append(fin - inicio)

    lista_selection = lista_original.copy()

    inicio = time.perf_counter()
    selection_sort(lista_selection)
    fin = time.perf_counter()

    tiempos_selection.append(fin - inicio)

    lista_insertion = lista_original.copy()

    inicio = time.perf_counter()
    insertion_sort(lista_insertion)
    fin = time.perf_counter()
    
    tiempo_insertion.append(fin - inicio)

plt.plot(tamaños, tiempos_bubble, marker="o", label="Bubble Sort")
plt.plot(tamaños, tiempos_selection, marker="o", label="Selection Sort")
plt.plot(tamaños, tiempo_insertion, marker="o", label="Insertion Sort")

plt.title("Comparación")
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo")
plt.legend()
plt.grid(True)

plt.show()