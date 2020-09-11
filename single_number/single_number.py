'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # create new arr for single value
    single_value = []
    # Iterate over original arr
    for i in arr:
        # it does exist in new arr
        # remove from arr
        if i in single_value:
            single_value.remove(i)
        # if it doesn't exist in new arr:
        # add to new arr
        else: 
            single_value.append(i)

    return single_value[0]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")


# Understand
# -- Find the single # in the arr
# -- Return the single #

# Plan
# -- Create new arr for single values
# -- Iterate through original arr & compare 
# -- Should end with single el in arr at end
