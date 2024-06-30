def bubble_sort(array):
    n = len(array)
    i = 0
    sorted_array = False
    while sorted_array == False:

        for j in range(n - 1 - i):  # -1 bc adj -i is reducing for every loop

            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]
            else:
                break
        if array[i] < array[i + 1]:
            i += 1

        if i == n - 1:
            sorted_array = True

    return array


bubble_sort([1, 3, 2])
