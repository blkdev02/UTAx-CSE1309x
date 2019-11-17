# UTA Week 5 (List Manipulation, List Sliciing, List Sliciing with Steps and List Exercises)

#Exercises

'''
Write a function that accepts a positive integer k and returns a list that contains the first five multiples of k. The multiples should be calculated starting from 1 to 5 (including both 1 and 5). For example the first five multiples of 3 are 3, 6, 9, 12, and 15'
'''
def multiples(x):
    myList = list()
    for i in range (1, 6):
        a = i * x 
        myList.append(a)
    return myList

'''
Write a function that accepts two positive integers a and b (a is smaller than b)and returns a list that contains all the odd numbers between a and b (including a and including b if applicable) in descending order.
'''
def odd(a, b):
    myList = list()
    
    for i in range(a, b+1):
        if i % 2 != 0:
            myList.append(i)
    myList.sort(reverse = True)
    return myList

'''
Write a function that accepts a positive integer k and returns the ascending sorted list of cube root values of all the numbers from 1 to k (including 1 and not including k). [if k is 1, your program should return an empty list]
'''
def cube(k):
    myList = list()
    
    if k ==1: 
        return myList
    
    for i in range(1, k):
        a = pow(i, 1/3)
        myList.append(a)
    return myList


'''
Write a function that accepts a positive integer k and returns the list of all the divisors of k. Your list should include both 1 and k.

'''

def divisors(k):
    myList =[]
    for i in range(1, k + 1):
        if k % i == 0: 
            myList.append(i)
    return myList


'''
Write a function that accepts a list as input and returns a new list which includes every other element in the original list. Keep the first element, i.e. input_list[0]. For example if:

input_list = ["we", "love", "python", "so","much"]
then your function should return a list such as:
['we', 'python', 'much']

'''

def exe(myList):
    list1 = []
    x = 0
    list1.append(myList[0])
    for i in range(2, len(myList)):
        if i % 2 == 0:
    
            list1.append(myList[i])
    return list1


'''
Write a function that accepts a list (which has a length of 4 or more) and a string and returns the list such that the second through the fourth element (index 1 through 3 both inclusive) in the input list are replaced by the input string. For example:

input_list = ["Isha", "Chandoygya", "Sri Vasya", "Mandukya", "Sri"]
input_string = "Brahman" 
Then, your function should return a list such as:
['Isha', 'Brahman', 'Brahman', 'Brahman', 'Sri']

'''

def  man( list1, str):
    x = 0 
    del list1[1:4]
    a = 1
    while x <= 2: 
        list1.insert(a, str)
        a += 1 
        x += 1
    return list1

'''
Write a function that accepts two lists A and B and returns a new list which contains all the elements of list A followed by elements of list B. Notice that the behaviour of this function is different from list.extend() method because the list.extend() method extends the list in place, but here you are asked to create a new list and return it. Your function should not return the original lists. For example if the input lists are:

A = ['p', 'q', 6, 'k']
B = [8, 10]
Then your function should return a list such as:
['p', 'q', 6, 'k', 8, 10]
'''
def man2(A, B):
    a = A 
    for i in B:
        a.append(i)
        
    return a

'''
Write a function that accepts two lists both of which contain integers and returns a new list which contains all the elements from both lists sorted in descending order. Your new list should include duplicate elements if they exist. Do NOT use the built in sort() or sorted() methods.


     
'''
def sort1 (lst, lst1):
    mycopy = lst[:]
    mycopy.extend(lst1)
    for j in range(1, len(mycopy)):
        for i in range(0, len(mycopy)-1):
            if mycopy[i] < mycopy[i+1]:
                temp = mycopy[i]
                mycopy[i] = mycopy[i+1]
                mycopy[i+1] = temp 
        
    return mycopy 
    
'''
Write a function that accepts a list and a value of an element and returns the count of how many times that element appears in the list. The behaviour of this function should be exactly like the list.count() method. You may NOT use any built in list methods for this problem.


'''
def exe (lst, let):
    mycopy = lst[:]
    count1 = 0
    for i in mycopy: 
        if i == let: 
            count1 += 1
    return count1 



'''
Write a function that accepts a list and return a new list which contains all but the first and last elements of the original list.

'''
def exe(lst):
    mycopy = lst[1:-1]
    
    return mycopy


'''
Write a function that accepts a list that contains positive integers and returns a new list which contains all the elements from original list but adds 1 to those elements which are odd. For example if :

input_list = [12, 3, 4, 5, 6]
Then your function should return a list such as:
[12, 4, 4, 6, 6]
'''
def exe(lst):
    lst1 = []
    for i in lst:
        if i % 2 == 0:
            lst1.append(i)
        elif i % 2 != 0:
            lst1.append(i+1)
    return lst1


'''
Write a function that accepts two lists both of which consists of integers and returns the total sum of all the odd integers from both lists.


'''
def exe(lst, lst1):
    sum1 = 0 
    for i in lst1: 
        if i % 2 !=0:
            sum1 += i
    for i in lst:
        if i % 2 !=0:
            sum1 += i 
    return sum1



'''
Write a function that accepts two input lists and returns a new list which contains only the unique elements from both lists
'''

def exe(lst, lst1):
    lst.extend(lst1)
    we = [] 
    for i in lst:
        if i not in we:
            we.append(i)
    
    return we

'''
Write a function that accepts a list and returns a new list such that the new list contains all the items of the old list in reverse order. Note that this is NOT a sorting problem. Do NOT use the built in reverse() method for this problem. For example if:

input_list = ['apples', 'eat', "don't", 'I', 'but', 'Grapes', 'Love', 'I']
then your function should return a list such as:
['I', 'Love', 'Grapes', 'but', 'I', "don't", 'eat', 'apples']
'''
def exe(lst):
    a = lst[(len(lst)-1): 0: -1]
    
    a.append(lst[0])
    return a

