# 1-valuables

# name= "maya"
# age = 22
# height=165.5
# job = "software engineer"
# print(f"My name is {name} , am {age} years old, my height is {height} cm, and I work as a {job}.")

# 2-to get valu types

# print(type(name), type(age), type(height), type(job))

#3-input

# name=input("Enter your name: ")
# age=int(input("Enter your age: "))
# height=float(input("Enter your height in cm: "))

# next_year=age+1

# print(f"hello {name}")
# print(f"your height is {height} cm")
# print(f"next year you will be {next_year} years old")

# operators

# a=10
# b=2

# print(a+b)
# print(a/b)
# print(a*b)

# print(a**b)
# print(a%b)

#task 1 
#How many days do you train per week?
# How many hours do you train each session?
#Total weekly training hours

# number=int(input("How many days do you train per week? "))
# hours=float(input("how many hours do you train each session? "))

# total=number*hours

# print(f"Total weekly training hours: {total} hours")

#day one final challenge

#athlete profile program

name=input("Enter your name: ")
age=int(input("Enter your age: "))
sport = input("Enter your sport: ")
number=int(input("How many days do you train per week? "))
hours=float(input("how many hours do you train each session? "))
height=float(input("Enter your height in cm: "))

total=number*hours
age_next=age+1

print("----- ATHLETE PROFILE -----")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Sport: {sport}")
print(f"Training days per week: {number}")
print(f"Training hours per session: {hours}")
print(f"Height in cm: {height}")
print(f"Total weekly training hours: {total} hours")
print(f"Age next year: {age_next}")
