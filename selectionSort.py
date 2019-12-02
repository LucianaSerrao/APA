def selectionSort(A):
    for i in range(len(A)):

        # Find the minimum element in remaining
        # unsorted array
        min = i
        for j in range(i + 1, len(A)):
            if A[min] > A[j]:
                min = j

        # Swap the found minimum element with
        # the first element
        A[i], A[min] = A[min], A[i]

    return A