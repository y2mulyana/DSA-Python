# Two sum
test_1 = [7,2] #target = 9
test_2 = [2,7,3,-1,4] #target = 2
test_3 = [25] #target = [] because need 2 integer
test_4 = [] #target = [] because need 2 integer
test_5 = [2, 7, 11, 15] #target 9
test_6 = [2, -1, 5, 3] #target 4
test_7 = [3, 2, 4] #target 6

"""
def two_sum(lst, target):
    if len(lst) < 2:
        return []
    else:
        for i in lst:
            dummy = target - i
            if dummy in lst and dummy != i:
                print([i, dummy])
                print([lst.index(i), lst.index(dummy)])
                return [lst.index(i), lst.index(dummy)]


double find i in for list type is  o(n^2) and in dictionary is o(1)

"""
def two_sum(array,target):
    num_available = {}
    for i in range(len(array)):
        needed_val = target - array[i]
        if needed_val in num_available:
            print([i,num_available[needed_val]])
            return [i,num_available[needed_val]]
        else:
            num_available[array[i]]=i
    return []


two_sum(test_7, 6)