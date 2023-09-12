import sys

def getint(promt):
    while True:
        try:
            number = int(input(promt))
            return number #breaking the loop 
        except ValueError:  #exception
            print("invalid num , enter a valid num: ")
        except EOFError:
            sys.exit(1) #terminating a program using  1
        finally:
            print("the finally clause always executes even if exception  ")

first_num= getint("please enter first num: ")
second_num= getint("please enter second num: ")

try:
    print("{} divided by {} is {}".format(first_num,second_num,first_num / second_num))
except ZeroDivisionError:
    print("u cant divided a zero ")
    sys.exit(1)
else:
    print("division performed successfully")











