from typing import List



def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = 0
    j = 0
    len_num1 = m+n
    while i < len_num1:
        # update
        if nums2[j] <= nums1[i] or nums1[i] == 0:

            # insert  and update list
            for num_ in range(i + 1, len_num1):  # deletes the last index
                nums1[len_num1 - num_ + 1] = nums1[len_num1 - num_]

            nums1[i] = nums2[j]
            j += 1
            i += 1
        else:
            i += 1
        print(nums1)

    return nums1

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

if __name__ == '__main__':
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1,m,nums2,n)