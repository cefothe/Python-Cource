# Flappy Bird (Part 3)
## Why does the score go up so fast?
You’ve probably noticed now that when you fly through some pipes 
the score soars upwards for a short period, instead of just going up 1.

The reason is that the code we added is in the update function, 
which runs every frame. The code we added will increment the score 
if the bird is past the pipe. But the bird is past the pipe for the whole 
time it takes the pipe to get to the edge of the screen. Every single frame 
while Barry is past the pipe the score goes up one. This gives you an appreciation of 
how fast the computer is drawing frames!

## Let’s fix the crazy score
Instead of adding 1 point each time we pass the pipes, 
let’s number the pipes! We’ll assign a number to each pair of pipes and just 
set the score to be equal to that number when we go past.

At the beginning of the game the pipes on the screen are pair number 1.

Add this to the reset() function:
```python3
top_pipe.pair_number = 1
```
We’ll just keep track in the top pipe, 
we know the bottom one will always be part of the same pair.

- [X] Every time when we create move the pipe to the start position increase the pipe number
- [X] In the place where we check if the bird and the pipe, instead of increment the score,
just assign the `top_pipe.pair_number`
- [X] Try the game, now when you go to pass some pipe the score is increase only by 1

## Make different gaps size
To make the game more interesting we want the gap between the pipes 
to be at a different y position each time. To do this we need to pick a random number.

- [X] Create new file called `test_random.py` and paste the following code their:
    ```python3
    import random
    print (random.randint(140,300))
    ```
  Execute the file couple of times to verify that every time you run it you see different numnber
-[X] Let's update the program programs to use the random for gaps.
    Find the 2 lines which do `left = WIDTH` for the pipes, and change them to:
    ```python3
    offset = 0
    top_pipe.midleft = (WIDTH,offset)
    bottom_pipe.midleft = (WIDTH,offset + top_pipe.height + gap)    
    ```  
-[ ] As you can see noting change at the moment, now we need to add random number to gap variable use 140 to 300

## It’s not Flappy Bird with out a flap
So far our bird image is very static and the game should probably
 just be called “Bird”. Let’s fix that now.
 
-[ ] Let's download those two images ![Bird dead](../lecture8/images/bird2.png)

-[ ] In order to create animation we need to change bir1 to bir2 when speed variable change.
But take to account that we need to that only when we a alive
    ```python3
    if barry_the_bird.alive:
        if barry_the_bird.speed > 0:
            barry_the_bird.image = "bird1"
        else:
            barry_the_bird.image = "bird2"
    ```
## Let's pipe show in different places
Now is the time to make `ofset` to be random as well. Use lower limit 140 and max limit 300

## Play the game
Can you see some problems. What happen when you with your score when you died.
- [ ] Your score doesn't start again and kept the previous result.
 When the reset function is called always change the  score to 0

- [ ] Add the end of the file create new variable called `best_result` equals to 0.
- [ ] Add check in `update` function that verify if the `barry_the_bird.score` is more than `best_result` if that is true 
assign to `best_result` value of `barry_the_bird.score`
- [ ] Show the best result value in the same as we did it for `barry_the_bird.score`

## Lives
Now is the time to implement lives, as the begging we have 3 lives. 
And we need to see for those lives what would be the better result 

