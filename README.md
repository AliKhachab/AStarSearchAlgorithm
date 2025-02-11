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
- The code uses the input() function to take in a board state from the user. (I was originally planning on using a file to read and write from, and may add implementation for this later, but the homework's priority was just to get the A* search algorithm down, so I did not worry about it too much. It might be easier to record a log in this sort of file, though).
- Once a board is generated, it will check if the board that was inputted, for some reason, is equal to the final board state already, which case it will tell the user that the initial state = the final state.
- Afterwards, assuming the initial state != the final state, it will add the initial state to an array managed by the ```heapq``` class, which turns an array into a minheap using separate functions. The minheap then handles the state based on the ```__lt__()``` method in the ```State``` class, sorting each State by the heuristic + depth value. It will search through all possible solutions.

# What I want to implement after this
- The homework assignment was only to create an A* search algorithm that worked for the 8-puzzle, but there should be a way to calculate earlier whether or not an initial state is unsolvable. If so, I would like to see if I can make a checker for those calculations, since running all possible checks for all possible states can leave us with thousands of states searched just for no solution.
- Read-write file support instead of just input(). Makes it easier to write a log of sorts, too.

