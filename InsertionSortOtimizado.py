import random
import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1

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
    sorted_array = insertion_sort(array)
    end_time = time.time()

    execution_time = end_time - start_time

    execution_times.append(execution_time)
    sizes.append(size)

    print(f"Array size: {size}\tExecution time: {execution_time:.6f} seconds")

# Plotar o gráfico
plt.plot(sizes, execution_times, marker='o')
plt.xlabel('Tamanho do Array')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Tempo de Execução do Insertion Sort Otimizado')
plt.grid(True)
plt.show()

# Array size: 1000 Execution time: 0.000888 seconds
# Array size: 5000 Execution time: 0.005494 seconds
# Array size: 10000 Execution time: 0.020824 seconds
# Array size: 50000 Execution time: 1.092999 seconds
# Array size: 100000 Execution time: 4.268157 seconds
# Array size: 500000 Execution time: 214.056491 seconds
# Array size: 1000000 Execution time: 866.183492 seconds