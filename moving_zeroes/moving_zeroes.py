'''
Input: a List of integers
Returns: a List of integers
'''
# First Pass Solution

# def moving_zeroes(arr):
#     for i in arr:
#         if i == 0:
#             arr.append(arr.pop(0))
#         elif i != 0:
#             arr.insert(0, i)
#         return arr

# Write Better Solution

def moving_zeroes(arr):
    lhs = 0
    rhs = len(arr) - 1

    while lhs <= rhs:
        # lhs iterates through until hits 0
        if arr[lhs] != 0:
            lhs += 1
            continue
        # rhs iterates throug until no 0
        if arr[rhs] == 0:
            rhs -= 1
            continue  

        arr[lhs], arr[rhs] = arr[rhs], arr[lhs]

    return arr

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
