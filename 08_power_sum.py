test_1 = [1, 2, 3] # 1 + 2 + 3 = 6^1
test_2 = [1, 2, [3]] # 1 + 2 + 3^2, because 3 is a list inside list level 2
test_3 = [1, 2, [3, 4], [[2]]] # 1 + 2 + (3 + 4)^2 + 2^3 

def power_sum(array,power=1):
    #write code here
