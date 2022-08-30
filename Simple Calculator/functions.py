from unittest import result


def addition(first_number, second_number):
     result = first_number + second_number
     print ("{0} + {1} = {2}" .format(first_number, second_number, result))

def subtraction(first_number, second_number):
     result = first_number - second_number
     print ("{0} - {1} = {2}" .format(first_number, second_number, result))

def multiplication(first_number, second_number):
     result = first_number * second_number
     print ("{0} * {1} = {2}" .format(first_number, second_number, result))

def division (first_number, second_number):
     if second_number == 0:
          print("Can't perform the operation")
     else:
          result = first_number/second_number
          print ("{0} / {1} = {2}" .format(first_number, second_number, result))

def modulus (first_number, second_number):
     result = first_number % second_number
     print ("{0} % {1} = {2}" .format(first_number, second_number, result))
