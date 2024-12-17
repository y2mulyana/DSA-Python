# test_7 = [1, 2, 1] # bukan monotonic
# test_8 = [3, 2, 4, 3] # bukan monotonic
# test_9 = [8, 3, 9, 2, 6, 7, 1, 4] # bukan monotonic

def is_monotonic(s):
    check = []
    if len(s) == 0 or len(s)== 1:
        check.append('i')
    else:
        for num in range(len(s)-1):
            if s[num+1] > s[num]:
                check.append('i')
            elif s[num+1] < s[num]:
                check.append('d')
    if 'i' in check and 'd' in check:
        print(f'Non monotonic = {check}')
        return False
    else:
        print(f'monotonic = {check}')
        return True
            
def test_is_monotonic():
    # Test case 1: Empty list
    assert is_monotonic([]) == True, "Test Case 1 Failed"

    # Test case 2: Single element list (monotonic by default)
    assert is_monotonic([5]) == True, "Test Case 2 Failed"

    # Test case 3: List is strictly increasing
    assert is_monotonic([1, 2, 3, 4, 5]) == True, "Test Case 3 Failed"

    # Test case 4: List is strictly decreasing
    assert is_monotonic([5, 4, 3, 2, 1]) == True, "Test Case 4 Failed"

    # Test case 5: List has equal elements (non-decreasing and non-increasing)
    assert is_monotonic([3, 3, 3, 3]) == True, "Test Case 5 Failed"

    # Test case 6: List is non-decreasing
    assert is_monotonic([1, 2, 2, 3, 4]) == True, "Test Case 6 Failed"

    # Test case 7: List is non-increasing
    assert is_monotonic([5, 5, 4, 3, 2]) == True, "Test Case 7 Failed"

    # Test case 8: List is neither increasing nor decreasing (zigzag pattern)
    assert is_monotonic([1, 3, 2, 4, 3]) == False, "Test Case 8 Failed"

    # Test case 9: List with negative numbers that is increasing
    assert is_monotonic([-5, -4, -3, -2, -1]) == True, "Test Case 9 Failed"

    # Test case 10: List with mixed positive and negative numbers (decreasing)
    assert is_monotonic([3, 0, -1, -2, -5]) == True, "Test Case 10 Failed"
    
    # Test case 11: Non monotonic
    assert is_monotonic([3, 2, 4, 3]) == False, "Test Case 11 Failed"
    
    # Test case 12: Non monotonic
    assert is_monotonic([2, 3, 3, 2]) == False, "Test Case 12 Failed"

    print("All test cases passed!")

# Run the test
test_is_monotonic()

    