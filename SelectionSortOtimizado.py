import random
import time
import matplotlib.pyplot as plt

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

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
    sorted_array = selection_sort(array)
    end_time = time.time()

    execution_time = end_time - start_time

    execution_times.append(execution_time)
    sizes.append(size)

    print(f"Array size: {size}\tExecution time: {execution_time:.6f} seconds")

# Plotar o gráfico
plt.plot(sizes, execution_times, marker='o')
plt.xlabel('Tamanho do Array')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Tempo de Execução do Selection Sort Otimizado')
plt.grid(True)
plt.show()
