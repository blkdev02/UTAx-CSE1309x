#UTA Week 7 Using a different IDE, Multidimensional Lists, Dictionaries


#execrises

'''
Write a function which accepts a 2D list of numbers and
returns the sum of all the number in the list You can assume that the number of columns in each row is the same.
(Do not use python's built-in sum() function).

'''
def sumOf2D(lst):
    sum1 = 0 
    for i in lst:
        for j in i:
            sum1 += j 
    
    return sum1





'''
Write a function that accepts a 2 Dimensional list of integers and
returns the average.
Remember that average = (sum_of_all_items) / (total_number_of_items).

'''

def sumOf2D(lst):
    sum1 = 0 
    num = 0 
    for i in lst:
        for j in i:
            sum1 += j
            num += 1 
    
    return sum1/float(num)




'''
Write a function that accepts a 2D list of integers and
returns the maximum EVEN value for the entire list. You can assume that the number of columns in each row is the same. Your function should return None if the list is empty or all the numbers in the 2D list are odd.
Do NOT use python's built in max() function.

'''

def sumOf2D(lst):
    current_max = 0 
    final_max = 0 
    for i in lst:
        for j in i:
        
            if j % 2 == 0 and j > current_max:
                current_max = j
            else:
                continue    
    final_max = current_max 
    return final_max

'''
Write a function that takes a two-dimensional list (list of lists)
of numbers as argument and returns a list which includes the sum of each row.
You can assume that the number of columns in each row is the same.

'''

def sum_of_rows(sample_list):
    mylist = []
    for item in sample_list:
        mylist.append(sum(item))
    return mylist

'''
Write a function that takes a two-dimensional list (list of lists)
of numbers as argument and returns a list which includes the sum of each column.
Assume that the number of columns in each row is the same.

'''
def sum_of_columns(sample_list):
    # Solution type 1:
    return [max(col) for col in zip(*sample_list)]
    # Alternative Solution
    cols = len(sample_list[0])
    mylist = []
    for c in range(cols):
        column_sum = 0
        for row in sample_list:
            column_sum += row[c]
        mylist.append(column_sum)
    return mylist


'''
Write a function that will receive a 2D list of integers.
The function should return the count of how many rows of the list have even sums and the count of how many rows have odd sums. For example if the even count was 2, and odd count was 4 your function should return them in a list like this: [2, 4].

'''
def count(lst):
    lst1 = [] 
    count_even = 0
    count_odd = 0
    
    for  i in lst: 
        a = sum(i)
        if a % 2 == 0:
            count_even += 1
        elif a % 2 != 0:
            count_odd += 1 
    lst1.append(count_even)
    lst1.append(count_odd)
    return lst1


'''
Write a function that takes a two-dimensional list (list of lists)
of numbers as argument and
returns a list which includes the maximum value of each row.

'''


def max_row(lst):
    lst1 = [] 
    for i in lst:
        lst1.append(max(i))
        
    return lst1



'''
Write a function that takes a two-dimensional list (list of lists)
of numbers as argument and returns a list which includes the maximum value of each column.
Assume that the length of columns is consistent in each row.

'''
def column_max(lst):
    lst1 = [] 
    current_max = 0 
    final_max = 0 
    for i in range(0, len(lst[0])):
        final_max = 0
        for j in lst:
            current_max = j[i]
            if final_max > current_max:
                continue
            else:
                final_max = current_max
        lst1.append(final_max)
    return lst1

'''
Write a function that accepts a 2-dimensional list of integers,
and returns a sorted (ascending order) 1-Dimensional list containing all the integers from the original 2-dimensional list.

'''
def d1(lst):
    temp_lst = [] 
    for i in lst:
        sort1 = sorted(i)
        for k in sort1:
            temp_lst.append(k)
    temp_lst.sort()        
    return temp_lst


'''
Write a function that accepts a 2-dimensional list of integers,
and sorts (descending order) all the elements inside each row
and returns the sorted 2-dimensional list.

'''

def sort1(lst):
    lst1 = []
    for i in lst:
        i.sort(reverse = True)
        lst1.append(i)
    return lst




'''
Write a function that accepts two (matrices) 2 dimensional lists a and b of
unknown lengths and returns True if they can be multiplied together False otherwise. Hint: Two matrices a and b can be multiplied together only if
the number of columns of the first matrix(a) is the same as the number of rows of the second matrix(b).
The input for this function will be two 2 Dimensional lists. For example if the input lists are:

'''

def check(lst, lst1):
    count_row = 0 
    count_column = 0
    a = None
    for i in range(0, len(lst[0])):
        for j in lst:
            a = j 
        count_column += 1    
    count_row = len(lst1[1])
    
    if count_row == count_column:
        return True 
        
    else: 
        return False


# instructor solution 

def _multiplication_check_sample_(a, b):
    columns_of_a = len(a[0])
    rows_of_b = len(b)
    if columns_of_a == rows_of_b:
        return True
    else:
        return False

 
'''
Write a function that accepts two (matrices) 2 dimensional lists a and b of unknown lengths and returns their product. Hint: Two matrices a and b can be multiplied together only if the number of columns of the first matrix(a) is the same as the number of rows of the second matrix(b). Hint: You may import and use the numpy module but your return must be a python list not a numpy array. The input for this function will be two 2 Dimensional lists. For example if the input lists are:

a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]
Then your function should return their product such as:
[[15, 9, 47], [21, 10, 66]]
'''
# find the product of matrices multiplication
def check(a, b):
        columns_of_a = len(a[0])
        rows_of_b = len(b)
        if columns_of_a == rows_of_b:
            return True
        else:
            return False

def resultant(temp1, temp2, row, column):
    result = 0
    for index in range(len(temp1[row])): 
        result += temp1[row][index] * temp2[index][column]
    return result
    
    
    #return sum(list(map(lambda x ,y: x*y, temp1[row], temp2[row][column])))
def create_matrix(list1, list2):
    matrix = []
    rows_of_a = len(list1)
    columns_of_b = len(list2[0])
    for i in range(rows_of_a):
        temp = []
        for j in range(columns_of_b):
            temp.append(None)
        matrix.append(temp)
    return (matrix)

def main_matrix_multiplication(matrix_a, matrix_b):
            
#create matrix list and a temp list to append all the columns of matrix_b
    
    temp_collect_column = []
    if check(matrix_a, matrix_b):
        matrix = create_matrix(matrix_a, matrix_b)
        for r in range(len(matrix_a)):
            for c in range(len(matrix_b[r])):
                temp_collect_column.append(matrix_b[c][r])
                matrix[r][c] = resultant(matrix_a, matrix_b, r, c)
        return (matrix)
                


    else:
        return None

###alternative with numpy
def _product_of_two_vectors_sample_(a, b):
    import numpy
    product = (numpy.mat(a) * numpy.mat(b))     # returns a numpy array
    product_to_list = product.tolist()          # convert the numpy array to a standard list
    return product_to_list






'''
Write a function that accepts a dictionary as input and returns a sorted list of all the keys in the dictionary.

'''
def sorting(dic):
    lst = list()
    lst = dic.keys()
    lst.sort()
    return lst

'''
Write a function that accepts a dictionary as input and returns a sorted list of all the values in the dictionary. Assume that the values of this dictionary are just integers.

'''

def sorting(dic):
    lst = list(dic.values())
    lst = sorted(lst)
    return lst



'''
Write a function that accepts a dictionary as input which contains the names and grades of students (The keys are student names and the values are lists of grades for 3 exams (1 Dimensional list)) and returns the list of names for those students whose grade on all three exams is greater than or equal to 78.

'''
def great_or_equal(dict1):
    lst = list(dict1.values())
    lst1 =list(dict1.keys())
    new_lst = list()
    for i in lst:
        if  min(i) < 78:
            continue
        else:
            num = lst.index(i)
            new_lst.append(lst1[num])
       
    return new_lst


'''
Write a function which accepts a dictionary and an integer as input and returns an ascending sorted list of all the keys whose values contain the input value. Note that the keys of this dictionary are strings while the values of this dictionary are 1 Dimensional lists of integers. For example if the input dictionary is:

sample = {"rabbit" : [1, 2, 3],
          "kitten" : [2, 2, 6],
          "lioness": [6, 8, 9]}
and the input integer is 2 then your function should return:
[ "kitten", "rabbit",]
If the input integer is not found then your function should return an empty list.
'''
def value_contain(dict1, int1):
    lst = list(dict1.keys())
    lst1 = list(dict1.values())
    new_lst = list()
    for i in lst1:
        if int1 in i:
            num = lst1.index(i)
            new_lst.append(lst[num])
    new_lst = sorted(new_lst)
    return new_lst


'''
Write a function that takes a string as input argument and returns a dictionary of letter counts i.e. the keys of this dictionary should be individual letters and the values should be the total count of those letters. You should ignore white spaces and they should not be counted as a character. Also note that a small letter character is equal to a capital letter character.

'''
def count(str1):
    str1 = str1.lower(). strip()
    dict1 = dict()
    for i in str1:
        if i == " ":
            continue
        num = str1.count(i)
        dict1.update({i: num})
    return dict1



'''
Write a function that takes a string as input argument and returns a dictionary of vowel counts i.e. the keys of this dictionary should be individual vowels and the values should be the total count of those vowels. You should ignore white spaces and they should not be counted as a character. Also note that a small letter vowel is equal to a capital letter vowel.

'''
def vowel_count(str1):
    str1 = str1.lower(). strip()
    dict1 = dict()
    for i in str1:
        if i == " ":
            continue
        elif i in "aeiou":
            num = str1.count(i)
            dict1.update({i: num})
    return dict1


'''
Write a function that takes a string of words as input argument and returns a dictionary of word counts. The keys of this dictionary should be the unique words and the values should be the total count of those words. Assume that characters are not case sensitive. For example if the input string is :

"I am tall when I am young and I am short when I am old" 
Then the output should be:
{'short': 1, 'young': 1, 'am': 4, 'when': 2, 'tall': 1, 'i': 4, 'and': 1, 'old': 1}

'''
def words_count(str1):
    str1 = str1.lower(). strip()
    lst = str1.split()
    dict1 = dict()
    for i in lst:
        if i == " ":
            continue
        elif dict1.get(i) == None:
            num = lst.count(i)
            dict1.update({i: num})
    return dict1




'''
Write a function that takes an integer as input argument and returns the integer using words. For example if the input is 4721 then the function should return the string "four seven two one". Note that there should be only one space between the words and they should be all lowercased in the string that you return.

'''
def numToWords(int1):
    dict1 = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', 
    '4': 'four', '5': 'five', '6': 'six', '7': 'seven', 
    '8': 'eight', '9': 'nine'}
    str1 = str(int1)
    lst = list()
    for i in str1:
        if dict1.get(i) == None:
            continue
        lst.append(dict1.get(i))
    str1 = " ".join(lst)
        
    return str1

'''
Write a function that accepts a string which contains a particular date from the Gregorian calendar. Your function should return what day of the week it was. Here are a few examples of what the input string(Month Day Year) will look like. However, you should not 'hardcode' your program to work only for these input!

"June 12 2012"
"September 3 1955"
"August 4 1843" 
Note that each item (Month Day Year) is separated by one space. For example if the input string is:
"May 5 1992"
Then your function should return the day of the week (string) such as:
"Tuesday"
Algorithm with sample example:
# Assume that input was "May 5 1992"
day (d) = 5        # It is the 5th day
month (m) = 3      # (*** Count starts at March i.e March = 1, April = 2, ... January = 11, February = 12)
century (c) = 19   # the first two characters of the century
year (y) = 92      # Year is 1992 (*** if month is January or february decrease one year)
# Formula and calculation
day of the week (w) = (d + floor(2.6m - 0.2) - 2c + y + floor(y/4) + floor(c/4)) modulo 7
after calculation we get, (w) = 2
Count for the day of the week starts at Sunday, i.e Sunday = 0, Monday = 1, Tuesday = 2, ... Saturday = 6
Since we got 2, May 5 1992 was a Tuesday
'''
from math import floor
def dayOftheWeek(str1):
    dict1 = {'january': 11, 'february': 12, 'march': 1, 'april': 2, 
            'may': 3, 'june': 4, 'july': 5, 'august': 6, 'september': 7,
            'october': 8, 'november': 9, 'december': 10}
    lst = str1.lower(). split()
    month = dict1.get(lst[0].lower())
    day = int(lst[1])
    full_year = int(lst[-1])
    temp_year = str(full_year)
    century = int(temp_year[:2])
    if month == 11 or month == 12: 
        year = int(temp_year[2:]) - 1
    else: 
        year = int(temp_year[2:])
    calculation = (day + (floor((2.6 * month) - 0.2) - (2 * century) 
    + year + floor(year/4) + floor(century/4))) % 7
    dict2  = { 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
               5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    answer = dict2.get(calculation)
    return answer

dayOftheWeek("May 5 1992")


'''
Write a function that takes a 4 digit integer (from 1000 to 9999 both inclusive) as input argument and returns the integer using words as shown below:

Sample Examples:
if the input integer is 7000 then the function should return the string "seven thousand"
if the input integer is 1008 then the function should return the string "one thousand eight"
if the input integer is 4010 then the function should return the string "four thousand ten"
if the input integer is 1012 then the function should return the string "one thousand twelve"
if the input integer is 4506 then the function should return the string "four thousand five hundred six"
if the input integer is 9900 then the function should return the string "nine thousand nine hundred"
if the input integer is 8880 then the function should return the string "eight thousand eight hundred eighty"
if the input integer is 5432 then the function should return the string "five thousand four hundred thirty two"
Notice that the words in the output strings should all be lower cased and separated by only one space and make sure your words match the following spellings:
one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen,
sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty,
ninety, hundred, thousand
'''

# Type your code here
def numTowords(int1):
    dict1 = { 1: 'one', 2: 'two', 3: 'three', 4: 'four',
               5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
               9: 'nine', 10: 'ten', 11:'eleven', 12: 'twelve',
               13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
               16 :'sixteen', 17: 'seventeen', 18: 'eighteen', 
               19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
               50: 'fifty', 60: 'sixty', 70:'seventy', 80: 'eighty',
               90: 'ninety', 100: 'hundred', 1000: 'thousand'}
    str1 = str(int1)
    lst = []
    word = " "
    for i in str1:
        lst.append(i)
    for j in str1:
        if j == "0":
            lst.remove(j)
            continue
            
        elif len(lst) == 4:
            word +=  dict1.get(int(lst[0]))+ " " + dict1.get(1000) + " "
            lst.remove(j)
                
        elif len(lst) == 3:
            word += dict1.get(int(lst[0]))+ " " + dict1.get(100)+ " "
            lst.remove(j)    
            
        elif len(lst) == 2:
            str2 = "".join(lst)
            int2 = int(str2)
            none_or_sum = dict1.get(int2)
            if none_or_sum == None:
                temp = ['0']
                temp.insert(0, j)
                str3 = "".join(temp)
                int3 = int(str3)
                word += dict1.get(int3)+ " "
                lst.remove(j)                
                
            else:
                word += none_or_sum+ " "
                del lst[:]
                break
        
        elif len(lst) == 1:
            a = int(j)
            word += dict1.get(a)
    word = word.strip()        
    return word     
        

numTowords(4010)







#Assignments


'''
Write a function named find_word_horizontal that accepts a 2-dimensional list of characters (like a crossword puzzle) and a string (word) as input arguments. This function searches the rows of the 2d list to find a match for the word. If a match is found, this functions returns a list containing row index and column index of the start of the match, otherwise it returns the value None (no quotations).

For example if the function is called as shown below:
crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
find_word_horizontal(crosswords,word)
then your function should return
[2,1]
Notice that the 2d input list represents a 2d crossword and the starting index of the horizontal word 'cat' is [2,1]

s	d	o	g
c	u	c	m
a	c	a	t
t	e	t	k
Note: In case of multiple matches only return the match with lower row index. If you find two matches in the same row then return the match with lower column index.

'''

def find_word_horizontal(crosswords,word):
    list_to_word = ''
    row = 0
    colmun = 0
    if not crosswords or not word:
        return None
    else:
        
        for nest in range(len(crosswords)):
            row = nest
            list_to_word = ''.join(crosswords[nest])
            if list_to_word.find(word) != -1:
                column = list_to_word.find(word)
                return [row, column]
    return None


'''
Write a function named find_word_vertical that accepts a 2-dimensional list of characters (like a crossword puzzle) and a string (word) as input arguments. This function searches the columns of the 2d list to find a match for the word. If a match is found, this functions returns a list containing row index and column index of the start of the match, otherwise it returns the value None (no quotations).

For example if the function is called as shown below:
crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
find_word_vertical(crosswords,word)
then your function should return:
[1,0]
Notice that the 2d input list represents a 2d crosswords and the starting index of the vertical word 'cat' is [1,0]

s	d	o	g
c	u	c	m
a	c	a	t
t	e	t	kNote: In case of multiple matches only return the match with lower column index. If you find two matches in the same column then return the match with lower row index.
'''

def find_word_vertical(crosswords,word):
    list_to_words = ''
    if not crosswords or not word:
        return None 
    else:
        for index in range(len(crosswords)):
            column = index
            temp_list = []
            for j in range(len(crosswords[index])):
                temp_list.append(crosswords[j][index])
            list_to_words = ''.join(temp_list)
            if list_to_words.find(word) != -1:
                row = list_to_words.find(word)
                return [row, column] 
    return None

'''
Write a function named capitalize_word_in_crossword that accepts a 2-dimensional list of characters (like a crossword puzzle) and a string (word) as input arguments. This function searches the rows and columns of the 2d list to find a match for the word. If a match is found, this functions capitalizes the matched characters in 2-dimensional list and returns the list. If no match is found, this function simply returns the origianl 2-dimensional list with no modification.

Example 1: If the function is called as shown below:
crosswords=[['s','d','o','g'],['c','u','c','m'],['a','x','a','t'],['t','e','t','k']]
word='cat'
  capitalize_word_in_crossword(crosswords,word)
then your function should return:
[['s','d','o','g'],['C','u','c','m'],['A','x','a','t'],['T','e','t','k']]
Notice that the above list is a representation for a 2-dimensional crossword puzzle as shown below.
s	d	o	g
C	u	c	m
A	x	a	t
T	e	t	kExample 2: if the function is called as shown below:
crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
  capitalize_word_in_crossword(crosswords,word)
then your function should return:
[['s','d','o','g'],['c','u','c','m'],['a','C','A','T'],['t','e','t','k']]
Notice that the above list is a representation for a 2-dimensional crossword puzzle as shown below.
s	d	o	g
c	u	c	m
a	C	A	T
t	e	t	kNote: If both a horizontal and a vertical match is found then only select the horizontal match. For example, in the above case there is a horizontal match starting at [2,1] and there is also a veritcal match starting at [1,0]. Notice that only the characters in the horizontal match should be capitalized in the returned list.
Hint: You should use the functions that you developed in part 1 and part 2 as helper functions for part 3.


'''

def find_word_vertical(crosswords,word):
    list_to_words = ''
    if not crosswords or not word:
        return None 
    else:
        for index in range(len(crosswords)):
            column = index
            temp_list = []
            for j in range(len(crosswords[index])):
                temp_list.append(crosswords[j][index])
            list_to_words = ''.join(temp_list)
            if list_to_words.find(word) != -1:
                row = list_to_words.find(word)
                return [row, column] 
    return None

def find_word_horizontal(crosswords,word):
    list_to_word = ''
    row = 0
    colmun = 0
    if not crosswords or not word:
        return None
    else:
        
        for nest in range(len(crosswords)):
            row = nest
            list_to_word = ''.join(crosswords[nest])
            if list_to_word.find(word) != -1:
                column = list_to_word.find(word)
                return [row, column]
    return None


def capitalize_word_in_crossword(crosswords,word):

    if not crosswords or not word:
        return None

    length_word = len(word)

    check_horizontal = find_word_horizontal(crosswords, word)
    if check_horizontal != None:
        list_location = check_horizontal
        for row in range(len(crosswords)):
             for column in range(len(crosswords[row])):
                 if [row, column] == list_location:
                     for i in range(column, (length_word + column)):
                         crosswords[row][i] = crosswords[row][i].capitalize()
                     return crosswords

    check_vertical = find_word_vertical(crosswords, word)
    if check_vertical != None:
        list_location = check_vertical
        for row in range(len(crosswords)):
            for column in range(len(crosswords[row])):
                if [row, column] == list_location:
                    for i in range(row, length_word + row):
                        crosswords[i][column] = crosswords[i][column].capitalize()
                    return crosswords


#Quiz
                     
        
'''
Write a function named row_maximums that accepts a 2-dimensional list of numbers as parameter and returns a dictionary whose values would be the maximum value of each row and whose keys would be the appropriate strings as specified below.

For example if the function receives the following list:


[[5, 0, 0, 0, 13],
 [0, 12, 0, 0],
 [20, 0, 11, 0],
  [6, 0, 0, 8]] 
then your function should return the dictionary such as:
{'row 0 max': 13, 'row 1 max': 12, 'row 3 max': 8, 'row 2 max': 20}
Notes:
Everything in the keys is separated by one space and the characters are lower cased.
The 2-dimensional list may have different number of columns in each row.
The row indicies for the keys should start at 0 and go to n. So your program should work for any number of rows and columns.
You may not use the built in max() function.

'''


def row_maximums(some_multi_dimensional_list):
    if not some_multi_dimensional_list:
        return None
    max_dict = {}
    for row in range(len(some_multi_dimensional_list)):
        maximum = max(some_multi_dimensional_list[row])
        max_dict["row", row,"max"] =  maximum
    return max_dict


'''
Write a function named construct_dictionary_from_lists that accepts 3 one dimensional lists and constructs and returns a dictionary as specified below.
The first one dimensional list will have n strings which will be the names of some people.
The second one dimensional list will have n integers which will be the ages that correspond to those people.
The third one dimensional list will have n integers which will be the scores that correspond to those people.
Note that if a person has a score of 60 or higher (score >= 60) that means the person passed, if not the person failed.
Your function should return a dictionary where each key is the name of a person and the value corresponding to that key should be a list containing age, score, 'pass' or 'fail' in the same order as shown in the sample output.
For example, if the function receives the following lists:

 (["paul", "saul", "steve", "chimpy"], [28, 59, 22, 5], [59, 85, 55, 60])
then your function should return the dictionary such as:
{'steve': [22, 55, 'fail'], 'saul': [59, 85, 'pass'], 'paul': [28, 59, 'fail'], 'chimpy': [5, 60, 'pass']}
Note that the order of the keys of the dictionary does not need to be the same as shown in this sample example.
'''


def construct_dictionary_from_lists(names_list, ages_list, scores_list):
    details_dict = {}
    for row in range(len(names_list)):
        temp = []
        temp.append(ages_list[row])
        temp.append(scores_list[row])
        if scores_list[row] >= 60:
            temp.append('paass')
        else:
            temp.append('fail')
            
        details_dict[names_list[row]] = temp
    return details_dict


 
################### Instructor function ###################
def create_dictionary_from_list_q5_sample(names, ages, scores):
    sample_dict = {}
    for index in range(0, len(names)):
        if scores[index] >= 60:
            sample_dict[names[index]] = [ages[index], scores[index], "pass"]
        else:
            sample_dict[names[index]] = [ages[index], scores[index], "fail"]

    return sample_dict


'''
Write a function named one_to_2D which receives an input list and two integers r and c as parameters and returns a new two-dimensional list having r rows and c columns.

Note that if the number of elements in the input list is larger than r*c then ignore the extra elements. If the number of elements in the input list is less than r*c then fill the two dimensional list with the keyword None. For example if your fuction is called as hown below:

 one_to_2D([8, 2, 9, 4, 1, 6, 7, 8, 7, 10], 2, 3) 
Then it should return:
 [[8, 2, 9],[4, 1, 6]]


 '''
def one_to_2D(some_list, r, c):
    column = 0
    multi_list = []
    for row in range(r):
        multi_list.append([])
        n = 0 
        while n != c:
            if len(multi_list[row]) < 3:
                if column < len(some_list):
                    multi_list[row].append(some_list[column])
                else:
                    multi_list[row].append(None)
                n += 1
                column += 1
            
    return multi_list


########## instructor answers
def _1d_to_2d_sample_(sample_list, rows, cols):
    my_2d_list = []
    product = rows * cols
    length = len(sample_list)
    if length > product:
        # ignore the extra elements by slicing
        # and creating a new list to work with
        sample_list = sample_list[0:product]
    else:
        # fill the rest of the index of the
        # 2d list with None
        difference = product - length
        for i in range(length, length+difference):
            sample_list.append(None)

    for i in range(0, len(sample_list), cols):
        my_2d_list.append(sample_list[i:i+cols])

    return my_2d_list


'''
Write a function named multiplication_table that receives a positive integer 'n' as parameter and returns a n by n multiplication table as a two-dimensional list.

For example if the integer received by the function 'n' is:

4
then your program should return a two_dimensional list with 4 rows and 4 columns such as:

[[1, 2, 3, 4],
 [2, 4, 6, 8],
 [3, 6, 9, 12],
 [4, 8, 12, 16]]
 '''

def multiplication_table(n):
    multi_list = [[i for i in range(1, n+1)]]
    temp_multi = multi_list[0][:]
    for element in temp_multi:
        if element == 1:
            continue
        else:
            temp = list(map(lambda x: x * element, temp_multi))
        multi_list.append(temp)
    return multi_list


######################instructor answer ##########
def multiplication_table(n):
    total_list = []
    for r in range(1, n+1):
        for c in range(1, n+1):
            total_list.append(r*c)
    multiplication_table = []
    for i in range(0, len(total_list), n):
        multiplication_table.append(total_list[i:i+n])
    return multiplication_table




                
