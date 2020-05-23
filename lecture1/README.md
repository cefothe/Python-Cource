# Lecture 1
## Hello world - Project
Let's create your first file called `project1.py` and paste the following code
```python3
print("Hello World")
```
Then run your first file and verify the output. You need to have `Hello World` message.

Еxercises (for each example create file `project1-{tasknumber}`):
- [ ] Create a program that print your name
- [ ] Create a program that print your name and your age
- [ ] Create a program that print your country name

## Hello World - Project (Variables)
The `"Hello World"` that we use in previous example is called literal.
After Python defines a literal, it sort of forgets it. Python stores literals in
memory then thinks they aren't being used so throws them out in a process called
`garbage collection` 

Your name a literal like this:
1) Think up a name that follows the rules listed after those steps
2) Put the name on the left side of an equals sign(=)
3) Put the literal on the right side of the equals operator

Create a python file called `project2` and paste the following code
```python3
my_message = "Hello into Python course"
print(my_message)
``` 
Now lets create the same examples with variables.
Еxercises (for each example create file `project2-{tasknumber}`):
- [X] Create a program that print your name
- [X] Create a program that print your name and your age
- [X] Create a program that print your country name

Please think about good variables name.
## Loops (iteration)
Loops are traditionally used when you have a block of code which you want to repeat a fixed number of times. 
The Python for statement iterates over the members of a sequence in order, executing the block each time. 

### Infinite loops
Are you ready to create a program that never finished by itself.
```python3
while True:
    print("Python ")
```

Еxercises (for each example create file `project3-1-{tasknumber}`):
- [X] Create a program with infinity loop that print your name
- [ ] Create a program with infinity loop that print our academy name

### Repeat
Let's create a block of code that count to 100.
```python3
number = 1
while number <= 100:
    print(number)
    number = number+1
```
Еxercises (for each example create file `project3-2-{tasknumber}`):
- [X] Create a program that print all numbers from 1 to 1000
- [X] Create a program that print all even numbers from 1 to 1000
- [ ] Create a program that print all odd numbers from 1 to 1000
- [X] Create a program that print all  numbers from 1000 to 1
- [ ] Create a program that print all even numbers from 1000 to 1
- [ ] Create a program that print all odd numbers from 1000 to 1
- [X] Create a program that print `Hello World` 300 times

## Taking a decision with If-Else
Python supports the usual logical conditions from mathematics:
1) Equals: `a == b`
2) Not Equals: `a != b`
3) Less than: `a < b`
4) Less than or equal to: `a <= b`
5) Greater than: `a > b`
6) Greater than or equal to: `a >= b`

These conditions can be used in several ways, most commonly in `if statements` and loops.
An `if statement` is written by using the if keyword.

```python3
a = 33
b = 200
if b > a:
  print("b is greater than a")
```
Еxercises (for each example create file `project4-1-{tasknumber}`):
- [ ] Let's use the example in this section and change the condition to `equals`
 and the printed message should be `b is equals to a`. Don't forget to change a and b to be equals to 10

### Else and Elif
#### Elif  
The `elif` keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
```python3
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
```
#### Else
The `else` keyword catches anything which isn't caught by the preceding conditions.
```python3
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```

Exercises (for each example create file `project5-1-{tasknumber}`):
- [X] Create a program that have variable called `age`, then compare it with 10. If you are under 12,
 you need to see the message `You are to young for Python`. If you are up or equals to 12, you need to see the message `Let's start with Python`.
 
## Embedding Values in Strings
If you want to display a message using the contents of a variable, you can embed values in a string with `%s`, which is like a token for a value you want to add later. (Embedding Values is a programmer-talking about "inserting values.") 
For example, to have Python calculate or store the number of points you've scored in a game, and then add it to a sentence like "I scored points," use:
```python3
my_score = 100
message = "I scored %s points"
print(message % my_score)
```
You can embed more values
```python3
nums = "What did the number %s say to be number %s ? Nice Belt!!!"
print(nums % (0,8))
```
Exercises (for each example create file `project6-{tasknumber}`):
- [X] Create a program that need to have two variables. `firstName` and `lastName`, 
which contains information about your first and last name. For example my first name is
Stefan and my last name is Angelov, the output of the program need to be `My first name is Stefan and my last name is Angelov`
- [ ] Create a program that need to have three variables `a`, `b` and `c`. For example `a=5`
`b=10` and the output of the program need to be `a=5, b=10, a+b=15`
- [ ] Create a program that need to one variable `age` equals to your years. For example: I'm on 26, so 
 the output of the program need to be `My age is 26` 

## Ask for Input
In practice, your program will always need some kind of input from the user.
You are still using the command line right now, so text is the only way to get input.
You get text from a user by using a special build-in called `input`. It waits 
for the user to type something.
```python3
number = input('Insert your number ')
print("Your number is %s" % number)
```
Exercises (for each example create file `project7-{tasknumber}`):
- [X] Create a program that ask you for your name, store the result into variable and then print `My name is Stefan`
- [ ] Create a program that ask you for your age, store the result into variable and then print `My age is 26`
