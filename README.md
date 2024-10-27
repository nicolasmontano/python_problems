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
## 29. Group anagrams (medium)
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
