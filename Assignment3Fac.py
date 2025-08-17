def factorial(number):
    mul = 1
    for i in range(1,number+1):
        mul = mul * i
    print(f"Factorial is {number} is : {mul}")


number1 = int(input("enter the number :"))
factorial(number1)
