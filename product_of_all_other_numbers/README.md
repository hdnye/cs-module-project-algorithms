# Product of All Other Numbers

Write a function that receives an array of integers and returns an array consisting of the product of all numbers in the array _except_ the number at that index. 

For example, given 
```
[1, 7, 3, 4]
```
your function should return 
```
[84, 12, 28, 21]
``` 
by calculating 
```
[7*3*4, 1*3*4, 1*7*4, 1*7*3]
```

In the above example, the final value at index 0 is the product of every number in the input array _except_ the number at index 0.

Can you do this in `O(n)` time with `O(n)` space _without_ using division?

## Testing
Run the test file by executing `python test_product_of_all_other_numbers.py`.

# Understand
# -- return an array that is the sum of all the numbers in the array 
# -- except at the index it's iterating over

# Plan
# Want to find the product of all integers except one
# -- need an empty array to store the products in
# -- Iterate through the list (recursive?)
#   -- find base case
#   -- need to multiply ints around current index
# -- How do we determine which is the integer & what's to be multiplied?
#   -- split arr in 2: left side of the cur_int & right side of the cur_int


