# Lecture 2
## Plan the game
In the quessing game, Python thinks of a random number. The player guesses the number.
1) If the player guesses correctly, Python says so
2) If the player guesses incorrectly, Python says whether the number is higher or lower.

### Ask for input
In practice, your program will always need some kind of input from the user.
You are still using the command line right now, so text is the only way to get input.
You get text from a user by using a special build-in called `input`. It waits 
for the user to type something.
Exercises (for each example create file `lessesn-2-project7-{tasknumber}`):
- [X] Ask user for `What is your guess? ` and save the result into variable called `players_guess`
- [X] Print the result from previews task 
- [X] Try to add 5 into variable of the first task

### Compare the guess to a Number
As you expect, `players_guess` is `17` (String value). Now is the type to change the type
of the inserted value to be a number.
```python3
players_quess = input("What is your guess? ")
print(int(players_quess)+10)
```
- [X] Create a variable called `computer_number` and assigned it some number
- [X] Ask user to guess a number `What is your guess?` and save the value into variable called `players_guess`
- [X] Compare `computer_number` and `players_quess`, if they are equals show message to user `Correct!`
- [X] If the `computer_number` is highest than `players_quess` print the message `Too low`
- [X] If the `computer_number` is less than `players_quess` print the message `Too high`

### Keep Asking until the player guesses correctly
Now you know hot to ask for the players guess, how to convert (change) the answer into a number,
and how to compare the player's answer to the computer's number.

You still need to set up something up that the computer keeps asking if the player doesn't
guess the number.

Do you remember how we create infinity loop from previous lessen: 
```python3
while True:
    print("Python ")
```
Now is the time to learn what key world `break` do. 
```python3
while True:
    print("Python ")
    break
```
As you can see of the example. Now the application printed only once `Python`.
- [X] Let's modified the the guessing game to kept asking for a number
- [X] Play the game three-time and count the number of tries until you guess the number
- [ ] Extend the game to do that part of the game

Now the game is so simple because we as developers give value to `computer_number`

### Make Python think of a random number
The player's guessing numbers. How do you get Python to think of a number?

The random integer feature randint is from the random module. It gives you a random number 
between two numbers that you put in the parenthesis that follows randint.
The number will include the lowest or highest number. 

```python3
import random
print(random.randint(1,100))
```

- [X] Create a program that print random number from 10 to 1000
- [X] Create a program that print random number from -100 to 100
- [X] Create a program that ask user for min and max number then generate random number
- [ ] Create a program that ask user for min and max number then generate 10 differents numbers

### Change the game to use random
- [X] Now is the time to change the game to use random number between 1 and 100

### Nested loops
A nested loop is a loop within a loop, an inner loop within the body of an outer one. 
How this works is that the first pass of the outer loop triggers the inner loop, which executes to completion. 
Then the second pass of the outer loop triggers the inner loop again. This repeats until the outer loop finishes.

```python3
for x in range(1,11):
    for y in range(1, 11):
        print(y, end= '\t')
    print()
```
- [ ] Create a program that use nested loops and the result need to be 
```
1	2	3	4	5	6	7	8	9	10	
2	4	6	8	10	12	14	16	18	20	
3	6	9	12	15	18	21	24	27	30	
4	8	12	16	20	24	28	32	36	40	
5	10	15	20	25	30	35	40	45	50	
6	12	18	24	30	36	42	48	54	60	
7	14	21	28	35	42	49	56	63	70	
8	16	24	32	40	48	56	64	72	80	
9	18	27	36	45	54	63	72	81	90	
10	20	30	40	50	60	70	80	90	100	
```

### Find the max/min number
- [X] Create a program that ask user for two numbers and then return the max number between them
- [ ] Create a program that ask user for three numbers and then return the max number between them
- [ ] Create a program that ask user for three numbers and then return the min number

### Sort three numbers
- [ ] Create a program that ask user for three numbers and then sort them (use only exchange values)