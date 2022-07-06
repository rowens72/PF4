# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
    return max(a, b, c)

# Write a Python function called mult_list() to multiply all the numbers in a list.
def  mult_list(myList):
    # make sure list has soemthing in it
    if len(myList) == 0:
        return 0

    value = myList[0]
    # loop through list and multiply numbers
    if len(myList) > 1:
        for x in myList[1:]:
            value = value * x
    return value
            
    
# Write a Python function called rev_string() to reverse a string.
def rev_string(myString): 
    # will throw error with empty string "RecursionError: maximum recursion depth exceeded"
    if myString == "":
        return myString
    else:
        return rev_string(myString[1:]) + myString[:1]

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, bseginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(a, b, c):
    return a in range(b, c + 1) 


# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. 
# Each number is the two numbers above it added together.
# I had to look this up online as  I am not very good at the math.
def pascal(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1




# call functions above
# 1
print('max_num: ', max_num(1, 6, 3))

# 2
print('mult_list: ', mult_list([1, 2, 3, 4]))
print('mult_list: ', mult_list([]))

# 3
print('rev_string : ', rev_string('Python function'))
print('rev_string : ', rev_string(''))

# 4
print('num_within: ', num_within(3,2,4))
print('num_within: ', num_within(3,1,3))
print('num_within: ', num_within(10,2,5))

# 5
pascal(6) 