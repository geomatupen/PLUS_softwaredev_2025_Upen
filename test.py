import os
import sys
print(sys.path)

help("modules")
days_of_the_week = 7
def say_hello(recipient):
    print("hello, world! hello {} ".format(recipient))
    return recipient