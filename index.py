import matplotlib.pyplot as plt
import time


def selection(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def counting(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr

def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def quickssort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickssort(left) + middle + quickssort(right)

incomedata = [300, 2000]  # Replace with your own incomedata

bubblet = []
selectiont = []
countingt = []
quickssortt = []

for i in range(1, len(incomedata) + 1):
    subset = incomedata[:i]
    
    start_time = time.time()
    bubble(subset)
    bubblet.append(time.time() - start_time)
    
    start_time = time.time()
    selection(subset)
    selectiont.append(time.time() - start_time)
    
    start_time = time.time()
    counting(subset)
    countingt.append(time.time() - start_time)
    
    start_time = time.time()
    quickssort(subset)
    quickssortt.append(time.time() - start_time)

plt.plot(range(1, len(incomedata) + 1), bubblet, label='Bubble Sort')
plt.plot(range(1, len(incomedata) + 1), selectiont, label='Selection Sort')
plt.plot(range(1, len(incomedata) + 1), countingt, label='Counting Sort')
plt.plot(range(1, len(incomedata) + 1), quickssortt, label='Quicksort')

plt.xlabel('meghdar dade vorodi')
plt.ylabel('Time')
plt.title('compare datas')
plt.legend()
plt.show()
