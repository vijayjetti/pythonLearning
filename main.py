"""
Python supports several built-in data types:
    Integers (int): Whole numbers (e.g., 10, -5).
    Floats (float): Decimal numbers (e.g., 3.14, -0.001).
    Strings (str): Text data enclosed in quotes (e.g., "Hello", 'Python').
    Booleans (bool): Represents True or False.
    Lists: Ordered, mutable collections (e.g., [1, 2, 3]).
    Tuples: Ordered, immutable collections (e.g., (1, 2, 3)).
    Sets: Unordered collections of unique elements (e.g., {1, 2, 3}).
    Dictionaries: Key-value pairs (e.g., {"name": "Alice", "age": 25}).
"""
#  Var types and Assignments
"""
print('Welcome to Python Learning')
a = 80
b = 10
if a<b:
    print('a is lessear than b')
else:
    print('a is greater than b')
"""

"""
age = 30
salary = 25.34
name = 'Vijay Jetti'
isFTE = True
print(f"{type(age)}  :{age}")
print(type(age),':',age)
print(type(salary), ':', salary)
print(f"{type(salary)}  :{salary}")
print(f"{type(name)}  :{name}")
print(f"{type(isFTE)}  :{isFTE}")

"""
# Type Casting
"""
print(int(salary))
print(str(age))
print(str(salary))
print(str(isFTE))
"""
# User Inputs
"""
name = input('Please enter your name: ')
firstNumber = input('Please enter your first number: ')
secondNumber = input('Please enter your second number: ')

print(name)
print(type(firstNumber), ':', firstNumber)
print(firstNumber+secondNumber)
print('Sum of Numbers:', int(firstNumber) + int(secondNumber))

"""
# Escape Sequence
"""
print('Hello Vijay', '\nHow are you')
print('Hello Vijay', "\tHow are you")
print('Hello Vijay', "How are you", 'What are you doing', sep=' || ' , end=' && ')
print('End of escape chars')
"""
"""
# Arithmatic Operators
a = 12
b = 3
print(a+b, a-b, a*b, a/b, a//b, a%b, a**b)

# Comparison Operators
print(a<b, a>b, a<=b, a>=b, a==b, a!=b)

# Logical Operators
print(True and True, False and True, True and False, False and False)
print(True or True, False or True, True or False, False or False)
print(not True, not False)

# Assignment Operators
# +=,-=, *=, /=, %=, *=, /=.
a+=5
print(a)
# Membership Operators // in and not in
fruits =['banana','apple','mango','guava']
print('banana' in fruits, 'kiwi' in fruits, 'kiwi' not in fruits)
fruits.remove('apple')
fruits.append('kiwi')
print('Count: ',fruits.count)
print(fruits)

# Identify Operators is, is not
x=15
y=20
print(x is y, x is not y)
"""
"""
# If Else Conditional Statements
age = int(input('Please enter your age: '))

if  18 <= age <= 80:
    print('You are old enough to drive')
elif age > 80:
    print('You are too old to drive, Better facilitate driver')
elif age >= 15:
    print('Please get a licence to drive a car')
else:
    print('Sorry, You can\'t drive a car')

print('End of the program')
"""
"""
# Match case Statements

lucky = int(input('Please enter your lucky number in between 1 and 10: '))

match lucky:
    case 2: print('You won mobile charger')
    case 5: print('You won $5')
    case 7: print('You won Macbook charger')
    case _: print('Sorry, Better luck next time')

"""
"""
# Print a table
# count = int(input('Please enter your table number: '))
for i in range(1, 11):
    # print(count,'X',i,'=',count*i)
    for j in range(1, 11):
        print(f'{i} X {j} = {i*j}')
    print(f'================================')    
    
"""
"""
fruits =['banana','apple','mango','guava']
for fruit in fruits:
    print(fruit)

for number in range(11):
    print(number)
"""    
# While loop
"""
#  print 1-10 numbers using While Loop
i=1
while i<=10:
    print(i)
    i+=1
"""
"""
# Break, Continue and Pass

for i in range(1, 11):
    if i==5:
        # break  # won't print 5 onwards
        # continue  #skip 5 to print
        pass # do nothing
    print(i)
"""
#  Strings

# Strings Indexing and Slicing
"""
name = 'Vijay'
print('Hello', name)
# Indexing
print(name[0], name[1], name[2], name[3], name[4])
print(name[-1],name[-2],name[-3],name[-4],name[-5])

name = 'VijayBhaskar'
print(name)
print(name[2:6]) # print from 2 to 5 chars [n-1]
print(name[:5]) # print till 4th char [n-1]
print(name[2:]) # print from 2nd char to till end
print(name[2:13:1]) # skip 0 [n-1] chars
# print(name[2:13:2]) # from the output of [2:13] skip every 1 chars
print(name[2:13:3]) # from the output of [2:13] skip every 2 chars after a char

"""
# String Methods
"""
text ='Welcome to Python Python Python Programing'
print(text.upper())
print(text.lower())
print(text.title()) # Each word would be capital
print(text.capitalize()) # First char would be capital
print('Swapcase: ',text.swapcase())
print(text.find('Python')) # Finds at char index
print(text.count('Python'))
print(text.replace('Python','Java'))
print(text.split())  # Split with seperator as space
name = ' Vijay '
age = 30
print(name.strip())
print(name.lstrip())
print(name.rstrip())
print('My name is {} and I am {} years old'.format(name, age))
print(f'My name is {name.strip()} and I am {age} yrs old handsome')
"""
# String Common functions
"""
text = 'Python123'
print(text.isalpha())
print(text.isalnum())
print(text.isdigit())
print(text.isidentifier())
print(text.isspace())
print(text.istitle())
print(len(text))
# Multi line strings 
language ='''
Python is 
required to start
any AI 
'''
print(language)
"""
# Functions and Modules
"""
def greet(name):
    print(f'Welcome {name} to functions in Python')
    return f'Hello {name}, Welcome to Python Learning'
print(greet('Vijay'))

def add(a,b):
    return a+b
print('Sum of two numbers:', add(2, 5))
print(f'sum value {add(9, 4)}')
print(f'sum value {add(b=4, a=5)}')

# Default Arguments
def greet(name='Guest'):
    return f'Hello {name}'
print(greet('Vijay'))
print(greet())

# Keyword Arguments
def student(name, age):
    return f'{name} is {age} years old'
print(student('Guna', 23))
print(student(age=13, name='Lucky'))

# Lambda Functions
square = lambda x: x ** 2
print(square(5))

qube = lambda x: x ** 3
print(qube(3))

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

"""
# Fibonacci Numbers
"""
def fibonacci(number):
    if number == 0 or number == 1:
        return number
    else:
        return fibonacci(number-2) + fibonacci(number-1)
print(fibonacci(6))
"""
"""
import math
print(math.sqrt(100))
print(math.pow(4,3))
print(math.pow(10,2))
print('Resuming of Learning')
"""

# Modules and Packages
"""
import math

print(math.sqrt(100))
print(math.pow(4,3))
print(math.pow(10,2))   

"""
"""
# Lists and List Methods
# Lists are ordered, mutable collections of items. They can contain elements of different data types, including other lists.
numbers = [10, 20, 30, 40, 50]
numbers.append(60)  # Add an element to the end of the list
print(numbers)
numbers.insert(3, 70)  # Insert an element at a specific index
print(numbers) 
numbers.remove(30)  # Remove the first occurrence of an element
print(numbers)
numbers.pop()  # Remove and return the last element
print(numbers)
numbers.pop(2)  # Remove and return the element at a specific index
print(numbers)
print(numbers.index(20))  # Get the index of the first occurrence of an element
print(numbers.count(2))  # Count the occurrences of an element
numbers.sort()  # Sort the list in ascending order
print(numbers)
numbers.sort(reverse=True)  # Sort the list in descending order
print(numbers)
numbers.reverse()  # Reverse the order of the list
print(numbers) 
"""
# List Comprehensions
# List comprehensions provide a concise way to create lists. 
# They consist of brackets containing an expression followed by a for clause, 
# and optionally, one or more if clauses.
"""
squared_numbers = [x ** 2 for x in range(1, 11)]
print(squared_numbers)
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)
"""