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
def get_highest_count_num(lst):
    #initialise variables
    highest_num = None
    highest = 0
    num_count = {}

    for num in lst:

        #count each number
        if num in num_count.keys():
            num_count[num] += 1
        else:
            num_count[num] = 1
        
        #update the highest if needed
        if num_count[num] > highest:
            highest = num_count[num]
            highest_num = num
    
    return highest_num


print(get_highest_count_num(input_lst))