# # PROGRAM TO ADD VARIABLE LENGTH ARGUMENTS IN A FUNCTION
# # KRUNALSINH CHHASATIYA
# # 10/12/2024
# def average(name,*args):
#   '''THESE FUNCTION CALCULATES AVERAGE OF THE GIVEN SUBJECTS'''
#   result = 0
#   for num in args:
#     result = result + num
#   avg = result / len(args)
#   print(f"{name} has a average of : {avg}")
# name = input("ENTER THE NAME : \n")
# number_list = list(map(int, input("ENTER THE NUMBERS : ").split(",")))
# average(name,*number_list)
# print("DOCSTRING IS : ",average.__doc__)



# # PROGRAM TO ADD KEYWORD ARGUMENTS IN A FUNCTION
# # KRUNALSINH CHHASATIYA
# # 10/12/2024
# def display(name,**kwargs):
#     '''THESE FUNCTION DISPLAYS THE NAME OF THE STUDENT AND MARKS OF SUBJECTS'''
#     for subjects,marks in kwargs.items():
#         print(f"NAME OF THE STUDENT : {name}.\nNAME OF THE SUBJECT : {subjects}\nMARKS : {marks}")
# display("SANDEEP",Maths = 100, History = 100, Science = 100)
# print("DOCSTRING IS : ",display.__doc__)



# # PROGRAM TO ADD MODULES IN A CURRENT FILE
# # KRUNALSINH CHHASATIYA
# # 10/12/2024
# # sys.path
# '''THESE FUNCTION PERFORMS THE OPERATION OF THE CALCULATER'''
# import cac
# from cac import add,sub,mul,div
# from cac import fact
# print(add(10,20))
# print(sub(10,20))
# print(mul(10,20))
# print(div(10,20))
# print(fact(5))
# print("DOCSTRING IS : ",__doc__)



# PROGRAM TO OPEN FILE USING PYTHON
# KRUNALSINH CHHASATIYA
# 10/12/2024
# with open("mytext.txt","rt") as file
# file = open("mytext.txt","rt")
# print(file.read())
# file.close()


# with open("UPDATED BANNER.png","rb") as rf:
#     with open("test_copy.png","wb") as wf:
#         for line in rf:
#             wf.write(line)



# file = open("text.txt","w")
# lines = ["HELLO WORLD\t", "WELCOME\t", "ENJOY"]
# file.writelines(lines)
# file.close()
# print("DATA WRITTEN SUCCESSFULLY!!!")



# try:
#     num = int(input("ENTER YOUR DIVISOR : "))
#     result = 100 / num
#     print("RESULT : ",result)
# except Exception as e:
#     print("EXCEPTION OCCURED : ",e)
# else:
#     print("NO EXCEPTION OCCURED : ")
# finally:
#     print("COMPLETED!!!")



# while True:
#     try:
#         x = int(input("ENTER A NUMBER : "))
#         break
#     except ValueError:
#         print("OOPS! THAT WAS NO VALID NUMBER. TRY AGAIN...")



