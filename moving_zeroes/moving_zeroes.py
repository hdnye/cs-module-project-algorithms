'''
Input: a List of integers
Returns: a List of integers
'''
# def moving_zeroes(arr):
#     # Your code here
#     # For loop to iterate through arr
#     for i in arr:
#         if i > 0:
#             arr.append(i)
#         else: 
#             arr.pop(0)
#     return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")


# Understand
# -- All 0s in an arr need to be moved to the rhs

# Plan
# -- Iterate through arr & find the 0s
# -- move the 0's to the rhs of all integers
# -- return altered arr