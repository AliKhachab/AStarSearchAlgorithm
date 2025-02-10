"""
Ali Khachab ID #1315669
Prof. Gass
Due Feb 28, 2025
Assignment 1 - A* Search on 8 Puzzle

Please note that this was done on Python version 3.10.12. If it does not work for you, you might be on an older version.
"""
from collections import deque


class State:
    def __init__(self, boardState, parentState, move, depth, cost):
        self.boardState = boardState
        self.parentState = parentState
        self.move = move
        self.depth = depth
        self.cost = cost # depth + heuristic = cost
    
    def __lt__(self, other): # For comparison purposes (i.e. if state1 < state2)
        return self.cost < other.cost
    
    def printBoard(self):
        for i in range(3):
            print(self.boardState[i])

    def isGoalState(self) -> bool:
        if self.boardState == EightPuzzle.FINAL_BOARD_STATE:
            return True
        return False

class EightPuzzle:
    FINAL_BOARD_STATE = [ 
        ["1", "2", "3"], 
        ["8", "X"v, "4"], 
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
    MOVES = {
        "UP": (-1, 0),
        "DOWN": (1, 0),
        "LEFT": (0, -1),
        "RIGHT": (0, 1)
    }
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
                    for j in range(3):
                        number = input(f"Please enter a number between 1-8 for the 8-puzzle board. If you would like to make it an empty space, please write X.\nThe current values in the board are: {str(setOfNumsInBoard)}. Do not repeat numbers.\n")
                        if (number in setOfNumsInBoard) or (number != "X" and (int(number) < 1 or int(number) > 8)) or (not number.isnumeric() and number != "X"):
                            raise ValueError
                        else: 
                            board[i].append(number)
                            setOfNumsInBoard.add(number)
                
                print(f"Your board looks like this:\n{str(board[0])}\n{str(board[1])}\n{str(board[2])}")
                break
            except ValueError:
                print("Please enter a valid input. Ensure that you did not repeat yourself, that the numbers are all between 1-8, and that the empty space is noted as 'X'.")
        return board
    
    @staticmethod
    def checkValidMove():
        pass


    @staticmethod
    def heuristicOfState(state: State) -> int:
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
        
        # Test heuristic
        print(EightPuzzle.heuristicOfState(State(board, None, None, 0, 0)))


if __name__ == "__main__":
    EightPuzzle.eightPuzzleSolver()