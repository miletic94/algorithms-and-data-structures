"""
Students have become secret admirers of SEGP. They find the course exciting and the professors amusing. After a superb Mid Semester examination its now time for the results. The TAs have released the marks of students in the form of an array, where arr[i] represents the marks of the ith student.

Since you are a curious kid, you want to find all the marks that are not smaller than those on its right side in the array.

Input Format
The first line of input will contain a single integer n denoting the number of students.
The next line will contain n space separated integers representing the marks of students.

Output Format
Output all the integers separated in the array from left to right that are not smaller than those on its right side.
"""

l1 = [16, 17, 4, 3, 5, 2, 29, 8, 1, 4, 2, 5]


def bigger_than_right(l1):
    bigger = []
    index = 0
    for grade in l1:
        for i in range(index+1, len(l1)):
            if grade <= l1[i]:
                print(grade, " is smaller than ", l1[i])
                break
            if i == len(l1) - 1 and grade >= l1[i]:
                bigger.append(grade)
        index = index + 1
    bigger.append(grade)
    return bigger


print(bigger_than_right(l1))
