# OOPS 
    # Class and Objects
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f'Hello, my name is {self.name} and I am {self.age} years old.'
    def is_adult(self):
        return self.age >= 18
    
person1 = Person('Vijay', 30)
print(person1.greet())
print(f'Is {person1.name} an adult? {person1.is_adult()}')

person2 = Person('Lucky', 13)
print(person2.greet())
print(f'Is {person2.name} an adult? {person2.is_adult()}')

# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_student_info(self):
        return f'Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}'
student1 = Student('Guna', 23, 'S12345')
print(student1.get_student_info())
print(student1.greet())

# Encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f'Amount deposited: {amount}. New balance: {self.__balance}'
        else:
            return 'Deposit amount must be positive.'

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f'Amount withdrawn: {amount}. New balance: {self.__balance}'
        else:
            return 'Invalid withdrawal amount or insufficient funds.'
account1 = BankAccount('123456789', 1000)
print(account1.deposit(500))
print(account1.withdraw(200))
print(account1.withdraw(1500))  # Attempt to withdraw more than balance

# Setters and Getters
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
            return f'Salary updated to: {self.__salary}'
        else:
            return 'Salary must be positive.'
employee1 = Employee('Vijay', 50000)
print(employee1.get_salary())
print(employee1.set_salary(55000))
print(employee1.get_salary())

"""
# Exception Handling
"""
try:
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    result = num1 / num2
    print(f'The result of {num1} divided by {num2} is: {result}')
except ZeroDivisionError:
    print('Error: Cannot divide by zero.')
except ValueError:
    print('Error: Invalid input. Please enter a valid number.') 
"""
# Custom Exceptions
"""
class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def validate_age(age):
    if age < 0:
        raise InvalidAgeError('Age cannot be negative.')
try:
    age = int(input('Enter your age: '))
    validate_age(age)
    print(f'Your age is: {age}')
except InvalidAgeError as e:
    print(f'Error: {e}')
except ValueError:
    print('Error: Invalid input. Please enter a valid age.')
else:    print('Age validation successful.')

"""
# Map, Filter, Reduce
"""
from functools import reduce

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f'Squared numbers: {squared}')

filtered = list(filter(lambda x: x > 10, squared))
print(f'Filtered numbers: {filtered}')

reduced = reduce(lambda x, y: x + y, filtered)
print(f'Reduced sum: {reduced}')

"""
#  File Handling 
# """

try:
    with open('example.txt', 'w') as file:
        file.write('Hello, this is a sample file.\n')
        file.write('This file is used for demonstrating file handling in Python.\n')

    with open('example.txt', 'r') as file:
        content = file.read()
        print('File Content:')
        print(content)
except FileNotFoundError:
    print('Error: File not found.')
except IOError:
    print('Error: Unable to read file.')

try:
    file = open('example.txt', 'r')
    content = file.read()
    print('File Content:')
    print(content)
except FileNotFoundError:
    print('Error: File not found.')
except IOError:
    print('Error: Unable to read file.')
finally:
    try:
        file.close()
    except NameError:
        pass  # file was never opened, so we can ignore this error  