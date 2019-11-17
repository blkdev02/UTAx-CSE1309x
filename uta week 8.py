# UTA WEEK8 File I/O, Tuples, Formatting

# Execrises


'''
Write a function that accepts a filename as input argument and reads the file and saves each line of the file as an element in a list (without the new line ("\n")character) and returns the list. Each line of the file has comma separated values: For example if the content of the file looks like this:

Lucas,Turing,22
Alan,Williams,27
Layla,Trinh,21
Brayden,Huang,22
Oliver,Greek,20
then your function should return a list such as
['Lucas,Turing,22', 'Alan,Williams,27', 'Layla,Trinh,21', 'Brayden,Huang,22', 'Oliver,Greek,20']

'''

def list_from_file(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    # NOW CONTINUE YOUR CODE FROM HERE!!!
    list_of_lines = []
    for line in data: 
        list_of_lines.append(line.strip())
    return list_of_lines


'''

Write a function that accepts a filename(string) of a CSV file which contains the information about student's names and their grades for four courses and returns a dictionary of the information. The keys of the dictionary should be the name of the students and the values should be a list of floating point numbers of their grades. For example, if the content of the file looks like this:

Mark,90,93,60,90
Abigail,84,50,72,75
Frank,46,83,53,79
Yohaan,47,77,74,96
then your function should return a dictionary such as:
out_dict = {'Frank': [46.0, 83.0, 53.0, 79.0],
            'Mark': [90.0, 93.0, 60.0, 90.0],
            'Yohaan': [47.0, 77.0, 74.0, 96.0],
            'Abigail': [84.0, 50.0, 72.0, 75.0]}


'''

def construct_dictionary(filename):
    my_dictionary = {}
    # Make a connection to the file
    file_test = open(filename, 'r')
    data = file_test.readlines()
    for line in data:
        name, course1, course2, course3, course4 = line.strip().split(',')
        my_dictionary[name] = [float(course1), float(course2), float(course3), float(course4)]
    file_test.close()

    return my_dictionary


'''
Write a function that takes a file name (string) of a CSV file which contains the information about student's names and their grades for four courses and returns a dictionary that contains information about the students whose grades in both Math and Chemistry is above 70. Note that if the file has any comments (lines starting with #) then you should ignore such a line. The file will have the following format:

#first_name,math,physics,chemistry,biology
For example if the contents of the file are:
Luke,89,94,81,97
Eva,40,50,65,90
Joseph,55,58,54,99
Oliver,73,74,89,91
then your function should return a dictionary such as:
out_dict = {'Luke': [89.0, 94.0, 81.0, 97.0],
            'Oliver': [73.0, 74.0, 89.0, 91.0]}

'''
def math_chemistry_scores(filename):
    math_chemistry_dict = {}

    access_file = open(filename, 'r')
    data = access_file.readlines()

    temp_list = []

    for line in data:
        if line[0] != '#':
            name, math, physics, chemistry, biology = line.strip().split(',')
            if float(math) > 70 and float(chemistry) > 70:
                math_chemistry_dict[name] = [float(math), float(physics), float(chemistry), float(biology)]
    
        

    access_file.close()
    return math_chemistry_dict


'''
Write a function that accepts a filename as input argument, the file contains the information about a persons expenses on milk and bread and returns a dictionary that contains exactly the strings 'milk' and 'bread' as the keys and their floating point values in a list as values. Each line of the file may start with a 'm' or a 'b' denoting milk or bread respectively. For example if the contents of the file are:

m 0 0 0
b 2 5 1
b 3 5 4
m 1 0 0
b 5 3 1
m 0 1 0
b 2 4 5
then your function should return a dictionary such as:
out_dict = {'milk': [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]], 
            'bread': [[2.0, 5.0, 1.0], [3.0, 5.0, 4.0], [5.0, 3.0, 1.0], [2.0, 4.0, 5.0]]}

            '''
def order_by(filename):
    # Make a connection to the file
    file_access = open(filename, 'r')
    data = file_access.readlines()
    new_dict = {}
    new_dict["milk"]  = []
    new_dict["bread"] = []
    for line in data:
        line = line.strip() 
        char, num1, num2, num3 = line.strip().split()
        if char == "m":
            new_dict["milk"] += [[float(num1), float(num2), float(num3)]]
        else:
            new_dict["bread"] += [[float(num1), float(num2), float(num3)]]
        
        
    return new_dict


'''
Write a function that accepts a file name as input argument and constructs and returns a nested dictionary from it. The keys of this dictionary should be last names, and the values should be dictionaries that contain first names as the keys and integer ages as the values. Note that the data may contain multiple people with the same last name, but it will have unique first names. Ignore any lines that start with '#' The file will contain comma separated values (CSV) For example if the contents of the file are:

#first_name,last_name,age
Matthew,Abbey,65
Chloe,Orion,49
Yohaan,Adams,54
Krishna,Adams,35
Resa,Orion,86
Lucas,Abbey,60
Courtney,Abbey,67
Joseph,Orion,45
Mark,Abbey,60
Eva,Orion,76
then your function should return a dictionary such as:
{'Abbey': {'Matthew': 65, 'Courtney': 67, 'Lucas': 60, 'Mark': 60},
 'Orion': {'Chloe': 49, 'Resa': 86, 'Eva': 76, 'Joseph': 45},
 'Adams': {'Krishna': 35, 'Yohaan': 54}}
 '''


def order_by_lastname(filename):
    my_dictionary = {}
    # Make a connection to the file
    file_pointer = open(filename, 'r')
    data = file_pointer.readlines()
    for line in data:
        if line.startswith("#"):
            continue
        first_name, last_name, age = line.strip().split(',')
        if last_name not in my_dictionary: 
            my_dictionary[last_name] = {first_name : int(age)} 
        else:
            my_dictionary [last_name][first_name] = int(age)
            
        sec_dictionary = {}
        
    return my_dictionary



'''
Write a function that accepts a tuple of positive integers and returns the mean and median of the integers as a tuple. For example if the input tuple is:

(3, 3, 0, 1, 12, 13, 15, 16)
then your function should return a tuple that contains the mean and median as:
(7.875, 7.5)
'''

def statistics(atuple):
    total = 0
    for i in atuple:
        total += i
    mean = float(total/len(atuple))
    
    lst = sorted(atuple)
    
    
    if len(atuple) % 2 == 0:
        num = int(len(lst)/2)
        median = ((lst[num] + lst[num-1])/ 2)
    elif len(lst) % 2 != 0:
        num = int(len(lst)/2)
        median = float(lst[num])
    return (mean, median)




'''
Write a function that accepts a dictionary as input and returns a tuple of tuples. That is your first tuple should be the tuple of all the keys, and the second tuple should be tuple of all the values in the dictionary. For example if the input dictionary is:

input_dictionary = {1:"a", 2:"b", 3:"c", 4:"d"} 
then you should return a tuple(tuple of keys, tuple of values) such as:
((1, 2, 3, 4), ('a', 'b', 'c', 'd'))

'''

def dict_to_tup(dictionary):
    kep_tup = tuple(dictionary.keys())
    val_tup = tuple(dictionary.values())
    return  kep_tup, val_tup





# Assignment

'''
Write a function named create_grades_dict that accepts a string as the name of a file. Assuming that the file is a text file which includes name and grades of students, your function should read the file and return a dictionary with the exact format as shown below: The format of the input file is:

Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
.... 
An example of the input file is shown below. Sample Input Output Assuming that the input file "student_grades.txt" contains the following text:
1000123456, Rubble, Test_3,  80, Test_4 , 80
1000123459, Chipmunk, Test_4, 96, Test_1, 86 , Quiz_1 , 88
Notes:
Items are seperated by comma and one or more spaces may exist between the items.
The "ID" of each student is unique. Two students may have the same Name (but IDs will be different)
The "Name" of each student will only include a last name with no punctuation. Maximum of 15 characters.
There will be an integer grade for each test (0-100)
There are only four valid tests, i.e. Test_1, Test_2, Test_3, Test_4. There may be other grades in the file and you should ignore those grades.
Each student may have missing grade(s) for the tests. A missing grades should be considered as 0.
Grades may not be in order i.e. Test_3 may appear before Test_1.
Your function should read the input file, calculate the average test grade for each student and return a dictionary with the following format:
{'Student_ID':[Last_name,Test_1_grade,Test_2_grade,Test_3_grade,Test_4_grade,average], ...}
For example in the case of sample input file shown above, your function should return the following dictionary:
{'1000123456': ['Rubble', 0, 0, 80, 80, 40.0], '1000123459': ['Chipmunk', 86, 0, 0, 96, 45.5]}

'''


def create_grades_dict(file_name):

    #open the file, access mode 'r' - read
    file_access = open(file_name, 'r')
    data = file_access.readlines()
    student_dict = {}

    for lines in data:
        line = lines.replace(' ','').strip(',')
        temp_value = []
        temp_value.append(line[1])
        if "Test_1" in line:
            temp_value.append(line[line.index('Test_1')+1])
        else:
            temp_value.append(0)
            
        if "Test_2" in line:
            temp_value.append(line[line.index('Test_2')+1])
        else:
            temp_value.append(0)
            
        if "Test_3" in line:
            temp_value.append(line[line.index('Test_3')+1])
        else:
            temp_value.append(0)
            
        if "Test_4" in line:
            temp_value.append(line[line.index('Test_4')+1])
        else:
            temp_value.append(0)
            
        student_dict[str(line[0])] = temp_value


    return student_dict

########## instructor answer ##########

def _create_grades_dict(file_name):
    grade_dict={}
    tests=['Test_1','Test_2','Test_3','Test_4']
    fp=open(file_name,'r')
    lines=fp.readlines()
    fp.close()
    for line in lines:
        elements=line.strip().split(",")
        if elements and elements[0]:
            current_key=elements[0].strip()
            if len(current_key)==10:
                if grade_dict.get(current_key)==None:
                    # Key does not exist. Create it
                    grade_dict[current_key]=[elements[1].strip(),0,0,0,0,0]                
                for index in range(2,len(elements),2):
                    current_element=elements[index].strip()
                    if  current_element in tests:
                        grade_dict[current_key][int(current_element[-1])]=int(elements[index+1])
                grade_dict[current_key][5]=sum(grade_dict[current_key][1:5])/4.0
    return grade_dict


'''
Write a function called print_grades that accepts the name of a file (string) as input argument. Assuming the format of the file is the same as the file in part 1, your function should call the function that you developed in part 1 to read the file and create the grades dictionary. Using the grades dictionary, your function should print the names, grades, and averages of students with the exact format shown below. Notice that you are asked to write a function (NOT a program) and that function prints the grades. Your function should return None after printing the grades.

Sample Input file:

1000123456, Rubble, Test_3,  80, Test_4 , 80, quiz , 90
1000123210, Bunny, Test_2, 100, Test_1, 100,Test_3   , 100 ,Test_4 , 100
1000123458, Duck, Test_1, 86, Test_5   , 100 , Test_2 ,93 ,Test_4, 94
Your program's output should be:

    ID     |       Name       | Test_1 | Test_2 | Test_3 | Test_4 |  Avg.  |
1000123210 | Bunny            |    100 |    100 |    100 |    100 | 100.00 |
1000123456 | Rubble           |      0 |      0 |     80 |     80 |  40.00 |
1000123458 | Duck             |     86 |     93 |      0 |     94 |  68.25 |
Notes:
Column titles are all centered
The printed output is sorted in ascending order based on the student IDs
Each column is seperated from a neighboring column(s) by three characters ' | ' (space vertical_bar space).
IDs are always 10 characters and they are left justified (not counting the boundary characters)
Names are left justified (maximum of 16 characters, not counting the boundary characters).
Grades and averages are right justified. The width of the columns for the grades and averages is 6 characters (not counting the boundary characters).
Averages are right justified with two digits of accuracy after the decimal point.
Hint: Use the function which you developed in part 1 to read the input file and create a dictionary. Use .format() to format the output.

'''



def create_grades_dict(file_name):

    #open the file, access mode 'r' - read
    file_access = open(file_name, 'r')
    data = file_access.readlines()
    student_dict = {}

    for lines in data:
        line = lines.replace(' ','').strip(',')
        temp_value = []
        temp_value.append(line[1])
        if "Test_1" in line:
            temp_value.append(line[line.index('Test_1')+1])
        else:
            temp_value.append(0)
            
        if "Test_2" in line:
            temp_value.append(line[line.index('Test_2')+1])
        else:
            temp_value.append(0)
            
        if "Test_3" in line:
            temp_value.append(line[line.index('Test_3')+1])
        else:
            temp_value.append(0)
            
        if "Test_4" in line:
            temp_value.append(line[line.index('Test_4')+1])
        else:
            temp_value.append(0)
            
        student_dict[str(line[0])] = temp_value


    return student_dict

def print_grades(file_name):
    # Call your create_grades_dict() function to create the dictionary
    grades_dict = create_grades_dict(file_name)
    print( "{0:^10s} |  {1:^16s}  |  {2:^6s}  |  {3:^6s}  |  {4:^6s}  |  {5:^6s}  |  {6:^6s}  |".format("ID", "Name", "Test_1", "Test_2", "Test_3", "Avg."))
    for value in grades_dict.values():
        value.append(float(sum(value[1:]))/len(value[1:]))
        
    for key, value in grades_dict.items():
        print( "{0:<10s}  |  ".format(key), end="")      
        if type(value) == str:
            print("{0:<16s}  |  ".format(value), end="")
        elif type(value) == int:
            print("{0:>6d}  |  ".format(value), end="")
        else:
            print("{0:>6.2f}".format(value))


        
 
################### Instructor function ###################
def _create_grades_dict(file_name):
    grade_dict={}
    tests=['Test_1','Test_2','Test_3','Test_4']
    fp=open(file_name,'r')
    lines=fp.readlines()
    fp.close()
    for line in lines:
        elements=line.strip().split(",")
        if elements and elements[0]:
            current_key=elements[0].strip()
            if len(current_key)==10:
                if grade_dict.get(current_key)==None:
                    # Key does not exist. Create it
                    grade_dict[current_key]=[elements[1].strip(),0,0,0,0,0]
                for index in range(2,len(elements),2):
                    current_element=elements[index].strip()
                    if  current_element in tests:
                        grade_dict[current_key][int(current_element[-1])]=int(elements[index+1])
                grade_dict[current_key][5]=sum(grade_dict[current_key][1:5])/4.0
    return grade_dict
def _print_grades(file_name):
    grade_dict=_create_grades_dict(file_name)
    ids=list(grade_dict.keys())
    ids.sort()
    print("{0:^10s} | {1:^16s} | {2:^6s} | {3:^6s} | {4:^6s} | {5:^6s} | {6:^6s} |".format('ID','Name','Test_1','Test_2','Test_3','Test_4','Avg.'))
    for id in ids:
        name=grade_dict[id][0]
        grades=grade_dict[id][1:5]
        average=grade_dict[id][5]
        print("{0:6d}".format(grade),end="")
        print(" | {0:>6.2f} |".format(average))

    


    
#Quiz

        
'''
Write a function named list_to_tuples that receives a two dimensional list of strings as parameter and returns a tuple of tuples where the content of each inner list is reversed as shown below: For example if the two dimensional list received by the function is

[['mean', 'really', 'is', 'jean'],
 ['world', 'my', 'rocks', 'python']]
Then, your function should return a tuple of tuples as shown below:
(('jean', 'is', 'really', 'mean'), ('python', 'rocks', 'my', 'world'))
'''
def list_to_tuples(MY_LIST):
    my_tuple = ()
    for item in MY_LIST:
        my_tuple += (tuple(item),)
    return my_tuple


'''

Write a function named calculate_grades that receives a file name. The file contains names of students and their grades for 4 quizzes and returns a tuple as specified below. Each line of the file will have the following format:

name,quiz1_score,quiz2_score,quiz3_score,quiz4_score
For example if the contents of the file are:
john,89,94,81,97
eva,40,45,65,90
joseph,0,0,54,99
tim,73,74,89,91
The name and grades are separated by commas. Your function should return the names of the student and their quiz averages as a tuple of tuples as shown below:
(('eva', 60.0), ('john', 90.25), ('joseph', 38.25), ('tim', 81.75))
The tuples should be sorted in ascending order by the student's name.

'''

def calculate_grades(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    # NOW CONTINUE YOUR CODE FROM HERE!!!
    return_tuple = ()
    for lines in data:
        line = lines.strip().split(',')
        return_tuple += (tuple(line[0], (float(sum(line[1:])) / len(line[1:]))
    return_tuple = tuple(sorted(return_tuple, key=lambda name:name[0]))
    return return_tuple
        
'''

Write a function named formatted_print that receives a dictionary as argument. The keys of the dictionary will be the names of the students and the values of the dictionary will be their average scores. Your function should print this information exactly as specified below :

For example if the dictionary received by the function is

{'john':34.480, 'eva':88.5, 'alex':90.55, 'tim': 65.900} 
Then your function should print:
alex       90.55
eva        88.50
tim        65.90
john       34.48
Note:
The names have to be accommodated within 10 spaces and they are left justified.
The scores are floats and they should be right justified in 6 spaces with two digits after the decimal point.
All this information has to be sorted (descending order) by the scores of the students. Notice how alex has the highest score and appears first and john has the lowest score and appears last.
'''


def formatted_print(my_dict):
    sorted_key = sorted(my_dict)
    for key in sorted_key:
        print(" {0:<10s}  {1:>6.2f}".format(key, my_dict[key]))


################### Sample Solution ###################
def dict_to_print(a):
    my_names = list(a.keys())
    my_scores = list(a.values())
    
    # Sort the information by score descending order
    unSorted = True
    while unSorted:
        unSorted = False
        for index in range(0, len(my_scores)-1):
            # if next element is greater element then swap them
            if my_scores[index] < my_scores[index + 1]:
                # sort the scores
                temporary_score = my_scores[index]
                my_scores[index] = my_scores[index + 1]
                my_scores[index + 1] = temporary_score
                # sort the names as well 
                temporary_name = my_names[index]
                my_names[index] = my_names[index + 1]
                my_names[index + 1] = temporary_name               
                
                unSorted = True    
    for x in range(0, len(my_names)):
        print("{0:<10s}{1:>6.2f}".format(my_names[x], my_scores[x]))
        


'''
Write a function named calculate_expenses that receives a filename as argument. The file contains the information about a person's expenses on items. Your function should return a list of tuples sorted based on the name of the items. Each tuple consists of the name of the item and total expense of that item as shown below:

milk,2.35
bread , 1.95
 chips ,    2.54
milk  ,    2.38
milk,2.31
bread,    1.90


Notice that each line of the file only includes an item and the purchase price of that item separated by a comma. There may be spaces before or after the item or the price. Then your function should read the file and return a list of tuples such as:
[('bread', '$3.85'), ('chips', '$2.54'), ('milk', '$7.04')]
Notes:
Tuples are sorted based on the item names i.e. bread comes before chips which comes before milk.
The total expenses are strings which start with a $ and they have two digits of accuracy after the decimal point.
Hint: Use "${:.2f}" to properly create and format strings for the total expenses.
'''
d
def calculate_expenses(filename):
    file_access = open(filename, 'r')
    data = file_access.readlines()
    my_list = []
    temp1 = []
    no_duplicates = set()
    set_to_list = list(no_duplicates)
    
    
    for lines in data:
        line = lines.replace(' ','').split(',')
        temp1.append(line)
        no_duplicates.add(line[0])

    set_to_list = list(no_duplicates)

    for index in range(len(set_to_list)):
        expense = 0
        for lists in temp1:
            if set_to_list[index] in lists:
                expense += lists[-1]

        my_list.append(set_to_list[index],'${0:.2f}'.format(expense))
        my_list = sorted(my_list, key=lambda item:item[0])
    return my_list
        
        
        
################### Sample Solution ###################
def _calculate_expenses_from_file_sample_q6(filename):

    my_dictionary = {}
    # Make a connection to the file
    file_pointer = open(filename, 'r')
    data = file_pointer.readlines()
    
    for line in data:
        line = line.strip().split(',')
        my_item = line[0].strip()
        my_price = float(line[1].strip())
      
        if my_item not in my_dictionary:
            my_dictionary[my_item] =  my_price
        else:
            my_dictionary[my_item] +=  my_price
    my_list = []
    my_keys = sorted(my_dictionary.keys())
    for x in my_keys:
        my_list.append((x,"${0:.2f}".format(my_dictionary[x])))
    return my_list






        
