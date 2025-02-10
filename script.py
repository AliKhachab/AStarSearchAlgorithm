"""
Ali Khachab ID #1315669
Prof. Gass
Due Feb 28, 2025
Assignment 1 - A* Search on 8 Puzzle

Please note that this was done on Python version 3.10.12. If it does not work for you, you might be on an older version.
"""
import heapq
from copy import deepcopy

class State:
    def __init__(self, boardState, parentState, move, depth: int, cost: int):
        self.boardState = boardState
        self.parentState = parentState
        self.move = move
        self.depth = depth # "g" in the A* algorithm
        self.cost = cost # depth + heuristic = cost (basically, f (cost) = g (depth) + h (calculated from heuristic() function)
    
    def __lt__(self, other): # For comparison purposes (i.e. if state1 < state2)
        return self.cost < other.cost
    
    def printBoard(self):
        for i in range(3):
            print(self.boardState[i])

    def isGoalState(self) -> bool:
        if str(self.boardState) == str(EightPuzzle.FINAL_BOARD_STATE):
            return True
        return False

class EightPuzzle:
    # Common variables
    FINAL_BOARD_STATE = [ 
        ["1", "2", "3"], 
        ["8", "X", "4"], 
        ["7", "6", "5"] 
    ]
    FINAL_BOARD_STATE_DICT = { # Keep track of all the positions of the final numbers that we want
        "1": (0, 0),
        "2": (0, 1),
        "3": (0, 2),
        "8": (1, 0),
        "X": (1, 1),
        "4": (1, 2),
        "7": (2, 0),
        "6": (2, 1),
        "5": (2, 2)
    }
    MOVES = { "UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT": (0, 1) }
    
    @staticmethod
    def generateBoard():
        """
        This code sets up the board with user input. I.e.
        1 2 3
        4 5 6
        7 8 X
        """
        board = [[],[],[]]
        setOfNumsInBoard = set() 
        while True:
            try:
                for i in range(3):
                    for _ in range(3):
                        number = input(f"Please enter a number between 1-8 for the 8-puzzle board. If you would like to make it an empty space, please write X.\nThe current values in the board are: {str(setOfNumsInBoard)}. Do not repeat numbers.\n")
                        if (number in setOfNumsInBoard) or (number != "X" and (int(number) < 1 or int(number) > 8)) or (not number.isnumeric() and number != "X"):
                            raise ValueError
                        else: 
                            board[i].append(number)
                            setOfNumsInBoard.add(number)
                break
            except ValueError:
                print("Please enter a valid input. Ensure that you did not repeat yourself, that the numbers are all between 1-8, and that the empty space is noted as 'X'.")
        return board

    @staticmethod
    def heuristicOfState(state: State) -> int:
        """
        This function generates the Manhattan distance of the current state.
        """
        distance = 0
        for row in range(3):
            for col in range(3):
                if state.boardState[row][col] != "X":
                     current_number = state.boardState[row][col]
                     distance += (abs(row - EightPuzzle.FINAL_BOARD_STATE_DICT[current_number][0]) + abs(col - EightPuzzle.FINAL_BOARD_STATE_DICT[current_number][1]))
                else:
                    continue
        return distance
    
    @staticmethod
    def generatePossibleMoves(state: State) -> list[State]:
        """
        Find a list of all possible moves that can be made in the current state.
        First, find the position of the empty space (X). Then check all possible adjacent tiles (up down left right) to see if it does not go out of bounds of the arrays.
        If it is, add it to the list of possible moves.
        """
        res = []
        emptySpaceXValue = None
        emptySpaceYValue = None
        for i in range(3):
            for j in range(3):
                if state.boardState[i][j] == "X":
                    emptySpaceXValue = i
                    emptySpaceYValue = j
                    break
                
        for move in EightPuzzle.MOVES:
            newRow = emptySpaceXValue + EightPuzzle.MOVES[move][0]
            newCol = emptySpaceYValue + EightPuzzle.MOVES[move][1]
            if (newRow >= 0 and newRow < 3) and (newCol >= 0 and newCol < 3):
                copyBoard = deepcopy(state.boardState) # I had an issue with this part where I accidentally made a shallow copy instead of a deep copy of the array. This caused the board to be modified in the parent state as well, meaning that the X would only move along the column it started in..
                copyBoard[emptySpaceXValue][emptySpaceYValue], copyBoard[newRow][newCol] = copyBoard[newRow][newCol], copyBoard[emptySpaceXValue][emptySpaceYValue]
                # swap the positions of X and the space adjacent to it (up down left right)
                newDepth = state.depth + 1
                newCost = newDepth + EightPuzzle.heuristicOfState(State(boardState=copyBoard, parentState=state, move=move, depth=newDepth, cost=0))
                res.append(State(boardState = copyBoard, parentState = state, move = move, depth = newDepth, cost = newCost))                
        return res

    @staticmethod
    def eightPuzzleSolver() -> None:
        """
        This function solves the 8-puzzle problem using the A* algorithm.

        For reference, the final board state needs to be:
        [ ["1", "2", "3"],
        ["8", "X", "4"],
        ["7", "6", "5"]  ]
        """
        board = EightPuzzle.generateBoard()
        if board == EightPuzzle.FINAL_BOARD_STATE:
            print("The board is already in the final state. No moves needed.")
            return
        
        frontier = []
        initialState = State(boardState = board, parentState = None, move = None, depth = 0, cost = 0)
        heapq.heappush(frontier, initialState)
        seen = set()
        seen.add(str(frontier[0].boardState)) # You will notice later I use a string repr. of the list to check if it is in the set. This is because lists are not hashable, so I couldn't add it to the set in the first place.

        while frontier:
            currState = heapq.heappop(frontier)
            print(f"Current depth: {currState.depth}\nCurrent cost: {currState.cost}\nCurrent board state:")
            currState.printBoard()
            if currState.isGoalState():
                print("Goal state reached")
                return True
            else:
                possibleNextMoves = EightPuzzle.generatePossibleMoves(currState)
                print(f"Seen states: {seen}")
                # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                for newState in possibleNextMoves:
                    if str(newState.boardState) not in seen:
                        heapq.heappush(frontier, newState) # this is what the __lt__ function is for
                        seen.add(str(newState.boardState))
                        # print("--\nAdding to frontier:")
                        # newState.printBoard()
                # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        return False


if __name__ == "__main__":
    print("No solution") if not EightPuzzle.eightPuzzleSolver() else print("Solution displayed above")