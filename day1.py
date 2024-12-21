# a = int(input("ENTER THE NUMBER TO CHECK WHETHER IT IS EVEN OR NOT : "))
# if(a % 2 == 0):
#     print("THE NUMBER IS EVEN!!!")
# elif(a == 0):
#     print("THE NUMBER IS 0")
# else:
#     print("THE NUMBER IS ODD!!!")


# a = int(input("ENTER THE FIRST NUMBER : "))
# b = int(input("ENTER THE SECOND NUMBER : "))
# c = int(input("ENTER THE THIRD NUMBER : "))
# if(a > b and a > c):
#     print(f"{a} IS THE GREATEST!")
# elif(b > a and b > c):
#     print(f"{b} IS THE GREATEST!")
# else:
#     print(f"{c} IS THE GREATEST!")


# a = int(input("ENTER THE NUMBER TO CHECK WHETHER IT IS EVEN OR NOT : "))
# result = "EVEN" if a % 2 == 0 else "ODD"
# print(result)


# a = 0
# while(a < 5):
#     print(a)
#     a += 1


# for i in range(0,11):
#     print(i)


# for i in range(1,11):
#     print(5*i)


# for i in range(1,11):
#     if(i % 2 == 0):
#         print(i)


# for i in range(0,11,2):
#     print(i)


# import sys
# #Accessing command-line arguments
# script_name = sys.argv[0]
# arg1 = sys.argv[1]
# arg2 = sys.argv[2]
# #Printing command-line arguments
# print("Script Name : ",script_name)
# print("First Arguments : ",arg1)
# print("Second Arguments : ",arg2)

# # python day1.py 10 20 
# #E:\IMPACT TRAINING>python day1.py 10 20
# # Script Name :  day1.py
# # First Arguments :  10
# # Second Arguments :  20


# a=float(input("ENTER THE NO. :"))
# print(a)


# a=int(input("ENTER THE FIRST NUMBER : "))
# b=int(input("ENTER THE SECOND NUMBER : "))
# c=int(input("ENTER THE THIRD NUMBER : "))
# d=int(input("ENTER THE FOURTH NUMBER : "))
# e=int(input("ENTER THE FIFTH NUMBER : "))
# sum = a + b + c + d + e
# print(sum) 


# result = lambda a,b : a + b
# print(result(10,20))

# f = lambda x,y : x + y
# sum = f(10,20)
# print(sum)


# from functools import reduce

# # Example data
# numbers = [1, 2, 3, 4, 5, 6]

# # 1. Using `map`: Double each number in the list
# doubled = list(map(lambda x: x * 2, numbers))
# print("Doubled numbers:", doubled)

# # 2. Using `filter`: Keep only the even numbers
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print("Even numbers:", evens)

# # 3. Using `reduce`: Compute the sum of all numbers
# sum_of_numbers = reduce(lambda x, y: x + y, numbers)
# print("Sum of numbers:", sum_of_numbers)


# def fact(n):
#     """THIS FUNCTION CALCULATES FACTORIAL OF A GIVEN NUMBER"""
#     result = 1
#     for i in range(1,n + 1):
#         result = result * i
#     return result
# print(fact(5))
# print(fact.__doc__)


