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
- [ ] Create a program that print your name
- [ ] Create a program that print your name and your age
- [ ] Create a program that print your country name

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
- [ ] Create a program with infinity loop that print your name
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
- [ ] Create a program that print all numbers from 1 to 1000
- [ ] Create a program that print all even numbers from 1 to 1000
- [ ] Create a program that print all odd numbers from 1 to 1000
- [ ] Create a program that print all  numbers from 1000 to 1
- [ ] Create a program that print all even numbers from 1000 to 1
- [ ] Create a program that print all odd numbers from 1000 to 1
- [ ] Create a program that print `Hello World` 300 times

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