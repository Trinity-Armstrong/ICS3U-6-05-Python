#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: December 2019
# This program calculates your average grade


def calculate(list_of_marks):
    # This function calculates the average of the user's grades

    mark_average = 0

    # Process
    for counter in list_of_marks:
        mark_average = mark_average + counter

    mark_average = mark_average/len(list_of_marks)

    # Output
    return round(mark_average)


def main():
    # This function outputs the users grades and average

    list_of_marks = []
    mark = None

    # Input
    print("I will be calculating your overall average.")
    print("Enter all of your marks, enter -1 when you're done.")
    print("")

    mark = int(input("Enter your mark: "))
    list_of_marks.append(mark)
    while mark != -1:
        mark = int(input("Enter your mark: "))
        list_of_marks.append(mark)

    # Process
    list_of_marks.pop()
    average = calculate(list_of_marks)

    # Output
    print("")
    print("Your average is {0}%".format(average))


if __name__ == "__main__":
    main()
