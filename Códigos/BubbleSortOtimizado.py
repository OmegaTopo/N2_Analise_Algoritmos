import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        n -= 1

# Função para gerar um array desordenado de tamanho específico
def generate_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

# Tamanhos dos arrays
array_sizes = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]


# Listas para armazenar os tempos de execução e os tamanhos dos arrays
execution_times = []
sizes = []

# Ordenar e medir o tempo de execução para cada tamanho de array
for size in array_sizes:
    array = generate_array(size)

    start_time = time.time()
    sorted_array = bubble_sort(array)
    end_time = time.time()

    execution_time = end_time - start_time

    execution_times.append(execution_time)
    sizes.append(size)

    print(f"Array size: {size}\tExecution time: {execution_time:.6f} seconds")

# Plotar o gráfico
plt.plot(sizes, execution_times, marker='o')
plt.xlabel('Tamanho do Array')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Tempo de Execução do Bubble Sort Otimizado')
plt.grid(True)
plt.show()
