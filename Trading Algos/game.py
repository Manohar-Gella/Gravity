import tkinter as tk
from tkinter import messagebox

# Global variables
current_player = 'X'
board = [['' for _ in range(3)] for _ in range(3)]

def check_winner():
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return True
        if board[0][i] == board[1][i] == board[2][i] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

def check_draw():
    # Check if the board is full and there is no winner
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                return False
    return True

def on_click(row, col):
    global current_player

    if board[row][col] == '':
        board[row][col] = current_player
        button_grid[row][col].config(text=current_player)

        if check_winner():
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            reset_board()
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_board()
        else:
            current_player = 'X' if current_player == 'O' else 'O'

def reset_board():
    global current_player
    current_player = 'X'
    for i in range(3):
        for j in range(3):
            board[i][j] = ''
            button_grid[i][j].config(text='')

# Create the main application window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create the buttons grid
button_grid = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        button_grid[i][j] = tk.Button(root, text='', width=8, height=4,
                                      command=lambda row=i, col=j: on_click(row, col))
        button_grid[i][j].grid(row=i, column=j)

# Create a button to reset the game
reset_button = tk.Button(root, text="Reset", command=reset_board)
reset_button.grid(row=3, column=1, columnspan=3)

# Start the application
root.mainloop()
