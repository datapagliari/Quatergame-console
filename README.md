'Quater-Cards'
A game about multiplying quaternion-like numbers

------------------------------------------------

Made in python3
For playing in the command line

------------------------------------------------

QUATERNION?:
A quaternion is an hiper-complex number, of the form A + B*i + C*j + D*k.
Like the complex numbers A+B*i, with two new imaginary variables.
Where: i*i = j*j = k*k = -1
And also: i*j*k = -1

CARDS:
Here, we play with cards with particular numbers, like: 3*i*j, -4*k, or 1*j*k, which is the same as just j*k. 
There are also numbers without imaginay part.
There are 32 cards, from 1 to 4*i*j*k

RULES:
Each player will have three cards in their hands
There's only one scoreboard in the game:
Player 1 wins if the final score is a positive number. If it is negative, Player 2 wins.
In every turn, a card will be the jackpot accumulated

MOVEMENT:
Each player plays some of their cards (one minimun, once at the time), 
and multiply the numbers in the jackpot accumulated.
For example: if the number 3*i is in the jackpot, and I play the card -2*j*k, the product will be: 
-6*i*j*k = -6*(-1) = 6

If the product is a real number (with no values of i, j, or k), the player can score the jackpot.

As player 1's goal is end the game with a positive score, he'll try to get positive products.
Plater 2's, in opossition, will try to get negative products.
