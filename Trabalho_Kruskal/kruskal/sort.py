import numpy as np
import itertools

def max_heapify(arr, n, i, gt):
    l = 2 * i + 1 #filho esquerdo
    r = 2 * i + 2 #filho direito
    maior = i #inicializando maior na raiz
    if l < n and gt(arr[l], arr[maior]):
        maior = l
    if r < n and gt(arr[r], arr[maior]):
        maior = r
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i] #trocar
        max_heapify(arr, n, maior, gt) #heapify a raiz

def gt_func(e1,e2):
    return e1[2] > e2[2]
    
def build_max_heap(arr, n):
    for i in range(n, -1, -1):
        max_heapify(arr, n, i, gt_func)

def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr, n)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] #trocar
        max_heapify(arr, i, 0, gt_func)
    return arr

def counting_sort(arr):
    n = len(arr)
    m = max(arr, key=lambda x: x[2])[2] + 1
    count = [0] * m
    aux = [0] * n  
    res = []              
    for elem in arr:
        count[elem[2]] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            aux[i] = a
            i += 1
    for i in range(n):
        res.append([[a, b, c] for a, b, c in arr if c == aux[i]])
    return list(itertools.chain.from_iterable(res))