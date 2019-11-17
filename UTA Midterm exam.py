#Midterm Exam





'''            
Write a function called find_integer_with_most_divisors that accepts a list of integers and
returns the integer from the list that has the most divisors. In case of a tie, return the first item that has the most divisors.
For example:

if the list is:

 [8, 12, 18, 6]
In this list, 8 has four divisors which are: [1,2,4,8] ;
12 has six divisors which are: [1,2,3,4,6,12];
18 has six divisors which are: [1,2,3,6,9,18] ;
and 6 has four divisors which are: [1,2,3,6].
Notice that both 12 and 18 are tied for maximum number of divisors (both have 6 divisors).
Your function should return the first item with maximum number of divisors;
so it should return:
12
 '''
def find_integer_with_most_divisors(inputList):
    #create two lists. 1st for temp list 2nd for permanent list
    temp_list = []
    perm_list = []

    # create two variables 1st for the temp integer. 2nd for the permanent integer
    temp = None
    perm = None

    #create a forp loop to loop through the input list and for each one loop that integer and find its divisors
    # then store its divisors in the temp list
    for ele in inputList:
        temp = ele
        for each in range(1, ele+1):
            if ele % each == 0:
                temp_list.append(each)
        if len(temp_list) > len(perm_list):
            perm_list = temp_list.copy()
            perm = temp
            temp_list.clear()
    return perm





# method 2 
def find_integer_with_most_divisors(inputList):
    #create a variable count to  count the number of divisiors 
    count = 0

    # create a variable to sotre the integer which the highest number of divisors
    perm = 0

    #create a forp loop to loop through the input list and for each one loop that integer and find its divisors
    # then add count += 1 then if count > perm change, perm to ele 
    for ele in inputList:
        temp = ele
        for each in range(1, ele+1):
            if ele % each == 0:
                count += 1
        if count > perm:
            perm = ele
    return perm

   
#method 3
def find_integer_with_most_divisors(inputList):
    #create two variable, 1 to  count the number of divisiors and 2 make a copy of count
    count = 0
    temp = 0

    # create a variable to sotre the integer which the highest number of divisors
    perm = 0

    #create a forp loop to loop through the input list and for each one loop that integer and find its divisors
    # then add count += 1 then if count > perm change, perm to ele 
    for ele in inputList:
        for each in range(1, ele+1):
            if ele % each == 0:
                count += 1
        if count > temp:
            perm = ele
            temp = count 
        count = 0 
    return perm





'''
Write a function named list_of_primes that accepts a positive integer n and
returns a sorted list (ascending order) of all the prime numbers between 2 and
n (including 2 but not including n)
'''

def list_of_prime(n):
    #create a boolean variable
    checkPrime = True
    # create an empty list
    returnList = []

    #for loop loop through n and find the prime from 2 to n
    for integer in range(2, n):
        if integer == 2:
            returnList.append(integer)
            continue
        for ele in range(2, integer):
            if integer % ele == 0:
                checkPrime = False 
                break
        if checkPrime:
            returnList.append(integer)
    return (sorted(returnList())     
        
#method 2

def list_of_prime(n):
    
    #create the check Prime function - return a boolean value
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
    
    # create an empty list
    returnList = []

    #for loop loop through n and find the prime from 2 to n
    for integer in range(2, n):
        if integer == 2:
            returnList.append(integer)
            continue
        else:
            if checkPrime(integer):
                returnList.append(integer)
        
    return (sorted(returnList())



'''
Write a function named items_price that accepts two lists as parameters.
The first list contains the quantities of n different items,
the second list contains the prices that correspond to those n items respectively.
Now, calculate the total amount of money required to purchase those items.
Assume that both the lists will have equal lengths.
For example if the input lists are:

a = [2, 3, 5, 7, 9]
This list (list a) gives you the quantity of each item.
b = [5, 8, 4, 1, 11]
This list (list b) gives you the per item price for each item corresponding to the first list (list a).
This means that if you want to purchase 2 units of the first item, each unit costs $5 per item,
to purchase the 3 units of second item it costs $8 per item ...
Now, your function should calculate and return the total price required to purchase all the quantities of all the items given to you.
The correct output for the lists above would be:
160

'''

def items_price(a, b):
    aSum = sum(list(map(lambda a, b: a * b, a, b)))
    return aSum

# alternative
################### Instructor function ###################
def _find_dot_product_sample_(a, b):
    result = 0
    for i in range(0, len(a)):
        result += a[i] * b[i]
    return result


'''
Write a function named crazy_list that accepts a list as parameter and
returns a boolean (either True or False) based on whether or not the list is the same forward and backwards.
You may NOT use list.reverse() method.

For example, if the list received by the function is:

[5, 6, 8, 9, 'PYTHON', 9, 8, 6, 5] 
(Notice how the list is exactly the same whethere you read it from left to right, or from right to left)
Then your function should return the Boolean
True 
however, if the list recieved by the function is something like this:
[4, 5, 6, 7, 8, 4, 5, 2] 
(Notice how the list is NOT the same when reading from left to right vs right to left)
In this case, your function should return the Boolean
False

'''
def crazy_list(some_list):
    # create a reserve empty list
    reverse = []

    #create a boolean  variable
    check = None 

    for ele in some_list[len(some_list)::-1]:
        reverse.append(ele)

    for i in range(len(reverse)):
        if some_list[i] != reverse[i]:
            return False
    return True
        
#alternative  answer from instructor
################### Instructor function ###################
def _test_list_palindrom_sample_ed2(some_list):
    size = len(some_list)
    if size % 2 == 0:
        # if the length is even
        mid = int(size / 2)
        first_half = some_list[0:mid]
        # get the second half and reverse it
        second_half = some_list[mid::][::-1]
    else:
        mid = int((size ) / 2)
         # get the first half
        first_half = some_list[0:mid]
        # get the second half and reverse it
        second_half = some_list[mid+1::][::-1]
    if first_half == second_half:
        return True
    else:
        return False

'''
Write a function called pattern_sum that receives two single digit positive integers,
(k and m) as parameters and calculates and returns the total sum as:
k + kk + kkk + .... (the last number in the sequence should have m digits)
For example, if the two integers are:

(4, 5)
Your function should return the total sum of:
4 + 44 + 444 + 4444 + 44444
Notice the last number in this sequence has 5 digits. The return value should be:
49380
if the two integers are:
(5, 3)
Your function should return the total sum of:
5 + 55 + 555
Notice the last numebr in this sequence has 3 digits. The return value should be:
615


'''
def pattern_sum(k, m):
    string = str(k)
    count = 0

    for i in range(1,m+1):
        count += int(i * string)
    return count

#alternative answer from instructor

################### Instructor function ###################
def _chain_of_number_sample_ed2_(a, b):
    chain_list = []
    my_sum = 0
    for x in range(1, b+1):
        chain_list.append(x*str(a))
    for items in chain_list:
        my_sum = my_sum + int(items)

    return my_sum


'''
Write a function named unique_common that accepts two lists both of which contain integers as parameters
and returns a sorted list (ascending order) which contains unique common elements from both the lists.
If there are no common elements between the two lists,
then your function should return the keyword None

For example, if two of the lists received by the function are:

([5, 6, -7, 8, 8, 9, 9, 10], [2, 4, 8, 8, 5, -7])
You can see that elements 5, -7, and 8 are common in both the first list and
the second list and that the element 8 occurs twice in both lists. Now you should return a sorted list (ascending order) of unique common elements like this:
[-7, 5, 8]
if the two lists received by the function are:
([5, 6, 7, 0], [3, 2, 3, 2])
Since, there are no common elements between the two lists,
your function should return the keyword
None

'''

def unique_common(a, b):
    store = []

    for i in a:
        for j in b:
            if i == j:
                if i in store:
                    continue
                else:
                    store.append(i)
    if not store:
        return None
    else:
        return(store.sort())

# alternative
def unique_common(a, b):
    store = []

    for i in a:
        if i in b:
            if i in store:
                continue 
            else:
                store.append(i)
    if not store:
        return None
    else:
        return(store.sort())


'''
Write a function named find_gcd that accepts a list of positive integers and returns their greatest common divisor (GCD). Your function should return 1 as the GCD if there are no common factors between the integers. Here are some examples:

if the list was

[12, 24, 6, 18]
then your function should return the GCD:
6
if the list was
[3, 5, 9, 11, 13]
then your function should return their GCD:
1

'''

def find_gcd(some_list):
    # create a two empty lists
    temp = []
    nest = []

    #create a variable to store the count and gcd
    count = 0

    # a for loop to loop through the input list and find divisors for each
    for item in some_list:
        for ele in range(1, item+1):
            if item % ele == 0:
                temp.append(ele)
    for item in temp:
        temp_count = 0
        temp_count = temp.count(item)
        if temp_count >= count:
            if item not in nest:
                nest.append(item)
            count = temp_count
    return max(nest)


'''
Write a program that asks the user to enter an integer between 1 and 9999 (both inclusive) and then prints the input integer using words. For example if the user enters:

3421
Then your program should print
three thousand four hundred twenty one
more examples:
Input	Printed Output
15	fifteen
7000	seven thousand
501	five hundred one
1008	one thousand eight
7	seven
Notes:
the words in the printed output should all be lower cased and separated by only one space
There is no "and" between the printed words.
Notice that when you use a print() statement, Python by default adds a new line after each printed output. If you do not want each new print statment to be printed in a new line then you should add end="" at the end of your print arguments as shown below:
print("seven ", end = "")
print("thousand")
This will print
seven thousand
Also when you use two arguments in a print statement, Python adds a space between them by default. For example:
print("x",5)
will print
x 5
If you do not want a space to be inserted between your arguments then you should add sep="" at the end of your print arguments as shown below:
print("x",5,sep="")
will print
x5
Make sure your words match the following spellings:
one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen,
sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty,
ninety, hundred, thousand

'''
user = (input("Please enter a number: "))
user_int = int(user)
str_num_list = []
for i in user:
    str_num_list.append(i)
word = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
'ninety', 'hundred', 'thousand']
numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000]
for i in range(len(str_num_list)):
    # thousands
    if len(str_num_list) - i == 4:  
        num_int = int(str_num_list[i])
        if num_int in numbers:
            index = numbers.index(num_int)
            print(word[index], word[-1], end=' ')
    # hundreds        
    if len(str_num_list) - i == 3:   
        num_int = int(str_num_list[i])
        if num_int == 0:
            continue
        elif num_int in numbers:
            index = numbers.index(num_int)
            print(word[index], word[-2], end=' ')
    # tens
    if len(str_num_list) - i == 2:
        already_added = False
        num_int = int(str_num_list[i])
        if num_int == 0:
            continue
        two_string = str_num_list[i] + str_num_list[-1]
        if int(two_string) in numbers:
            index = numbers.index(int(two_string))
            print(word[index], end=' ')
            already_added = True
            continue
        if num_int in numbers:
            two_string = str_num_list[i] + '0'
            int_two_string = int(two_string)
            if int_two_string in numbers:
                index = numbers.index(int_two_string)
                print(word[index], end=' ')
    # ones
    if len(str_num_list) - i == 1:
        num_int = int(str_num_list[i])
        if already_added:
            break
        else:
            if num_int not in numbers:
                continue
            elif num_int in numbers:
                index = numbers.index(num_int)
                print(word[index])
            


# instructor's answer

################### Instructor code ###################
n=int(input('please enter an integer between 1 and 9999: '))
one_to_ten=['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ten_to_nineteen=['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
'sixteen', 'seventeen', 'eighteen', 'nineteen']
twenty_to_ninety=['','','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
'ninety']
temp_str=""
if n==0:
    temp_str='zero'
    #print('zero')
first_digit=n//1000
second_digit=(n%1000)//100
third_digit=(n%100)//10
fourth_digit=(n%10)
if first_digit>0:
    temp_str=temp_str+one_to_ten[first_digit]+' thousand '
    #print (one_to_ten[first_digit],'thousand ',end='')
if second_digit>0:
    temp_str=temp_str+one_to_ten[second_digit]+' hundred '
    #print (one_to_ten[second_digit],'hundred ',end='')
if third_digit>1:
    temp_str=temp_str+twenty_to_ninety[third_digit]+" "
    #print (twenty_to_ninety[third_digit],'',end='')
if third_digit==1:
    temp_str=temp_str+ten_to_nineteen[fourth_digit]+" "
    #print (ten_to_nineteen[fourth_digit],'',end='')
else:
    if fourth_digit:
        temp_str=temp_str+one_to_ten[fourth_digit]+" "
        #print (one_to_ten[fourth_digit],'',end='')
if temp_str[-1]==" ":
    temp_str=temp_str[0:-1]
print (temp_str)

