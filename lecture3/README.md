# Lecture 3
##  Functions
Functions are a simple way to group together actions. With them you can do some 
groups of actions repeatedly without having to  retype all the code. You save 
typing, and it's easier to think about how to structure your program and to update it.

Create a file with following code in it.
```python3
def print_hello_world():
    """Hello World as a function"""
    print("Hello World")
```
Run the program, as you can see their aren't any result at the console. This is 
because we just declare function and didn't call it. 
```python3
print_hello_world()
``` 
Create a sum function that take two params **first** and **second**
```python3
def sum(first, second):
    return first+second
print(sum(12,20))
```
- [ ] Create a function that **subtract** to numbers  **first** and **second**
- [ ] Create a function that **divide** to numbers  **first** and **second**
- [ ] Create a function that **multiply** to numbers  **first** and **second**
- [ ] Create a program that ask a user for operation then for two numbers and perform the math operation

## Comments 
When writing code in Python, it’s important to make sure that your code 
can be easily understood by others. Giving variables obvious names, 
defining explicit functions, and organizing your code are all great ways to do this.

Another awesome and easy way to increase the readability of your code is 
by using comments!
```python3
def sum(first, second):
    """
    This function apply sum operation between first and second arguments
    """
    return first+second
```
- [ ] Add comments to all functions for previous point 

## Use the guess number game that we created in previous lecture
- [ ] Create function called **do_guess_round** and extract all code related to guess in that new function
- [ ] Stop the game when we find the correct number
- [ ] Create rounds between you and the computer
- [ ] Extract all string into constants. (Constant need to be with capital letter)
- [ ] When a round finished add message to user about round number 
- [ ] When a round finished show message to user **Are you sure you want to quit (Y/N)**
- [ ] If user insert **Y** then the program finish, if you type **N** the game continue with next round

## Use turtle as external library
Purtle graphics is a popular way for introducing programming to kids. 
It was part of the original Logo programming language developed by Wally Feurzig and Seymour Papert in 1966. 
```python3
from turtle import *

shape("turtle")
fd(100)
lt(90)

done()
```
- fd(number) is a function that move your character 100 symbols forward
- lt(degrees) is a function that turn on left on specific degrees

- [ ] Create a square using the turtle module
- [ ] Create a isosceles triangle using the turtle module
- [ ] Create a оctagon using the turtle module

- If you want to fill your figure you need to use following functions:-
    - color(collorName) to choice the collor
    - begin_fill() to start filling. This function need to be call before any drawing
    - end_fill() to end the filling. This function need to be call after all drawing functions.

- [ ] Create a square that is with color red
- [ ] Ask user for to insert the color name via terminal, then create a square with that color
- [ ] Ask user for to insert the color name via terminal, then create a decagon with that color
 