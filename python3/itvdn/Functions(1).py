# Task1
# def call_name(name = "Olga"):
#     print "Hello, ", name, "!"
#
# call_name()
#Task2
# def ex1(x):
#     return x**2
# def ex2(x):
#     return x + x**2
#
# for x in range(-5, 5):
#     print ex1(x)
# x = -5
# my_list_ex1 = []
# my_list_ex2 = []
# x_list = []
# while x <=5:
#     x_list.append(x)
#     my_list_ex1.append(ex1(x))
#     my_list_ex2.append(ex2(x))
#     x= x+0.5
#
# print "x:", "{:>30}".format(x_list)
# print "ex1: ","{:>30}".format(my_list_ex1)
# print "ex2: ", "{:>30}".format(my_list_ex2)

#TASK3

def summ(a,b):
    print "summ is: ", a+b
def sub(a,b):
    print "sub is: ", a-b
def mult(a,b):
    print "mult is:", a*b
def div(a,b):
    if a == 0 or b == 0:
        print "Error: can not be divided into zero"
    else:
        print "div is: ", a/b


operation = 0
operation_list = (None, summ, sub, mult, div)


while True:
    operation = input("Choose operation: "
                      "1. summ "
                      "2. sub "
                      "3. mult "
                      "4. div "
                      "5. exit ")
    if 0 < operation >= len(operation_list):
        break

    a = input("Enter first number: ")
    b = input("Enter second number: ")
    operation_list[operation](a,b)