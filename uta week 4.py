 # Week 4  Functions, Modules, Loops and Nested Loops
'''
Write a function which accepts an input list of numbers and returns the largest number in the list (Do not use python's built-in max() function).

'''

def maxOflist(my_list):
    maxValue = my_list[0]
    
    for i in my_list[1:]:
        if maxValue > i:
            my_list = my_list[(my_list.index(i)+1):] 
        else:
            maxValue = i
        
    return maxValue


'''
Write a function that accepts a list of integers and returns the average. Assume that the input list contains only numbers. Do NOT use the built-in sum() function.

'''
def averageOfList(my_list):
    average = 0 
    sum1 = 0
    for i in my_list:
        sum1 += i 
    average = sum1/ len(my_list)
    return average

'''
Write a function which accepts an input list of numbers and returns the smallest number in the list (Do not use python's built-in min() function).

'''
def minOflist(my_list):
    minValue = my_list[0]
    for i in my_list[1:]:
        if minValue < i:
            my_list = my_list[(my_list.index(i)+1):]
        else:
            minValue = i 
    return minValue


'''
Write a function that finds the magnitude of a given vector. The magnitude of a vector is the square root of sum of squares of all the components of the vector. Your input for this function will be a (vector with x,y,z components) 1 dimensional list containing 3 integers. For example if the input list is:

vector = [2, 3, -4]
Then you should return the magnitude (as a floating point number) of this vector:
5.385164807134504
'''
import math
def mag_vector(my_list):
    sum1 = 0
    for i in my_list:
        sum1 += pow(i, 2)
    
    return math.sqrt(sum1)


'''
Write a function that normalizes a vector (finds the unit vector). A vector can be normalized by dividing each individual component of the vector by its magnitude. Your input for this function will be a vector i.e. 1 dimensional list containing 3 integers. For example if the input list is:

vector = [2, 3, -4]
Then you should return the unit vector(1-Dimensional list) such as:
[0.3713906763541037, 0.5570860145311556, -0.7427813527082074]
'''

import math
def mag_vector(my_list):
    sum1 = 0
    for i in my_list:
        sum1 += pow(i, 2)
    
    return [(my_list[0] / math.sqrt(sum1)), (my_list[1] / math.sqrt(sum1)), (my_list[2] / math.sqrt(sum1))]



'''
Python Modules Exercise 1 (Evaluate Trigonometric Expression)
Write a function that accepts a number  x  and evaluates the following expression:

y=sin(x)−cos(x)+sin(x)cos(x) 
and returns the value of y. (Hint: Use math module)
'''


from math import *
def trig(x):
    
    return ((sin(x)) - (cos(x)) + ((sin(x))*(cos(x))))


'''
Python Modules Exercise 2 (Evaluate Expression)
Write a function that accepts a number  x  and evaluates the following expression:

y=abs(x3)+cos(3x−−√) 
and returns the value of y. Hint: Use the math module!

'''
from math import *
def exp(x):
    
    return abs((pow(x, 3))) + cos (pow((3*x), 0.5))
    



'''
Python Modules Exercise 3 (Find Distance between two points)
Write a function that finds the distance between two points and returns it. The distance between two points with x,y, and z components can be calculated as:

distance=(x2−x1)2+(y2−y1)2+(z2−z1)2−−−−−−−−−−−−−−−−−−−−−−−−−−−−√ The input for this function will be two 1 Dimensional lists that contain the x,y,z coordinates each. For example if the input lists are:
a = [2, 3, -5] 
b = [4, -3, 12]
Then your function should return their distance such as:
18.138357147217054
Hint: You may use the math module!

'''
# Type your code here
def distance(list1, list2):
    # the variables assigned to elements in list1
    a = list1[0]
    b = list1[1]
    c = list1[2]
    
    # the variables assigned to elements in list1
    
    d = list2[0]
    e = list2[1]
    f = list2[2]
    
    # calculate the distance 
    dis =  pow((pow((a - d), 2) + pow((b - e), 2) + pow((c - f), 2)), 0.5)
    return dis





# Assignments for week 4


'''
Write a function that calculates and returns the monthly payments for a loan. This function accepts three parameters in the exact order (principal, annual_interest_rate, duration):

principal: The total amount of loan. Assume that the principal is a positive floating point number.
annual_interest_rate: This is the percent interest rate per year. Assume that annual_interest_rate is a floating point number. (Notice that 4.5 means that the interest rate is 4.5 percent per year.)
duration: number of years to pay the loan back. Assume that duration is a positive integer.
To calculate the amount of monthly payment for the loan you should use the following equation

MonthlyPayment=Principal∗r(1+r)n(1+r)n−1 
Where:

r is the monthly interest rate (should be calculated by first dividing the annual_interest_rate by 100 and then divide the result by 12 to make it monthly). Notice that if the interest rate is equal to zero then the above equation will give you a ZeroDivisionError. In that case you should use the follwing equation: MonthlyPayment=Principaln 
n is the total number of monthly payments for the entire duration of the loan (Notice that n is equal to loan duration in years multiplied by 12).
Your function should return the monthly payment as a floating point number.

Example: if your function is called with the following parameters:

(1000.0,4.5,5)
Then it should return a floating point number:
18.643019241516996
Remember that you are not asked to print anything. So, your function should just return the monthly payments. You do not need to call your function, it will automatically be called and tested for correctness with the test cases we provide. You only need to write one function and we will test your program with the first function that appears in your code. So, if you want to write more than one function to help you solve the problem remember to embed the helper functions inside the first function.

'''

def monthPayment(principal, annual_interest_rate, duration):
    monthly_interest_rate = ((annual_interest_rate) / 100) / 12.0
    n = duration * 12
    e = (1 + monthly_interest_rate)**n
    if annual_interest_rate == 0:
        return (principal / n)
    else:
         monthlyPayment = principal * ((monthly_interest_rate * e) / (e -1))
    return monthlyPayment


print(monthPayment(1000.0, 0, 5))



# Part 2: Calculate the remaining balance of a loan
'''

Write a function that calculates and returns the remaining loan balance. This function accepts four parameters in the exact order shown below:

(principal, annual_interest_rate, duration , number_of_payments)
principal: The total amount of loan. Assume that the principal is positive floating point number.
annual_interest_rate: This is the percent interest rate per year. Assume that annual_interest_rate is a floating point number. (Notice that 4.5 means that the interest rate is 4.5 percent per year.)
duration: number of years to pay the loan back. Assume that duration is a positive integer.
number_of_payments: number of monthly payments that are already paid. Assume that number_of_payments is an integer.
To calculate the reamining loan balance use the following equation

RemainingLoanBalance=Principal∗(1+r)n−(1+r)p(1+r)n−1 
Where:

r is the monthly interest rate. r should be calculated by first dividing the annual_interest_rate by 100 and then divide the result by 12 to make it monthly. Notice that if the interest rate is equal to zero then the above equation will give you a ZeroDivisionError. In that case you should use the follwing equation:  RemainingLoanBalance=Principal(1−pn) 
n is the total number of monthly payments for the entire duration of the loan. Notice that n is equal to loan duration in years multiplied by 12.
p is the number of payments which are already made.
Your function should return the remaining balance as a floating point number.

Example: if your function is called with the following parameters:

(1000.0,4.5,5,12)
Then it should return a floating point number:
817.5512804582867
Remember that you are not asked to print anything.
So, your function should just return the resulting remaining balance.
You do not need to call your function,
it will automatically be called and tested for correctness with the test cases we provide.
You only need to write one function and
we will test your program with the first function that appears in your code.
So, if you want to write more than one function to help you solve the problem remember to embed the helper function(s) inside the first function.
'''

def remainPayment(principal, annual_interest_rate, duration, number_of_payments):
    n = duration * 12
    r = (annual_interest_rate / 100.0) / 12.0
    if annual_interest_rate == 0:
        remainBalance = principal *( 1 - (number_of_payments / n))
    else:
        remainBalance = principal * (((1 + r)**n - (1 + r)**number_of_payments) / ((1 + r)**n - 1))

    return remainBalance

print(remainPayment(1000.0, 4.5, 5, 12))

        

'''
Write a program for loan calculations. Your program should ask the user for three pieces of information (with three seperate input() functions:)

Total amount of loan.
Annual interest rate. (Assume that the interest rate is a positive integer. For example 5 means that annual interest is 5% (five percent) per year.
Total duration of loan in years.
Your Program should use the two functions that you implented in part 1 and 2 of this exercise and display the follwoing information about the loan.

In the first first line show the amount of loan and interest rate.
In the second line show duration of the loan and monthly payment.
In each of the following lines show the Loan balance and total amount paid for each year.
Example 1: assuming that user inputs the following numbers in response to your questions:

Enter loan amount: 1000.0
Enter annual interest rate (percent): 10.0
Enter loan duration in years: 5
The output of your program should be:

LOAN AMOUNT: 1000 INTEREST RATE (PERCENT): 10
DURATION (YEARS): 5 MONTHLY PAYMENT: 21
YEAR: 1 BALANCE: 837 TOTAL PAYMENT 254
YEAR: 2 BALANCE: 658 TOTAL PAYMENT 509
YEAR: 3 BALANCE: 460 TOTAL PAYMENT 764
YEAR: 4 BALANCE: 241 TOTAL PAYMENT 1019
YEAR: 5 BALANCE: 0 TOTAL PAYMENT 1274

'''

def displayLoan(loan, annual_interest_rate, duration):
    print("LOAN AMOUNT:", int(loan), end= ' ')
    print("INTEREST RATE (PERCENT):", int(annual_interest_rate))
    print("DURATION (YEARS):", duration, end=' ')
    print("MONTHLY PAYMENT:", int(monthPayment(loan, annual_interest_rate, duration)))


    current = None
    current_total = None
    

    for each_year in range(duration):
        YEAR = each_year + 1
        BALANCE = (remainPayment(principal, annual_interest_rate, duration, ((each_year + 1) * 12)))
        MONTH = ((each_year + 1)* 12 ) * (monthPayment(principal, annual_interest_rate, duration))

        print("YEAR:", YEAR, "BALANCE:", int(BALANCE), "MONTHLY PAYMENT:", int(MONTH))


              
        
          
    
    

        
    


principal = float(input("Enter loan amount: "))
annual_interest_rate = float(input("Enter annual interest rate: "))
duration = int(input("Enter loan duration in years: "))

displayLoan(principal, annual_interest_rate, duration)




#Quiz for week 4


'''
Write a program that asks the user for a positive number 'n' as input. Assume that the user enters a number greater than or equal to 3 and print a triangle as described below. For example if the user enters 6 then the output should be:

*
**
***
****
*****
******
*****
****
***
**
*
Note that, there should be no spaces between the asterisks (*))
'''

user = int(input("Enter a number: "))
for i in range(0, user+1):
    print(i * '*')
for i in range(user-1, 0, -1):
    print(i * '*')



'''
Write a function that accepts a list of integers as parameter. Your function should return the sum of all the odd numbers in the list. If there are no odd numbers in the list, your function should return 0 as the sum.

Remember that you are not asked to print anything.
So, your function should just return the sum of all the odd numbers in the list. You do not need to call your function,
it will automatically be called and tested for correctness with the test cases we provide.
You only need to write one function and we will test your program with the first function that appears in your code.
So, if you want to write more than one function to help you solve the problem, remember to embed the helper functions inside the first function.

'''

def sumOdd(list1):
    list2 = []
    for each in list1:
        if each % 2 != 0:
            list2.append(each)
    if len(list2) == 0:
        return 0
    else:
        return (sum(list2))

################### Sample Solution ###################
def _sum_of_odds_sampleX_(my_list):
    my_sum = 0
    for items in my_list:
        if items % 2 != 0:
            my_sum = my_sum + items
    return my_sum


'''
Write a function that receives a positive integer as function parameter and returns True
if the integer is a perfect number, False otherwise.
A perfect number is a number whose sum of the all the divisors (excluding itself) is equal to itself.
For example: divisors of 6 (excluding 6 are) : 1, 2, 3 and their sum is 1+2+3 = 6.
Therefore, 6 is a perfect number.

Remember, that you are not asked to print anything.
So, your function should return either True or False.
You do not need to call your function,
it will automatically be called and tested for correctness with the test cases we provide.
You only need to write one function and we will test your program with the first function that appears in your code.
So, if you want to write more than one function to help you solve the problem,
remember to embed the helper functions inside the first function.

'''

def checkPerfectnumber(n):
    numList = []
    for num in range(1, n):
        if n %  num == 0:
            numList.append(num)
    if sum(numList) == n:
        return True
    else:
        return False

print(checkPerfectnumber(6))


'''
Write a function that accepts a positive integer n as function parameter
and returns True if n is a prime number, False otherwise.
Note that zero and one are not prime numbers and
two is the only prime number that is even.

Remember that you are not asked to print anything.
So, your function should return either True or False and not print it.
You do not need to call your function, it will automatically be called
and tested for correctness with the test cases we provide.
You only need to write one function and
we will test your program with the first function that appears in your code. So, if you want to write more than one function to help you solve the problem remember to embed the helper functions inside the first function.

'''
def checkPrime(n):
    check_Prime = True 
    if n < 2:
        check_Prime = False
        return check_Prime
    
    for num in range(2, n):
        if n % num == 0:
            check_Prime = False
            return check_Prime
    return check_Prime



'''
Write a function that accepts two positive integers as function parameters
and returns their least common multiple (LCM).
The LCM of two integers a and b is the smallest (non zero) positive integer that is divisible by both a and b.
For example, the LCM of 4 and 6 is 12, the LCM of 10 and 5 is 10.

Remember that you are not asked to print anything.
So, your function should return the LCM and not print it.
You do not need to call your function, it will automatically be called
and tested for correctness with the test cases we provide.
You only need to write one function
and we will test your program with the first function that appears in your code.
So, if you want to write more than one function to help you solve the problem,
remember to embed the helper functions inside the first function.
'''

def LCM(a, b):
    # first make a backup/copy of a
    copy_of_a = a
    # While the remainder when a is divided by b is not 0
    # continue to add a to its backup (copy_of_a)
    while (copy_of_a % b) != 0:
        copy_of_a = copy_of_a + a
    return copy_of_a



'''
Write a function that accepts two positive integers as parameters.
The first integer is the number of heads and the second integer is the number of legs of all the creatures in a farm which consists of chickens and dogs.
Your function should calculate and return the number of chickens and number of dogs in the farm in a list as specified below.
If it is impossible to determine the correct number of chickens and dogs with the given information then your function should return None.
Example 1, if your function received the following numbers:

5, 12 
This means that someone has counted a total of 5 heads and total of 12 legs in the farm.
Now, your function should calculate how many chickens and how many dogs are in the farm and return that information in a list exactly as shown below.
[4, 1] 
this means that there were 4 chickens and 1 dog in the farm.

Example 2, if your function received the following numbers:
7, 12 
Then it should return:
None 


Remember that you are not asked to print anything.
So, your function should return a list that contains two numbers exactly in this order [number_of_chickens, number_of_dogs] not print it.
You do not need to call your function, it will automatically be called and tested for correctness with the test cases we provide.
You only need to write one function and we will test your program with the first function that appears in your code.
So, if you want to write more than one function to help you solve the problem remember to embed the helper functions inside the first function.
'''

def chicken_dog(n,m):
    # copy the integers
    heads = n
    legs = m
    # create variables to count the number of chickens and dogs
    dogs = 0
    chicken = 0
    if heads == 0 or legs == 0 :
        return None 
    if (heads == 1):
        if legs % 2 != 0 or legs > 4:
            return None
        
    copy_heads = heads
    for i in range(copy_heads):
        legs -= 2
        chicken += 1
        heads -= 1
        if int(legs / heads) == 4: 
            dogs = heads
            return ([chicken, dogs])
        if heads > legs:
            return None
    return([chicken, dogs])


        
                
            
 # the answer        
    def _sample_fun_puzzle_ (heads,legs):
    dogs=(legs-heads*2)/2
    if dogs<0 or dogs%1:
        return None
    dogs=int(dogs)
    chickens=heads-dogs
    if chickens< 0:
        return None
    return [chickens,dogs]



