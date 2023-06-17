import random
import time
import datetime
import os
import matplotlib.pyplot as plt

# Constantes de tamanho de array
TAMANHO_VETOR_1000 = 1000
TAMANHO_VETOR_10000 = 10000
TAMANHO_VETOR_50000 = 50000
TAMANHO_VETOR_100000 = 100000
TAMANHO_VETOR_500000 = 500000
TAMANHO_VETOR_1000000 = 1000000

# Funções
def generateRand(array, tamanho):
    numeros_gerados = set()  # Conjunto para armazenar os números gerados
    while len(numeros_gerados) < tamanho:
        numero_aleatorio = random.randint(1, (tamanho*3))
        numeros_gerados.add(numero_aleatorio)
    
    array.extend(numeros_gerados)

def merge_sort_hibrido(arr):
    if len(arr) <= 16:
        insertion_sort(arr)
    else:
        meio = len(arr) // 2
        esquerda = arr[:meio]
        direita = arr[meio:]

        merge_sort_hibrido(esquerda)
        merge_sort_hibrido(direita)

        merge(arr, esquerda, direita)

def merge(arr, esquerda, direita):
    i = j = k = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            arr[k] = esquerda[i]
            i += 1
        else:
            arr[k] = direita[j]
            j += 1
        k += 1

    while i < len(esquerda):
        arr[k] = esquerda[i]
        i += 1
        k += 1

    while j < len(direita):
        arr[k] = direita[j]
        j += 1
        k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = chave


# Início do programa
num_execucoes = 5
tamanhos_array = [TAMANHO_VETOR_1000, TAMANHO_VETOR_10000, TAMANHO_VETOR_50000, TAMANHO_VETOR_100000, TAMANHO_VETOR_500000, TAMANHO_VETOR_1000000]

tempos_execucao_total = []

for tamanho in tamanhos_array:
    tempos_execucao = []

    for _ in range(num_execucoes):
        lista = []
        generateRand(lista, tamanho)

        inicio = time.time()
        merge_sort_hibrido(lista)
        fim = time.time()

        tempo_execucao = fim - inicio
        tempos_execucao.append(tempo_execucao)

    tempo_medio_execucao = sum(tempos_execucao) / num_execucoes
    tempos_execucao_total.append(tempo_medio_execucao)

    tempo_formatado = datetime.timedelta(seconds=tempo_medio_execucao)
    with open("resultados_merge_melhorado.txt", "a") as arquivo:
        arquivo.write(f"Tamanho do array: {tamanho}\n")
        arquivo.write(f"Tempo médio de execução do MergeSortHibrido: {tempo_formatado}\n")
        arquivo.write("\n")

# Plotar o gráfico de linhas
plt.plot(tamanhos_array, tempos_execucao_total, marker='o')
plt.xlabel('Tamanho do Array')
plt.ylabel('Tempo Médio de Execução (segundos)')
plt.title('Desempenho do Merge Sort Híbrido')
plt.grid(True)
plt.show()

os.startfile("resultados_merge_melhorado.txt")