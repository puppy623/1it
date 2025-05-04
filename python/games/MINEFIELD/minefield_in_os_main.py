# minefield
# 1.0.0

import sys
import os
import random
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    for row in board:
        print(" ".join(row))

def create_board(size):
    board = []
    for i in range(size):
        board.append(["O"] * size)
    return board

def place_mines(board, num_mines):
    for i in range(num_mines):
        x = random.randint(0, len(board) - 1)
        y = random.randint(0, len(board) - 1)
        board[x][y] = "X"
    return board

def get_user_input():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    return x, y

def get_mine_count(board, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x + i < 0 or x + i >= len(board) or y + j < 0 or y + j >= len(board):
                continue
            if board[x + i][y + j] == "X":
                count += 1
    return count

def main():
    size = 5
    num_mines = 5
    board = create_board(size)
    board = place_mines(board, num_mines)
    print_board(board)
    while True:
        x, y = get_user_input()
        if board[x][y] == "X":
            print("You lose!")
            break
        else:
            board[x][y] = str(get_mine_count(board, x, y))
            print_board(board)
            if all([all([cell != "O" for cell in row]) for row in board]):
                print("You win!")
                break

if __name__ == "__main__":
    main()

# WIP


