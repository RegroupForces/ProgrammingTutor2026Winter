"""
TASK
Given a list of integers, find the integer that occurs most frequently. 
E.g, given [1,2,3,3,3,4,4,5], your solution should produce 3 as a result. 
If there are multiple occurrences of most frequent, select the integer first counted as most frequent. 
E.g given [1,2,2,3,4,4], your solution should produce 2 as a result. 
There are many ways to do this, don’t worry about efficiency. 
"""

#example
input_lst = [1,2,3,3,3,4,4,5] #this is the first example in the question


#solution
num_count = {}
for item in input_lst:
    if item in num_count.keys():
        num_count[item] += 1
    else:
        num_count[item] = 1

res = sorted(num_count.values(), reverse=True)[0]

print(res)