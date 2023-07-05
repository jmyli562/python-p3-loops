#!/usr/bin/env python3


def happy_new_year():
    i = 10
    while i >= 1:
        if i == 1:
            print(i)
            print("Happy New Year!")
            break
        else:
            print(i)
            i = i - 1


def square_integers(int_list):
    int_list = [num**2 for num in int_list]
    return int_list


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
