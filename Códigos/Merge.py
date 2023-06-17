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

def mergeSort(array, inicio=0, fim=None):
    if fim is None:
        fim = len(array)
    if fim - inicio > 1:
        meio = (fim + inicio) // 2
        mergeSort(array, inicio, meio)
        mergeSort(array, meio, fim)
        merge(array, inicio, meio, fim)

def merge(array, inicio, meio, fim):
    left = array[inicio:meio]
    right = array[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            array[k] = right[top_right]
            top_right += 1
        elif top_right >= len(right):
            array[k] = left[top_left]
            top_left += 1
        elif left[top_left] < right[top_right]: 
            array[k] = left[top_left]
            top_left += 1
        else: 
            array[k] = right[top_right]
            top_right += 1

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
        mergeSort(lista)
        fim = time.time()

        tempo_execucao = fim - inicio
        tempos_execucao.append(tempo_execucao)

    tempo_medio_execucao = sum(tempos_execucao) / num_execucoes
    tempos_execucao_total.append(tempo_medio_execucao)

    tempo_formatado = datetime.timedelta(seconds=tempo_medio_execucao)
    with open("resultados_merge.txt", "a") as arquivo:
        arquivo.write(f"Tamanho do array: {tamanho}\n")
        arquivo.write(f"Tempo médio de execução do MergeSort: {tempo_formatado}\n")
        arquivo.write("\n")

os.startfile("resultados_heap.txt")
# Plotar o gráfico de linhas
plt.plot(tamanhos_array, tempos_execucao_total, marker='o')
plt.xlabel('Tamanho do Array')
plt.ylabel('Tempo Médio de Execução (segundos)')
plt.title('Desempenho do Merge Sort')
plt.grid(True)
plt.show()

os.startfile("resultados_heap.txt")