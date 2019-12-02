def selectionSort(A):
    for i in range(len(A)):

        # Acha o elemento mínimo no array
        min = i
        for j in range(i + 1, len(A)):
            if A[min] > A[j]:
                min = j

        # Troca o elemento minimo com o primeiro elemento do array
        A[i], A[min] = A[min], A[i]

    return A