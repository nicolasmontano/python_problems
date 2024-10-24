from typing import List

# k is the sum that need to be equal to. count the numbers of sub-arrays that fulfill the condition
# save in the dictionary the condition you need e.g. odds number or if sum is multiple of
# the current_prefix_sum the thing  want to compare to k
"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
"""


def subarraySum(nums: List[int], k: int) -> int:

    cum_sum_dict = {0: 1}
    count = 0
    cum_sum = 0

    for num in nums:
        cum_sum += num
        if cum_sum - k in cum_sum_dict:
            count += cum_sum_dict[cum_sum - k]

        if cum_sum in cum_sum_dict:
            cum_sum_dict[cum_sum] += 1
        else:
            cum_sum_dict[cum_sum] = 1

        print(num, cum_sum, cum_sum - k, cum_sum_dict)

    return count


"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.
"""


def numberOfSubarrays(nums: List[int], k: int) -> int:
    prefix_counts = {0: 1}
    current_prefix_sum = 0
    count = 0

    for num in nums:
        if num % 2 != 0:
            current_prefix_sum += 1

        if (current_prefix_sum - k) in prefix_counts:
            count += prefix_counts[current_prefix_sum - k]

        if current_prefix_sum in prefix_counts:
            prefix_counts[current_prefix_sum] += 1
        else:
            prefix_counts[current_prefix_sum] = 1

    return count


"""
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
"""
def checkSubarraySum(nums: List[int], k: int) -> bool:

    mod_map = {0: -1}  # Initialize with 0:-1 to handle the case where sum is multiple of k from the start
    prefix_sum = 0

    for i, num in enumerate(nums):
        prefix_sum += num
        mod = prefix_sum % k

        if mod in mod_map:
            # Check if the subarray length is at least 2
            if i - mod_map[mod] > 1:
                return True
        else:
            # Store the index of this mod
            mod_map[mod] = i

        print(f"i: num: mod: mod_map")

    return False

