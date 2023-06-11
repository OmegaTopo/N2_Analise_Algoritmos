import random
import time
import datetime
import os

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

# Função para selecionar o pivô e rearranjar os elementos menores à esquerda e maiores à direita e ordenar

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivo = arr[0]
        esquerda = [x for x in arr[1:] if x < pivo]
        direita = [x for x in arr[1:] if x >= pivo]
        return quicksort(esquerda) + [pivo] + quicksort(direita)

# Início do programa
num_execucoes = 5
tamanhos_array = [TAMANHO_VETOR_1000, TAMANHO_VETOR_10000, TAMANHO_VETOR_50000, TAMANHO_VETOR_100000, TAMANHO_VETOR_500000, TAMANHO_VETOR_1000000]

with open("resultados.txt", "w") as arquivo:
    for tamanho in tamanhos_array:
        tempos_execucao = []

        for _ in range(num_execucoes):
            lista = []
            generateRand(lista, tamanho)

            inicio = time.time()
            quicksort(lista)
            fim = time.time()

            tempo_execucao = fim - inicio
            tempos_execucao.append(tempo_execucao)

        tempo_medio_execucao = sum(tempos_execucao) / num_execucoes

        tempo_formatado = datetime.timedelta(seconds=tempo_medio_execucao)
        arquivo.write(f"Tamanho do array: {tamanho}\n")
        arquivo.write(f"Tempo médio de execução do HeapSort: {tempo_formatado}\n")
        arquivo.write("\n")

os.startfile("resultados.txt")