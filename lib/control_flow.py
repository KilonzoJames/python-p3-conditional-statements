#!/usr/bin/env python3

def admin_login(username, password):
    if (username == 'admin' or username == 'ADMIN') and password == '12345':
        return "Access granted"
    else:
        return "Access denied"
print(admin_login("admin", "12345"))

def hows_the_weather(temperature):
    if temperature < 40 :
        response="brisk"
    elif 40<= temperature < 65 :
        response="a little chilly"
    elif temperature >= 85:
        response="too dang hot"
    else:
        response="perfect"
    return f"It's {response} out there!"
print(hows_the_weather(33))

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        result = "FizzBuzz"
    elif num % 3 == 0:
        result = "Fizz"
    elif num % 5 ==0:
        result = "Buzz"
    else:
        result = num
    return result
print(fizzbuzz(1))
print(fizzbuzz(55))
print(fizzbuzz(30))

def calculator(operation, num1, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "*":
        result =num1 * num2
    else:
        print("Invalid operation!")
        return None
    return result
print(calculator("-",7,1))
