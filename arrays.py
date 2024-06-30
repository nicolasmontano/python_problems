def bubble_sort_nm(array):
    n = len(array)
    sorted_array = False

    i = 0
    while i <= n - 2:
        for j in range(i, n - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            else:
                break
        # if i=
        if array[i] < array[i + 1]:
            i += 1
    return array


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):  # it fixed on number therefore it reduces the space
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break

    return array


def merge_sort(array, m, l, r):
    # Merges two subarrays of arr[].
    # First subarray is arr[l..m]
    # Second subarray is arr[m+1..r]

    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    # creates the two arrays
    L = [array[i] for i in range(n1)]
    R = [array[i + m + 1] for i in range(n2)]

# array problem 4
def solution(A):
    # Implement your solution here
    n=len(A)

    count_cars=0
    number_of_1=0
    list_of_0=[]

    for i in range(n): # 0(n)
        if A[n-1-i]==1:
            number_of_1+=1
        else:
            list_of_0.append(number_of_1)

    number_pairs=sum(list_of_0) #O(n)

    if number_pairs>1000000000:
        return -1
    else:
        return number_pairs

if __name__ == '__main__':
    print(bubble_sort([3, 2, 1, 8, 4]))
