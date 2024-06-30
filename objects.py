# Strings
string = "abcd1"
string.lower()
string.isnumeric()
string.count("a")
string[-1::-1]  # reverse as string '1dcba'
string[:5:2]  # go by two "ac1"

# List
# list index [0,1,2,3] neg: [-4,-3,-2,-1]  -> positive list[index:how many records needed]  , negative list[index forward: <index]
list_ = [1, 2, 3, 4,0]
list_.reverse()  # reverse # O(n)
list_.sort(reverse=True)  # inplace O(n log n)
sorted([(i,val) for i,val in enumerate(list_)],key= lambda  x: x[1]) # sorted list with index
set(list_)
[*enumerate(l)] # creates a list, with index

# dict
dict_ = {"a": 1, "b": 2, "c": 0}
sorted(dict_.items(), key=lambda x: x[1])  # sort by value, sorted func returns a list
dict(zip([0, 1], ["a", "b"]))  # dict from  two lists
sorted(dict_.items(), key=lambda x: x[1], reverse=True)  # sorted list
dict(sorted(dict_.items(), key=lambda x: x[1], reverse=True))  # sorted dict

# set
set_0 = {1, 2, 3, 3}
set_1 = {1, 2, 4, 4}
set_0.intersection(set_1)  # intersection O(min(len(set_0), len(set_1)))
set_0 - set_1  # missing in set_1 {3}
x in set(1,2,3,4) #counting

# Collections
from collections import defaultdict, Counter

# Defaultdict: useful for looping  and avoid Key_error when adding a new element
dict_ = defaultdict(int)  # works as a dict, int means dict_.values() as int ==0
dict_['a'] += 1  # avoid Key_error when adding a new element

# CounterUseful: dict like object that counts number of appearances
counter_0 = Counter([1, 1, 1, 2, 2])  # can accept list, dicts, works as a dict:Counter({1: 3, 2: 2})
counter_1 = Counter([1, 1, 3, 3])
counter_0 - counter_1  # missing elements in 1 , {2: 2, 1: 1}
counter_1 - counter_0  # missing elements in 0, {3: 2}

for key, value in Counter(dict_).items():
    print(key, value)

for i in range(-1):
    print(i)


# if sequence then add

# hol max to store