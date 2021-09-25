# Tutorial #11: Python Basics

This tutorial covers essential programming skills in Python:

- Variables
- Python's object model
- Conditions
- Functions
- Data structures 
- Loops
- Functions as objects
- Exception handling
- Modules

## Install Python:

Install the latest version of **Python 3** from the [official Python site](https://www.python.org/downloads/).

## 1. Hello, World!

Use your favorite source code editor (e.g., VS Code) to create a Python script in a file called *hello-world.py* with the following code:

```python
print("Hello, World!")
```

> To create the Python script, create a new file in your source code editor and save it as *hello-world.py*. The extension *.py* means your file contains a Python script.

Then, run your program using the command-line interface. In this tutorial, we will use the command-line interface to run our Python programs. Later, we will run our Python programs using a web application development framework.  

**Execute your Python program**

Depending on your operating system and Python installation settings, you may run your Python program using one of the following commands on the command-line interface. Make sure you navigate to the exact location where you saved your Python script file:

The Python installer will make the Python interpreter available through the `python` command by default:

`python hello-word.py`

In some cases, the Python installer will make the Python interpreter available through the `python3` command:

`python3 hello-world.py`

On Windows, some users may need to use the Python launcher (*py*):

`py python hello-world.py`

## 2. Variables

From now on, we will write our Python code using the interactive mode of the Python interpreter. Run the Python interpreter from the command line interface by typing the command `python` (or the equivalent command in your local machine used in Task 1).

Python has four primitive data types:
- Integers
- Floats
- Strings
- Booleans

```python
an_integer = 5
a_float = 5.5
a_string = "Hello, World!"
a_boolean = True # The other possible boolean value is False 
```

We can use the *type* function to determine a data type:

```python
type(an_integer)
type(a_float)
type(a_string)
type(a_boolean)
```

### Type conversion 

As in other programming languages, we can convert a data type into another one using the functions:
    - int()
    - float()
    - string()
    - bool()

For example,

```python
a_number_string = "5"
a_number = int(a_number_string)
```

### Formatting strings

Python 3.6 added a new string interpolation method called literal string interpolation or *f strings*. This new way of formatting strings is powerful and easy to use.

It enables us to embed Python expressions inside strings:

```python
my_name = "Jose"
f"Hello, {my_name}"
```

> Note we need to add the prefix *f* to the string we want to format.

F strings also make it easy to specify the format of float and other types when displayed as strings:

```python
total = 2.0
f"The total of your order is: ${total:.2f}"
```

> The syntax *.2f* means: display the *total* variable as with two decimal points.

## 3. Python's object model

A powerful technique that Python supports is object-oriented programming, a particular type of programming or programming paradigm, which is a way of thinking about how we write programs.

In object-oriented programming, we think about the world in terms of objects where objects contain data inside of them called attributes. Objects also support the ability to perform actions through methods (functions) that operate on those objects.

EVERYTHING that exists in Python, like numbers, strings, lists, and even functions, and other entities, exists in Python in its own "box," known as Python objects. This means every entity has attributes and methods. 

Create a Python file called *objects.py*.

String methods are very useful for manipulating strings:

```python
my_name = "jose"

my_name.count('j')
my_name.startswith("J")

my_name_upper = my_name.capitalize()
my_name_upper

my_name_upper.startswith("J")
```

## 4. Conditions

Python conditions begin with the *if* keyword followed by a boolean expression and a colon.
- A boolean expression is something that evaluates to *True* or *False*
- The colon indicates the beginning of the body of the if statement

Write a program that tells if a variable *n* with a value of your choice is positive, negative, or zero:

```python
n = 10

if n > 0:
    print(f"{n} is positive")
elif n < 0:
    print(f"{n} is negative")
else:
    print(f"{n} is zero") 
```

> In Python, indentation is required! This is how Python knows what is part of the body of a conditional statement (or any other block statement).

## 5. Functions

We have already seen several built-in functions, such as print, type, and int.

We can also define our functions. Let's write a function that *prints* the square of a number:

```python
def print_square(n):
    print(n ** 2)

print_square(100)
```

Create a function that *returns* the square of a number:

```python
def square(n):
    return n ** 2

square = square(100)
print(square)
```

Attempting to capture the result of a function that does not return any value results in *None*, which is a special value in Python that represents the absence of a value:

```python
square = print_square(100)
print(square)

print(type(square))
```

## 6. Data structures

Python has four built-in types of data structures:

- Tuples: a sequence of immutable values
- Lists: a sequence of mutable values
- Sets: a collection of unique values
- Dictionaries: a collection of key-value pairs

Strings are also considered sequences in Python because we can access individual characters using the exact mechanisms for manipulating elements contained in lists and other data structures.

```python
my_name = "Jose"

my_name[0]
my_name[1]
my_name[2]

my_name[:3]

len(my_name)
```

### Lists

Now, rather than using a single variable for representing a single name, let's create a list representing names of people:

```python
names = ["Jose", "Mary", "Erick"]
names
```

Lists are mutable, and there are several methods to access and manipulate the data in a list:

```python
names.append("Pedro")
print(names)

names.sort()
print(names)
```

> Note the sort method changes the order in which the elements in the list appear.

### Dictionaries

A dictionary or dict is a container that stores mappings of unique keys to values. Dictionaries in Python resemble dictionaries in the real world. A dictionary in the real world contains words (keys) and definitions (values). When you want to obtain a definition (value), you use the word (key) for accessing its definition in the dictionary. The difference between Python dictionaries is that in Python, values can be any object! However, the concept of using keys to access values remains the same.

Let's use a dictionary to organize the list of people in a more detailed way by adding their ages:

```python
people ={"Jose": 30, "Mary": 25, "Erick": 32}
people
```

> We access elements in a dictionary using keys rather than indexes as in lists.

Use the bracket notation to access individual elements in a dictionary:

```python
people["Jose"]
```

Python also has several methods for accessing information in a dictionary:

```python
people.keys()


'Jose' in people.keys()
'Jose' not in people.keys()

if 'Jose' in people.keys():
    print('Jose is in the dictionary')

# Equivalent to:

if 'Jose' in people:
    print('Jose is in the dictionary')
```

## 7. Loops

The main idea behind loops is to write code that can run multiple times.

Let's write the simplest loop in Python:

```python
for item in [0, 1, 2, 3, 4, 5]:
    print(item)
```

> Python takes each element in the list and executes the code in the loop's body for each element.

Another popular way for iterating over a sequence of values is to use the built-in function range:

```python
for item in range(0, 6):
    print(item)
```

We can also use for loops for iterating any type of data structure:

```python
my_name = "Jose"
for letter in my_name:
    print(letter)

names = ["Jose", "Mary", "Erick"]
for name in names:
    print(name)

people ={"Jose": 30, "Mary": 25, "Erick": 32}
for person in people:
    print(f"{person} => {people[person]}")
```

## 8. Functions as objects

Python follows the functional programming paradigm, in which functions can be treated like any other object. Thus, we can treat functions as the input and output of other functions!

Let's arrange the list our previous list of people as a list of dictionaries:

```python
people = [
    {"name": "Jose", "age": 30},
    {"name": "Mary", "age": 25},
    {"name": "Erick", "age": 32}
]

people.sort()
```

Since we are calling the sort method using a list of dictionaries, we need to inform Python how to sort them. We will define a function for telling Python how to process each dictionary in the list:

```python
def sort_people(person):
    return person["name"]

people.sort(key=sort_people)
people
```

When defining simple functions, we can use the lambda keyword to define a function in the place when we want to use them:

```python
people.sort(key=lambda person: person["name"])
people
```

## 9. Exception handling

At this point, we have seen Python throwing us errors due to unexpected events going on in our Python programs. Python also allows us to handle these exceptional situations and prevent our Python programs from crashing.

Write a program that asks two values from the user and computes their division: 

```python
def divide():
    x = int(input("x: "))
    y = int(input("y: "))    
    result = x / y
    print(f"{x} / {y} = {result}")

divide()
```

If the use enters for the second variable 0, the program crashes! As it is not possible to divide by 0:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in divide
ZeroDivisionError: division by zero
```

We can write a more robust program that handles a situation like this:

```python
def divide():
    x = int(input("x: "))
    y = int(input("y: "))    
    try:
        result = x / y
        print(f"{x} / {y} = {result}")
    except ZeroDivisionError:
        print("Cannot divide by 0!")

divide()
```

What happens if the user enters a value that is not a number?

We can also write another exception handling statement to address this potential problem:

```python
def divide():
    try:
        x = int(input("x: "))
        y = int(input("y: "))    
    except ValueError:
        print("Value entered is not a number.")
    else:
        try:
            result = x / y
            print(f"{x} / {y} = {result}")
        except ZeroDivisionError:
            print("Cannot divide by 0")

divide()
```

So exception handling is helpful if you expect that some lines of code might run into a problem, such as a value error or a zero division, and handle those errors properly.

If you're building a web application using Python, handling errors allows us to display a friendly message or to decide on a course of action rather than the program entirely crash and reporting a cryptic to the user.

## 10. Modules

We have built functions that we can use within the same Python program. We can also make those functions available to others and use them in other Python programs.

To achieve this, we first need to know how to import functions and classes from other Python files called modules.

From the module *math*, we can use several functions for computing mathematical operations:

```python
from math import sqrt

sqrt(9)
```

Python also supports using aliases when importing functionality from modules. Aliases help us to differentiate functionality imported in our Python programs and avoid name clashes with names of functions and variables created by us:

```python
from math import sqrt as calculate_sqrt

calculate_sqrt(9)
```

We can also import the entire module rather than a specific function:

```python
import math

# Importing the entire module requires using the dot notation for accessing individual functions:
math.sqrt(9)
```

We can also create our modules. Create a Python file called *mymodule.py* with the following code:

```python
def squares(n):
    return n ** 2
```

Import the file:

```python
from mymodule import squares

squares(10)
```

It is often the case that we want to use modules that are not available in our default Python installation, and we need to install them separately. Python has a package manager called *pip* for installing Python modules, which we will use next week for setting up a Web development framework called Django.
