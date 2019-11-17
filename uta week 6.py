# Week 6 String, String Methods, String Practice




'''
Write a program using while loops that asks the user for a positive integer 'n' and prints a triangle using numbers from 1 to 'n'. For example if the user enters 6 then the output should be like this :

(There should be no spaces between the numbers)

1
22
333
4444
55555
666666
'''
# Type your code here
num = int(input("Enter a postive integer: "))
a = 1  
while a <= num:
    c = str(a)
    print ( c * a)
    a += 1


'''
Write a program that asks the user for an input 'n' and prints a square of n by n asterisks "*". For example if the user enters 5 then the output should look like the following: Note that there should be no spaces between the asterisks

*****
*****
*****
*****
*****
'''
n = int(input("Enter a postive integer: "))
c = "*"
for i in range(1, n):
    c += "*"
for j in range(0, n):
    print (c)


'''
Write a program that asks the user for an input 'n' (assume that the user enters a positive integer) and prints only the boundaries of the triangle using asterisks "*" of height 'n'. For example if the user enters 6 then the height of the triangle should be 6 as shown below and there should be no spaces between the asterisks on the top line:

******
*   *
*  *
* *
**
*

'''
n = int(input("Enter a positive integer: "))
c = '*'
for i in range(n , 0, -1):
    if i == n or i == 2 or i == 1:
        print(i * c)
    else:
        result = i - 2
        astr = result * ' '
        print(c + astr + c)



'''
Write a function that accepts an alphabetic character and returns the number associated with it from the ASCII table.

'''


def char_integer(chara):
    integer=ord(chara)
    return (integer)

'''
Write a function that accepts an alphabetic string and returns an integer which is the sum of all the UTF-8 codes of the character in that string. For example if the input string is "hello" then your function should return 532
'''
def sum_chara(string):
    total = 0
    for i in string:
        total += ord(i)
    return (total)


'''
Write a function that accepts an input string consisting of alphabetic characters and removes all the leading whitespace of the string and returns it without using .strip(). For example if:

input_string = "    Hello  "
then your function should return a string such as:
output_string = "Hello  "

'''
def whiteSpace(string):
    string_list = list(string)
    for i in string_list:
        if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            pointer = string_list.index(i)
            return (''.join(string_list[pointer:]))



'''
Write a function that accepts an input string consisting of alphabetic characters and removes all the trailing whitespace of the string and returns it without using any .strip() method. For example if:

input_string = "  Hello       "
then your function should return an output string such as:
output_string = "  Hello"
'''
def trail(a):
    b = None
    for i in range((len(a))-1, 0, -1):
        if a[i] != " ":
            b = i 
            break
    c = a[:b+1]
    return c



'''
Write a function which accepts an input string and returns a string where the case of the characters are changed, i.e. all the uppercase characters are changed to lower case and all the lower case characters are changed to upper case. The non-alphabetic characters should not be changed. Do NOT use the string methods upper(), lower(), or swap().

'''

def change(string1):
    word =""
    lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U' , 'V', 'W', 'X', 'Y', 'Z']
    lst1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in string1: 
        if i in lst:
            index1 = lst.index(i)
            word += lst1[index1]
        elif i in lst1: 
            index2 = lst1.index(i)
            word += lst[index2]
        else:
            word += i 
    return word



'''
Write a function which accepts an input string consisting of alphabetic
characters and spaces and returns the string with all the spaces removed.
Do NOT use any string methods for this problem.

'''
def space(astring):
    str1 = ""
    for i in astring:
        if i != " ":
            str1 += i
    return str1




'''
Write a function that takes a string consisting of alphabetic characters as input argument and returns True if the string is a palindrome. A palindrome is a string which is the same backward or forward.
Note that capitalization does not matter here i.e. a lower case character can be considered the same as an upper case character.
'''

# Type your code here
def  drome(str1):
    a = 0
    b = -1
    str1 = str1.lower()
    lst = str1

    for i in range(len(lst), 0, -1):
        if not lst:
            return True 
        elif lst[a] == lst[ b]:
            lst = lst[a + 1: b]
            b += -1
            a += 1
    
    return False

'''
Write a function that takes a list of words as an input argument and returns True if the list is sorted and returns False otherwise.

'''
def test(lst):
    lst1 = lst
    lst2 = lst1 
    if sorted(lst1) == lst2:
        return True 
    else:
        return False

'''
Write a function which returns the total number of vowels in an input string which consists of alphabetic characters. Note that capitalization does not matter here i.e. a lower case character should be considered the same as an upper case character.
For this problem, the vowels are considered to be A, E, I, O, U.
'''
def vowels(str1):
    count = 0
    str2 = str1.lower()
    lst = str2.split(" ")
    lst1 = ["a", "e", "i", "o", "u"]
    
    for i in range(0, len(str2)):
        if str2[i] in lst1:
            count += 1
    
    return count




'''
Write a function that accepts a string and a character as input and
returns the number of times the character is repeated in the string.
Note that capitalization does not matter here i.e. a lower case character should be treated the same as an upper case character.

'''


def exe(str1, char):
    count = 0
    str2 = str1.lower()
    char1 =char.lower()
    for i in str2:
        if char1 == i:
            count += 1 
    return count

'''
Write a function that accepts a string and a character as input and
returns the count of all the words in the string which start with the given character. Assume that capitalization does not matter here.
You can assume that the input string is a sentence i.e. words are separated by spaces and consists of alphabetic characters.
'''
def start(str1, chr1):
    word = ""
    num = 0
    str1 =str1.lower()
    chr1 = chr1.lower()
    lst = str1.split()
    for i in lst:
        word = word.join(i)
        if chr1 == word[0]:
            num += 1
        word = ""
    return num

'''
Write a function which returns the number of words in the input string
which have more than 4 characters.
Assume that the input string consists of alphabetic characters separated by spaces and capitalization does not matter i.e. an upper case character should be treated the same as a lower case character.

'''
def length(str1):
    lst = str1.split()
    count = 0
    for i in lst:
        if len(i) > 4:
            count += 1
    return count

'''
Write a function that takes a string consisting of alphabetic characters as
input argument and returns the most common character.
Ignore white spaces i.e.
Do not count any white space as a character.
Note that capitalization does not matter here i.e. that a lower case character is equal to a upper case character.
In case of a tie between certain characters return the last character that has the most count
'''
def exe(str1):
    a= 0
    str1 = str1.lower()
    str1 = str1.replace( " ", "")
    b = len(str1)-1
    for j in range(len(str1)):
        count = 0
        count1 = 0
        for i in str1:
            word = str1[a]
            if word == i:
                count += 1 
        temp = count
        for i in str1:
            word1 = str1[b]
            if word1 == i:
                count1 += 1
        if  count > count1:
            most_char = word
            b -= 1
            continue
        elif count < count1: 
            most_char = word1
            a += 1
        else:
            most_char = word1
            a += 1
    return most_char


'''
Write a function which accepts an input string and returns a reverse of the input string while the case for every single character is reversed. The input string for this function would be a sentence (words separated by spaces) consisting of alphabetic characters. For example if:

input_string = "Hello Python World"
then the function should return a string such as:
"DLROw NOHTYp OLLEh"

'''
# Type your code here
def change(string1):
    word =""
    lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U' , 'V', 'W', 'X', 'Y', 'Z']
    lst1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(string1)-1, -1, -1): 
        if string1[i] in lst:
            a = string1[i] 
            index1 = lst.index(a)
            word += lst1[index1]
        elif string1[i] in lst1: 
            a = string1[i]
            index2 = lst1.index(a)
            word += lst[index2]
        else:
            word += string1[i]


'''
Write a function that accepts a string of words separated by spaces
consisting of alphabetic characters and returns a string such that
each word in the input string is reversed while the order of the words
in the input string is preserved. The length of the input string must be equal to the length of the output string i.e. there should be no extra trailing or leading spaces in your output string. For example if:

input_string   = “this is a sample test”
then the function should return a string such as:
"siht si a elpmas tset"
'''

def reserve(string):
    blist = []
    tempList = string.split()
    for word in tempList:
        reString = word[len(word)::-1]
        blist.append(reString)
    return ' '.join(blist)
    
    





#Assignment




'''

Write a function named single_insert_or_delete that accepts two strings as input arguments and returns:

0 if the two strings match exactly.
1 if the first string can become the same as the second string by inserting or deleting a single character.
Notice that inserting and deleting a character is not the same as replacing a character.
2 otherwise
Capital letters are considered the same as lower case letters. Here are some examples:
First string	Second String	Function return
Python	Java	2
book	boot	2
sin	sink	1 (Inserting a single character at the end)
dog	Dog	0
poke	spoke	1 (Inserting a single character at the start)
poker	poke	1 (Deleting a single character from the end)
programing	programming	1 (Inserting a single character)


'''
def single_insert_or_delete(s1,s2):
    a1 = s1.lower()
    a2 = s2.lower()
    
    a1_list = list(a1)
    a2_list = list(a2)
    
    if a1 == a2:
        return 0
    mistakes = 0
    if len(a1) > len(a2):
        for i in range(len(a1_list)):
            if a1_list[i] not in a2_list[i:]:
                a2_list.insert(i, a1_list[i])
                mistakes += 1
    elif len(a1) < len(a2):
        for i in range(len(a2_list)):
            if a2_list[i] not in a1_list[i:]:
                a1_list.insert(i, a2_list[i])
                mistakes += 1
    else:
        for i in range(len(a2_list)):
            if a2_list[i] != a1_list[i]:
                a1_list[i] = a2_list[i]
        mistakes = 2
                
    if mistakes > 2:
        mistakes = 2
    return mistakes

#instructor answer
################### Instructor function ###################
def _instructor_function (s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    if s1==s2:
        return 0
    if abs(len(s1)-len(s2))!=1:
        return 2

    if len(s1)>len(s2):
        # only deletion is possible
        for k in range(len(s2)):
            if s1[k]!=s2[k]:
                if s1[k+1:]==s2[k:]:
                    return 1
                else:
                    return 2
        return 1
    else: # s1 is shorter Only insertion is possible
        for k in range(len(s1)):
            if s1[k]!=s2[k]:
                if s1[k:]==s2[k+1:]:
                    return 1
                else:
                    return 2
        return 1

    

'''
Write a function named find_mismatch that accepts two strings as input arguments and returns:

0 if the two strings match exactly.
1 if the two strings have the same length and mismatch in only one character.
2 if the two strings do not have the same length or mismatch in two or more characters.
Capital letters are considered the same as lower case letters. Here are some examples:
First string	Second String	Function return
Python	Java	2
Hello There	helloothere	1
sin	sink	2 (note not the same length)
dog	Dog	0


'''

def find_mismatch(s1,s2):
    a1 = s1.lower()
    a2 = s2.lower()
    
    a1_list = list(a1)
    a2_list = list(a2)
    
    if a1 == a2:
        return 0
    mistakes = 0
    if len(a1) > len(a2):
        for i in range(len(a1_list)):
            if a1_list[i] not in a2_list[i:]:
                a2_list.insert(i, a1_list[i])
                mistakes += 1
    elif len(a1) < len(a2):
        for i in range(len(a2_list)):
            if a2_list[i] not in a1_list[i:]:
                a1_list.insert(i, a2_list[i])
                mistakes += 1
    else:
        for i in range(len(a2_list)):
            if a2_list[i] != a1_list[i]:
                a1_list[i] = a2_list[i]
        mistakes = 2
                
    if mistakes > 2:
        mistakes = 2
    return mistakes

'''
Write a function named spelling_corrector that accepts two arguments. The first argument is a sentence (string) and the second argument is a list of words (correct_spells). Your function should check each word in the input string against all the words in the correct_spells list and return a string such that:

If a word in the original sentence matches exactly with a word in the correct_spells then the word is not modified and it should be directly copied to the output string.
if a word in the sentence can match a word in the correct_spells list by replacing, inserting, or deleting a single character, then that word should be replaced by the correct word in the correct_spelled list.
If neither of the two previous conditions is true, then the word in the original string should not be modified and should be directly copied to the output string.
Notes:
Do not spell check one or two letter words (copy them directly to the output string).
In case of a tie use the first word from the correct_spelled list.
Ignore capitalization, i.e. consider capital letters to be the same as lower case letters.
All characters in the output string should all be in lower case letters.
Assume that the input string only includes alphabetic characters and spaces. (a-z and A-Z)
Remove extra spaces between the words.
Remove spaces at the start and end of the output string.
Examples:
Sentence (str)	correct_spells (list)	Function return (str)
Thes is the Firs cas	['that','first','case','car']	thes is the first case
programing is fan and eesy	['programming','this','fun','easy','book' ]	programming is fun and easy
Thes is vary essy	['this', 'is', 'very', 'very', 'easy']	this is very easy
Wee lpve Pythen	['we', 'Live', 'In', 'Python']	we live python
Notice:
In the first example 'thes' is not replaced with anything.
In the first example both 'case' and 'car' could replace the 'cas' in the original sentence, but 'case' is selected because it was encountered first.
Please notice that this assignment is only an exercise and a real spell checker requires more functionalities.
Hint: You should use the functions that you developed in part 1 and part 2 to help you solve this problem.


'''

def spelling_corrector(s1, s2):

    def single_insert_or_delete(s1,s2):
        a1 = s1.lower()
        a2 = s2.lower()
        
        a1_list = list(a1)
        a2_list = list(a2)
    
        if a1 == a2:
            return 0
        mistakes = 0
        if len(a1) > len(a2):
            for i in range(len(a1_list)):
                if a1_list[i] not in a2_list[i:]:
                    a2_list.insert(i, a1_list[i])
                    mistakes += 1
        elif len(a1) < len(a2):
            for i in range(len(a2_list)):
                if a2_list[i] not in a1_list[i:]:
                    a1_list.insert(i, a2_list[i])
                    mistakes += 1
        else:
            for i in range(len(a2_list)):
                if a2_list[i] != a1_list[i]:
                    a1_list[i] = a2_list[i]
                    mistakes += 1
                    
        if mistakes > 2:
            mistakes = 2
        return mistakes


    # find the mismatch
    def find_mismatch(s1,s2):
        a1 = s1.lower()
        a2 = s2.lower()
        
        a1_list = list(a1)
        a2_list = list(a2)
        
        if a1 == a2:
            return 0
        mistakes = 0
        if len(a1) > len(a2):
            for i in range(len(a1_list)):
                if a1_list[i] not in a2_list[i:]:
                    a2_list.insert(i, a1_list[i])
                    mistakes += 1
        elif len(a1) < len(a2):
            for i in range(len(a2_list)):
                if a2_list[i] not in a1_list[i:]:
                    a1_list.insert(i, a2_list[i])
                    mistakes += 1
        else:
            for i in range(len(a2_list)):
                if a2_list[i] != a1_list[i]:
                    a1_list[i] = a2_list[i]
                    mistakes += 1
                    
        if mistakes > 2:
            mistakes = 2
        return mistakes
    # replace with  correct spelling
    a1 = s1.split()
    temp = []
    for i in range(len(a1)):
        for j in range(len(s2)):
            mistakes = find_mismatch(a1[i], s2[j])
            if mistakes == 1:
                if single_insert_or_delete(a1[i], s2[j]) == 1:
                    temp.append(s2[j])
                break
        if mistakes == 2:
            temp.append(a1[i])
    return (' '.join(temp))



#quiz



'''
Write a function named count_consonants that receives a string as parameter and
returns the total count of the consonants in the string.
Consonants are all the characters in the english alphabet except for 'a', 'e', 'i', 'o', 'u'.
If the same consonant repeats multiple times you should count all of them.
Note that capitalization and punctuation does not matter here i.e. a lower case character should be considered the same as an upper case character.
'''
def count_consonants(string):
    new_string = string.replace(' ','')
    count = 0
    for char in new_string.lower():
        if char  not in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count 


'''
Write a function named find_longest_word that receives a string as parameter
and returns the longest word in the string.
Assume that the input to this function is a string of words consisting of alphabetic characters that are separated by space(s).
In case of a tie between some words return the last one that occurs.
'''
                    
def find_longest_word(string):
    alist = string.split(' ')
    templist = []
    temp_word = ''
    for i in alist:
        if len(i) >= len(temp_word):
            temp_word = i
            templist.append(temp_word)
    return (templist[-1])


'''
Encryption problem: You and your friend want to encrypt your messages and you have shared a secret key that is known to just the two of you. Every character in the character_set is mapped to some other character in the secret key. For example 'a' is mapped to 'D', 'b' is mapped to 'd', 'c' is mapped to '1' and so forth as shown below:

character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
Write a function named my_encryption that accepts a string (a message which will only consist of the characters from the character set) as function parameter and encrypts that message using the secret_key and returns it. For example if input to this function (the message that you want to send) is:
"Lets meet at the usual place at 9 am"
Then your function should should return the encrypted message:
"oABjMWAABMDBMB2AMvjvDPMYPD1AMDBMGMDW" 
Note that capitalization does matter here!

'''
def my_encryption(string):
    sentence = string.replace(' ', '')
    new_sentence = ''
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"

    for i in sentence:
        index = character_set.index(i)
        new_sentence += secret_key[index]

    return new_sentence





