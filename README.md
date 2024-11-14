# Problems
Solve these 100 carefully curated problems in order! See you at the top!
## page
https://topswe.com/

# Binary search problems
## 31. binary search (easy)

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.


```python
def search(self, nums: List[int], target: int) -> int:
    low = 0 
    high = len(nums) - 1 
    while low <= high: 
        mid = (low + high) // 2 
        if nums[mid] == target: 
            return mid 
        elif nums[mid] < target: 
            low = mid + 1 
        else: high = mid - 1   
    return -1 # Target not found
```

## 41.  First bad version (easy)
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
```python
def firstBadVersion(self, n: int) -> int:
    left=1 # start always at 1 to return left
    right=n
    while left<right:
        mid=(left+right)//2

        if isBadVersion(mid):
            right=mid
        else:
            left=mid+1

    return left

    # [false, false,  true, true]
    # will return first true when low==high
```
# Hash table
## 37. Group anagrams (medium)
Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    str_dict=defaultdict(list)

    for str_ in strs:
        key=''.join(sorted(str_))
        str_dict[key].append(str_)
    
    return [value for value  in  str_dict.values()]
```
# Hash table
## 29. Group anagrams (easy)
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
```python
def isValid(self, s: str) -> bool:
    stack=[]
    dict_symbol={'}':'{',
                    ']':'[',
                    ')':'('
    }
    for str_ in s:           
        if str_ in ["(","[","{"]:
            stack.append(str_)
        elif stack and dict_symbol[str_]==stack[-1]:
            stack.pop()
        else:
            return False
    if stack:
        return False
    return True    
```
## 40. Insert Delete GetRandom O(1)
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
```python
from random import  randint
class RandomizedSet:

    def __init__(self):
        self.values_dict=dict()
        self.values_list=[]

    def insert(self, val: int) -> bool:
        # print("insert",self.values_dict.keys())
        if val not in self.values_dict.keys():
            self.values_dict[val]=len(self.values_list)
            self.values_list.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        # print("remove",self.values_dict.keys())
        if val not in self.values_dict.keys():
            return False
        else:
            index=self.values_dict[val]
            val_replace=self.values_list[-1]
            self.values_dict[self.values_list[-1]]=index
            self.values_list[index]=val_replace
            self.values_list.pop()
            self.values_dict.pop(val)
            # print("remove_2",self.values_dict.keys())
            return True

    def getRandom(self) -> int:
        if self.values_list:
            max_index=len(self.values_list)-1
            return self.values_list[randint(0,max_index)]
        else:
            return None
```
# Sorted list by key
## 39. K Closest Points to Origin
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
```python
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

    def calc_eucl_dist(x1:List[int],x2:List[int]=[0,0]):
        return math.sqrt((x1[0]-x2[0])**2+(x1[1]-x2[1])**2)
    
    new_list=[]
    for point in points:
        new_list.append((point,calc_eucl_dist(point)))
    new_list.sort(key=lambda x:x[1])
    return [x[0] for x in new_list[:k]]
```

# Continious Subarrays
## 39. K Closest Points to Origin
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
```python
from collections import defaultdict
def subarraySum(self, nums: List[int], k: int) -> int:
    count = 0
    sum_counts=defaultdict(int)
    sum_counts[0]=1 # Initialize with a sum of 0 occurring for the first sum-k
    current_sum = 0

    for num in nums:
        current_sum += num
        if current_sum - k in sum_counts:
            count += sum_counts[current_sum - k]
        sum_counts[current_sum]+=1 # to consider 0 or negatives
    return count
```

# Kadane's Algorithm (max subarray)
## 51. Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.
```python
def maxSubArray(self, nums: List[int]) -> int:
    max_current = max_global = nums[0]

    for num in nums[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)
    
    return max_global
```
## 51. Maximum Product Subarray
Given an integer array nums, find a subarray that has the largest product, and return the product.
```python
def maxProduct(self, nums: List[int]) -> int:
    max_prod = min_prod = max_global = nums[0]
     # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current number is negative, swapping max_prod and min_prod helps manage sign flipping
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod
  
        # Calculate max and min products at the current position
        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
  
        # Update the result with the maximum product found so far
        max_global = max(max_global, max_prod)
    return max_global
```
# Sliding Window
## 56. 	Longest Substring Without Repeating Characters 
Given a string s, find the length of the longest substring without repeating characters.
```python
def lengthOfLongestSubstring(self, s: str) -> int:
    # s="tmmzuxt"
    max_len=0
    char_dict={}
    start,end=0,0
    for i,char in enumerate(s):
        if char in char_dict and char_dict[char]>=start:
            start=char_dict[char]+1
        
        char_dict[char]=i
        end=i
        # print(start,end)
        max_len=max(max_len,end-start+1)
    return max_len
```
## 57. Max Consecutive Ones III 
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
```python
def longestOnes(self, nums: List[int], k: int) -> int:
    left = 0
    right = 0
    max_length = 0
    zero_count = 0
    
    while right<len(nums):
        if nums[right]==0:
            zero_count+=1
        
        while zero_count>k:
            if nums[left]==0:
                zero_count -= 1
            left+=1

        max_length=max(max_length,right-left+1)
        right+=1
    
    return max_length
```
## 58. Maximize the Confusion of an Exam
A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. 
He wants to confuse the students by maximizing the number of consecutive questions with the same answer 
(multiple trues or multiple falses in a row).
```python
def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
    # sliding window
    def max_consec(char):
        left = 0
        right = 0
        max_len=0
        char_to_change=0

        while right<len(answerKey):

            if answerKey[right]!=char:
                char_to_change+=1

            while char_to_change>k:
                if answerKey[left]!=char:
                    char_to_change-=1
                left+=1

            max_len=max(max_len,right-left+1)
            right+=1

        return max_len
```
# multiple functions in one
## 58. return one, next
return x = [1, 2, None, 3, [4, '5', 6, [7, 8, 9]]]  first, third, fifth, ...
```python
def main(input_structure):
    output_list: list[str, int, float,None] = []
    counter: int = 0

    def return_one_other(structure: list[Any]):
        nonlocal counter
        for i, elem in enumerate(structure):
            if isinstance(elem, list):
                return_one_other(elem)

            elif isinstance(elem, (str, int, float)):
                counter += 1
                if counter % 2 > 0:
                    output_list.append(elem)
            else:
                pass
            # print(elem)

    return_one_other(input_structure)
    return output_list
```
