# UTA Final Exams


'''
Final Exam, Part 4 (Calculate your grade for this course)
Write a function named my_final_grade_calculation that receives a file name and returns a dictionary that tells whether a student in this course passed or failed based on the following criteria.

Each line of the file will have the format:

name, q1, q2, q3, q4, q5, q6, a1, a2, a3, a4, midterm, final
where
name is a string
q1 through q6 are quiz scores (integers)
a1 through a4 are assignment scores (integers values)
midterm is midterm score (integer)
final is final exam score (integer)
For example, if the content of the file looks like this:
tom, 10, 20, 0, 100, 0, 100, 70, 80, 90, 0, 80, 85
mary, 0, 50, 66, 40, 10, 60, 70, 80, 90, 100, 80, 85
joan, 0, 80, 40, 10, 50, 60, 7, 80, 90, 0, 80, 5
Note that there may be additional spaces between the entries in each line.

Your function should return a dictionary such as:
{"tom":"pass", "mary":"pass", "joan":"fail"} 
Notes:
Two of the lowest quizzes should be dropped and the average of the remaining four quizzes is worth 25% of the total grade.
The lowest assignment score should be dropped and the average of the remaining three assignments is worth 25% of the total grade.
Midterm and final exams are each 25% of the total grade.
Calculate the total score of the student and if the total score is greater than or equal to 60 (totalscore >= 60) then the student has passed. Notice that the keys (names) and the values (pass or fail) of the dictionary should be all lower cased with no spaces in any of them.

'''

def my_final_grade_calculation(filename):
    file_access = open(filename, 'r')
    data = file_access.readlines()
    result_dict = {}

    for each_line in data:
        temp = []
        resut = []
        line = each_line.replace(' ','').split(',')
        temp = line[1:7]
        min1_q = min(temp)
        temp.remove(min1_q)
        min2_q = min(temp)
        temp.remove(min2_q)
        result.append((float(sum(temp)) / len(temp)) * (0.25))
        temp = line[7:11]
        min1_a = min(temp)
        temp.remove(min1_a)
        result.append((float(sum(temp)) / len(temp)) * (0.25))
        result.append(line[-2]*0.25)
        result.append(line[-1]*0.25)
        if sum(result) >= 60:
            result_dict[line[0]] = 'Pass'
        else:
            result_dict[line[0]] = 'Fail'
    return result_dict



################### Instructor function ###################
def my_final_grades_sample_f(file_name):
    fp = open(file_name, "r")
    data = fp.readlines()
    my_dictionary = {}
    for x in range(0, len(data)):
        stripped = data[x].strip().split(',')
        for x in range(1, len(stripped)):
            stripped[x] = int(stripped[x].strip())

        # extract various parts from each line
        name = stripped[0].lower()
        quizzes = stripped[1:7]
        assignments = stripped[7:11]
        midterm = int(stripped[11])
        final = int(stripped[12])

        # deal with the quizzes # remove the two minimum quizzes
        quizzes.remove(min(quizzes))
        quizzes.remove(min(quizzes))

        # deal with the assignments # remove one of the minimum assignment
        assignments.remove(min(assignments))

        # calculate the percentage of each score based on 25%
        quiz_score = (sum(quizzes)/len(quizzes)) * 0.25
        assignment_score = (sum(assignments)/len(assignments)) * 0.25
        midterm_score = midterm * 0.25
        final_score = final * 0.25

        # calculate total score
        total_score = quiz_score + midterm_score + assignment_score + final_score
        # print("q =", quizzes, quiz_score)
        # print("assign =", assignments, assignment_score)
        # print("midterm, final", midterm_score, final_score)
        # print("total_score", total_score)
        if total_score >= 60:
            my_dictionary[name] = "pass"
        else:
            my_dictionary[name] = "fail"
    return my_dictionary



'''
Final Exam, Part 5 (Create a two dimensional list)
Write a function named "MY_2D_LIST" that receives a positive integer n (n >= 1) as parameter and returns a 2 dimensional list of numbers as shown below:

For example, if the function is called as

MY_2D_LIST(8)
then your function should return
[[1],
[1, 1],
[1, 2, 1],
[1, 3, 3, 1],
[1, 4, 6, 4, 1],
[1, 5, 10, 10, 5, 1],
[1, 6, 15, 20, 15, 6, 1],
[1, 7, 21, 35, 35, 21, 7, 1]]
Notes:
The first list has 1 element, the second list has 2 elements, the third list has 3 elements and so on.
The first and the last element of each list are always 1.
The value of other elements in each list is the sum of the elements from the previous list with the same index and the index before. For example, the value of the element with index 2 in the list with index 5 is 10 which is equal to the sum of the values of the elements from previoius list with index 2 and index 1.
This is called Pascal's Triangle
'''
def pascal(n):
    pascal_list = [[1]]
    for i in range(1, n):
        n = [1]
        for j in range(1, i):
            n.append(pascal_list[i-1][j-1] + pascal_list[i-1][j])
        n.append(1)
        pascal_list.append(n)
    return pascal_list





'''
Write a function named "reverse_dictionary" that receives a dictionary as input argument and returns a reverse of the input dictionary where the values of the original dictionary are used as keys for the returned dictionary and the keys of the original dictionary are used as value for the returned dictionary as explained below:

For example, if the function is called as

reverse_dictionary({'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']})
then your function should return
{'precise': ['accurate', 'exact'], 'clever': ['astute', 'smart'], 'talented': ['smart'], 'bright': ['smart'], 'exact': ['accurate'], 'smart': ['astute']}
Notes:
The list of values in the returned dictionary is sorted in ascending order
Capitalization does not matter. This means that all the words should be converted to lower case letters. For example the word "Accurate" is capitalized in the original dictionary but in the returned dictionary it is written with all lower case letters

'''
def reverse_dictionary(input_dict):
    new_dict = {}
    key_list = list(input_dict.keys())
    value_list = list(input_dict.values())
    for index in range(len(value_list)):
        key_to_value = key_list[index].lower()
        print(key_to_value)
        for item in value_list[index]:
            if new_dict.get(item) == None:
                new_dict[item] = [key_to_value]
            else:
                new_dict[item] += [key_to_value]
        new_dict[item] = sorted(new_dict[item])            
    return (new_dict)



################### Instructor function ###################
def _reverse_dictionary(input_dict):
    output_dict={}
    for k in input_dict:        
        for value in input_dict[k]:
            key_lowered=k.lower()
            value_lowered=value.lower()
            if output_dict.get(value_lowered):
                if k not in output_dict[value_lowered]:
                    output_dict[value_lowered].append(key_lowered)
                    output_dict[value_lowered].sort()
            else:
                output_dict[value_lowered]=[key_lowered]
    return output_dict



