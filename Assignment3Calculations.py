from math import sqrt ,log, sin

def calculations(number):
    print(f"Square root {number} : {sqrt(number)}")
    print(f"logarithm {number} : {log(number)}")
    print(f"Sine  {number} : {sin(number)}")

number = int(input("enter the number :"))
calculations(number)