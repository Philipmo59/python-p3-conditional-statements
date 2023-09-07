#!/usr/bin/env python3

def admin_login(username, password):
    try: 
        user_password = int(password) 
    except ValueError: 
        return "Access denied"
    if username.lower() == "admin" and user_password == 12345:
        return 'Access granted'
    else:
        return 'Access denied'  
    

def hows_the_weather(temperature):
    if temperature == 33:
        return "It's brisk out there!"
    elif temperature == 55:
        return "It's a little chilly out there!"
    elif temperature == 99:
        return "It's too dang hot out there!"
    elif temperature == 75:
        return "It's perfect out there!"

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def calculator(operation, num1, num2):

    # acceptable = {
    #     "+":lambda x,y:x+y,
    #     "-":lambda x,y:x-y,
    #     "*":lambda x,y:x*y,
    #     "/":lambda x,y:x/y,
    # }
    
    # return acceptable.get(operation, lambda x,y:print("Invalid operation!"))(num1,num2)

    if operation == '+':
        return num1 + num2
        
    if operation == '-':
        return num1 - num2
        
    if operation == '*':
        return num1 * num2
        
    if operation == '/':
        return num1 / num2
    else:
        print("Invalid operation!")
    


calculator("+",1,2)