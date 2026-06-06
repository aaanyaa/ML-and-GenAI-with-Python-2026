# ==========================================
# Assignment 1 - Python Basics
# Student Name: Aanya
# Enrollment Number: 00101012025
# ==========================================


# 1. Area of Rectangle

print("----- Area of Rectangle -----")
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area =", area)


# 2. Simple Interest

print("\n----- Simple Interest -----")
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (years): "))

SI = (P * R * T) / 100

print("Simple Interest =", SI)


# 3. Celsius to Fahrenheit

print("\n----- Celsius to Fahrenheit -----")
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (9/5) * celsius + 32

print("Temperature in Fahrenheit =", fahrenheit)


# 4. Average of 3 Numbers

print("\n----- Average of 3 Numbers -----")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)


# 5. Square and Cube of a Number

print("\n----- Square and Cube -----")
number = int(input("Enter a number: "))

square = number ** 2
cube = number ** 3

print("Square =", square)
print("Cube =", cube)


# 6. Swap Two Numbers Without Third Variable

print("\n----- Swap Two Numbers -----")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before Swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After Swapping:")
print("a =", a)
print("b =", b)


# 7. Student Report Program

print("\n----- Student Report -----")

student_name = input("Enter Student Name: ")

mark1 = float(input("Enter marks of Subject 1: "))
mark2 = float(input("Enter marks of Subject 2: "))
mark3 = float(input("Enter marks of Subject 3: "))
mark4 = float(input("Enter marks of Subject 4: "))
mark5 = float(input("Enter marks of Subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5

percentage = (total / 500) * 100

print("\n----- Student Report Card -----")
print("Student Name :", student_name)
print("Total Marks :", total)
print("Percentage :", percentage, "%")
