# UTA Week 9 Namespaces and Scope of Variables

#Exercises


'''
Write a function named calculate_fibonacci that receives a positive integer 'n' as parameter and calculates and returns the nth fibonacci number using recursion.

Notes

Fibonacci numbers are the numbers in the sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
The 0th Fibonacci number is 0, the 1st Fibonacci number is 1.
All other numbers are sum of the previous two numbers.
For example, when your function is called as:
calculate_fibonacci(10)
Then, your function should return the 10th fibonacci number:
55
'''
def calculate_fibonacci(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1 
    return(calculate_fibonacci(n-1) + calculate_fibonacci(n-2))


'''
Write a function named calculate_factorial that receives a positive integer 'n' as parameter and calculates and returns the factorial of n using recursion.

Notes

Factorial is the product of an integer with all the integers below it. For example, the factorial of 5 is 5*4*3*2*1 = 120. Note that the factorial of both 0 and 1 is 1. For example, when your function is called as:

calculate_factorial(10)
Then, your function should return the number:
3628800
'''

def calculate_factorial(n):
    if n ==0 or n == 1:
        return 1
    return(calculate_factorial(n-1)*n)




'''
Write a function named calculate_exponent that receives two positive integers a and b as parameter and calculates and returns a to the power of b using recursion. For example, when your function is called as:

calculate_exponent(5, 3)
Then, your function should return:
125
'''

def calculate_exponent(a, b):
    if a == 1:
        return 1 
    if b == 0:
        return 1
    elif b == 1:
        return a
    return (calculate_exponent(a, b-1)*a)



'''
Write a function named calculate_gcd that receives two positive integers a and b as parameter and returns their greatest common divisor (GCD) using recursion.

For example, when your function is called as:

calculate_gcd(10, 15)
Your function should return:
5

'''

def calculate_gcd(a, b):
        
    if a%b == 0:
        return b%a
    return(calculate_gcd(b, a%b))


'''
Write a function named nested_list_sum that receives a nested list of integers as parameter and calculates and returns the total sum of the integers in the list using recursion. Keep in mind that the inner elements may be integers or other nested lists themselves.

For example, when your function is called as:

nested_list_sum([1, -1, [2, -2], [3, -3, [4, -4], 10]])
Then, your function should return the total sum as
10
'''

def nested_list_sum(sample_list):
    my_sum = 0
    for element in sample_list:
        if type(element) != type([]):
            my_sum += element
        else :
            my_sum += _recursive_sum_sample_(element)
    return my_sum




'''
Write a program that asks the user for an input and
tries to handle the error that may occur when you try to type cast
the input to an int using the try ... except ... else clause.
Your function should print the result if the operation is successful,
if the operation is not successful your program should print 'Error'
'''



def try_error(user_input):
    try:
        int_input = int(user_input)
    except:
        print ("Error")
    else:
        print (int_input)

user = input("Please enter a word you want: ")
try_error(user)


'''
You are trying to modify the content of a list
and you need to write a function to perform the task.
The function takes three arguments. The first argument is the list itself,
the second argument is an index 'n' and the third argument is a string.
Your job is to set the 'n'th (index) item of the list as the given string
and return the modified list if successful.
In case of a failure your function should return the original list.
Write a function that performs this task using the try...except...else statements.
'''

def modify_list(lst, n, str1):
    try:
        if n <= len(lst):
            lst.insert(n, str1)
            if n >= 0:
                lst.pop(n+1)
            else:
                lst.pop(n)
        
    except:
        return lst
    else: 
        return lst


'''
You are trying to divide two numbers and
you need to write a function to perform the task.
The function takes two arguments. The first argument is a float
but you are unsure about the second argument
(there is a chance that the second argument could be a zero).
Write a function that takes a float and an unknown input and
tries to handle the error when you try to divide the float by the unknown input using the try..except..else clause. The unknown input could be either an integer or a string or a float. If the operation fails your function should return the value None (exactly without the quotes),
If successful your function should return the result.
'''

def unknown(arg1, arg2):
    try:
        result = arg1 /arg2 
    except(ArithmeticError, TypeError):
        return None 
    else:
        return result




'''
You are trying to concatenate two strings and
you need to write a function to perform the task.
The function takes two arguments.
You do not know the type of the first argument in advance
but the second argument is certainly a string.
Write a function that takes an unknown input and a string as input
and tries to handle the error when you try to concatenate this unknown input to the string using the try..except..else clause. The unknown input could be either an integer or a string or a float. If the concatenation fails your function should return the value None (exactly without the quotes), If successful your function should return the resulting string.

'''

def unknown(arg1, arg2):
    try:
        concatenate_string = arg1 + arg2 
    except (TypeError):
        return None
    else:
        return concatenate_string 
