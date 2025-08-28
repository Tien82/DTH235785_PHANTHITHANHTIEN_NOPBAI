print("Viet ma chuong trinh")

print("Albert Einstein da tung noi: Mot nguoi khong bao gio mac sai lam khong bao gio thu bat ky dieu gi moi.")

if 5>2:
    print("Five is greater than two")

total = 1 + \
2 + \
3
print(total); print("Hello python")

if True:
    print("True")
else:
    print("False")

#This is a comment
print("Hello, World!")

import math
import os

import math_libs
math_libs.add(4,5)

def add(a,b):
    result = a+b
    return result



#module1.py
question = "what is the meaning of Life, the Universe, and Everything?"
answer = 42

#module2.py

question = "what is your quest?"
answer = "To seek the holy grail."

import module1
import module2
print(module1.question)
print(module2.question)
print(module1.answer)
print(module2.answer)