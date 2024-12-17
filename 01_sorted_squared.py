def sorted_squared(array):
    # Create an array to hold the squared values, the same length as the input
    squared = [0] * len(array)
    
    # Initialize two pointers
    left, right = 0, len(array) - 1
    index = len(array) - 1
    
    # Traverse the array from both ends
    while left <= right:
        left_squared = array[left] * array[left]
        right_squared = array[right] * array[right]
        
        # Compare the squares and place the larger one at the current index
        if left_squared > right_squared:
            squared[index] = left_squared
            left += 1
        else:
            squared[index] = right_squared
            right -= 1
        
        # Move the index to the left
        index -= 1
    
    return squared

test_1 = [-4,-2,1,0,3]
test_2 = []