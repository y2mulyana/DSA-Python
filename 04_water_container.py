# Water container problem

test_1 = [1, 5, 6, 3, 4] # the container can contain is 5 & 4 = 12 volume unit
test_2 = [1,8,6,2,5,4,8,3,7] # the container can contain is 49 volume unit
test_3 = [10, 6, 5, 6, 9, 7] # the container can contain is 35 volume unit
test_4 = [7, 1, 8, 4, 3, 2, 5] # The container can hold a volume of 28 units.
test_5 = [1,1] #1
test_6 = [3, 7, 5, 6, 8, 4] # 21
test_7 = [1, 8, 6, 2, 5, 4, 8, 3, 7] #49s

def max_area(lst):
    a = 0
    b = len(lst) - 1
    area = 0
    step = 0
    while a < b:
        if lst[a] < lst[b]:
            area_1 = lst[a] * (b - a)
            if area < area_1:
                area = area_1
            a += 1
        else:
            area_1 = lst[b] * (b - a)
            if area < area_1:
                area = area_1
            b -= 1
       
    print(area)
    return area

# max_area(test_1)
# max_area(test_2)
# max_area(test_3)
# max_area(test_4)
# max_area(test_5)
# max_area(test_6)
max_area(test_7)