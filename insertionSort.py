

def insertionSort(A):
    for i in range(1, len(A)):
        x = A[i] #ponteiro auxiliar
        j = i - 1 #ponteiro de verificação
        while j >= 0 and x < A[j]:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = x

    return A
