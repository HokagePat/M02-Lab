# Author: Patrick Szpak
# Program: M02 Lab - If, else, and while case study (GPA.py)
# Purpose: Accept input for student name and GPA, test for qualifications
# Date: 11/03/2022

# This program will accept input for a student's first and last name
# As well as the student's GPA and test to see if the student either
# Qualifies for the Dean's List, Honor Roll, or neither.

studentLastName = input("Enter the student's last name OR ZZZ to quit: ")
if studentLastName == ('ZZZ'):
    quit()
elif studentLastName != ('ZZZ'):
    studentFirstName = input("Enter the student's first name: ")

studentGPA = float(input("Enter the student's GPA: "))
if studentGPA >= 3.5:
    print(studentFirstName + " " + studentLastName + " is on the Dean's List!")
elif 3.5 > studentGPA >= 3.25:
    print(studentFirstName + " " + studentLastName + " is on the Honor Roll!")
elif studentGPA < 3.25:
    print(studentFirstName + " " + studentLastName + " is not on the Dean's List or the Honor Roll.")