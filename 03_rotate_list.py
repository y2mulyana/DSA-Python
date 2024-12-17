def rotate_array(array,k):
    if len(array) == 0:
        return array
    elif k == 0 or k % len(array) == 0:
        print(array)
        return array
    
    else:
        rotation = k % len(array) 
        print(array[-rotation:] + array[:len(array)-rotation])
        return (array[-rotation:] + array[:len(array)-rotation])
           
test_1 = rotate_array([1,2,3,4], 0)