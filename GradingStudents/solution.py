#!/bin/python3

import os


#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    for x in grades:
        y = x % 5
        if x >= 38 and 5 - y < 3:
            grades[grades.index(x)] += (5 - y)
    return grades


if __name__ == '__main__':

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)