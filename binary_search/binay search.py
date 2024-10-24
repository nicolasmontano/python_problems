# ordered list then evalutes (find a min, max)

''''
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version,all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version.
 You should minimize the number of calls to the API.
'''
from typing import List


def firstBadVersion(n: int) -> int:
    left, right = 1, n

    while left < right:
        mid = (left + right) // 2
            right = mid
        else:
            left = mid + 1
    return left


items = [1, 2, 3]
max(enumerate(items), key=lambda x: x[1])[0]

'''
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.
'''


def findPeakElement(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            lef = mid + 1

    return left
