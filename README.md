# What this project is about

This script was done for my Intro to AI class in college. We reviewed informed and uninformed search, and the homework assignment was to code up our own A* search algorithm for the 8-puzzle, a game where you can take a set of 8 tiles and one empty tile, like so:

8 3 5
4 1 6
2 7 X ( X is the empty tile ) 

and turn it into the "goal state" of

1 2 3
8 X 4
7 6 5.

As stated above, this code uses the A* algorithm to review heuristics and their influence on search. In particular, it made it very easy for my code to find the fastest solution thanks to the information it saved prior in the "parent state" attribute of each State object.

# How this program works

You can read the comments on my code for further info, but basically:
- The code uses the input() function to take in a board state from the user.
- The
