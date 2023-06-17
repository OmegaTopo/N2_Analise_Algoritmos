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

# Função para ordenar

def heapify(arr, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and arr[i] < arr[esquerda]:
        maior = esquerda

    if direita < n and arr[maior] < arr[direita]:
        maior = direita

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)


def heapSort(arr):
    tamanho = len(arr)

    # Construindo o heap máximo
    for i in range(tamanho // 2 - 1, -1, -1):
        heapify(arr, tamanho, i)

    # Extrai os elementos um por um
    for i in range(tamanho - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Troca o primeiro e último elemento
        heapify(arr, i, 0)

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
        heapSort(lista)
        fim = time.time()

        tempo_execucao = fim - inicio
        tempos_execucao.append(tempo_execucao)

    tempo_medio_execucao = sum(tempos_execucao) / num_execucoes
    tempos_execucao_total.append(tempo_medio_execucao)

    tempo_formatado = datetime.timedelta(seconds=tempo_medio_execucao)
    with open("resultados_heap.txt", "a") as arquivo:
        arquivo.write(f"Tamanho do array: {tamanho}\n")
        arquivo.write(f"Tempo médio de execução do HeapSort: {tempo_formatado}\n")
        arquivo.write("\n")

# Plotar o gráfico de linhas
plt.plot(tamanhos_array, tempos_execucao_total, marker='o')
plt.xlabel('Tamanho do Array')
plt.ylabel('Tempo Médio de Execução (segundos)')
plt.title('Desempenho do HeapSort')
plt.grid(True)
plt.show()

os.startfile("resultados_heap.txt")