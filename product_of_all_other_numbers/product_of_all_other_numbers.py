'''
Input: a List of integers
Returns: a List of integers
'''

# First Pass Solution
# def product_of_all_other_numbers(arr):
#     # Your code here
#     # empty lists to hold values
#     lhs = [0]  
#     rhs = len(arr) -1 
 
#     # for loop to find products left of current index
#     for i in arr:
#         # base case
#         if i == 0:
#             return False
#         lhs[i] = lhs[i - 1] * arr[i -1]
#         rhs[i] = rhs[i + 1] * arr[i + 1]    
#     return arr[lhs + rhs]
    

# Write Better Solution
def product_of_all_other_numbers(arr):
    # var to arr
    length = len(arr)
    # arr to hold answers
    solution = [0] * length

    # arr to hold product of lhs
    solution[0] = 1
    # for loop to find lhs values
    for i in range(1, length):
        solution[i] = arr[i - 1] * solution[i - 1]
    # var to hold values to right of i
    # for the el at i 'len - 1', no el's the the right(end) so rhs = 1 
    rhs = 1
    for i in reversed(range(length)):
        solution[i] = solution[i] * rhs
        rhs *= arr[i]
    return solution


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
