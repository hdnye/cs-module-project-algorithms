# We'll say that a positive int divides itself if every digit in the number divides into the number evenly.
# So, for example, 128 divides itself since 1, 2, & 8 all divide into 128 evenly
# And we'll say that 0 does not divid into anything evenly , so no number with a digit 0 divides itself

# Write a function to determine if a number divides itself

def divide_self(num):
    pass
    # Make an original copy of num    
    # Loop over each input int in num:
    while num > 0:
    # -- if the digit is 0, return False
        if num % 10 == 0:
            return False
    # -- get right most digit using % 10
        rightmost = num % 10
    # -- divide isolated # & divide by original imput
    # -- if remainder != 0, else return false
        if num // rightmost != 0:
            return num   
    # -- remove last digit from # w/ int division (//) 
        new_rm = rightmost // 10
    # -- check next digit 
        if num % new_rm != 0:
            return True
    # once loop is complete, return True
    return True

print(divide_self(128)) # --> True
print(divide_self(130)) # --> False

# Understand the problem (gather information)
#   Any f() has an input & a desired output
#   What's the Input?
#   -- A number
#   -- Positive integer 
#   -- How large? 
#   -- 0-case?
#       -- return false
#   -- check if it's an int or can we get bad data? 
#       -- no bad data
#   What's the type of ouput? <-- here 'Determine' hints at true/false stmt
#   -- Boolean

# Plan how to solve the problem
#   Planning & coding at the same time is a shit idea, stop doing it
#   Can use chunks of code to verify information but don't need to end up in the solution
#   Start with pseudocode to flesh out the probelem & direct where you want your code to go
#   -- to divide evenly (modulo operator takes 1 num % the other & returns the remainder of a/b)
#   -- So n % 2 == 0
#   -- "Every" implies needing an iteration/loop
#   -- If stmts to check edge cases: n % 2 != 0: return  False
#   -- How to get ind'l digit in num
#       -- could convert to string or list
#       -- isolate each digit. 
#       -- remove each digit after running through the loop



# Execute the plan

# Reflect
