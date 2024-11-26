import tkinter as tk
from tkinter import messagebox  # Import messagebox

# Global variable to store the current player
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]  # 3x3 board to track moves

# Function to draw the Tic-Tac-Toe grid
def draw_grid(canvas):
    # Draw horizontal lines with a darker gray color
    canvas.create_line(100, 100, 400, 100, width=2, fill="#808080")
    canvas.create_line(100, 200, 400, 200, width=2, fill="#808080")
    canvas.create_line(100, 300, 400, 300, width=2, fill="#808080")
    canvas.create_line(100, 400, 400, 400, width=2, fill="#808080")
    # Draw vertical lines with a darker gray color
    canvas.create_line(100, 100, 100, 400, width=2, fill="#808080")
    canvas.create_line(200, 100, 200, 400, width=2, fill="#808080")
    canvas.create_line(300, 100, 300, 400, width=2, fill="#808080")
    canvas.create_line(400, 400, 400, 100, width=2, fill="#808080")

# Function to handle player moves
def player_move(event, canvas):
    global current_player

    # Calculate the row and column based on the mouse click position
    row = (event.y - 100) // 100
    col = (event.x - 100) // 100

    # Check if the spot is available
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "":
        # Mark the spot with the current player's symbol
        board[row][col] = current_player
        x_pos = 100 + col * 100 + 50
        y_pos = 100 + row * 100 + 50
        
        # Draw X or O in the appropriate spot with updated colors
        if current_player == "X":
            canvas.create_text(x_pos, y_pos, text="X", font=("Arial", 36, "bold"), fill="#0000FF")  # Blue for X
        else:
            canvas.create_text(x_pos, y_pos, text="O", font=("Arial", 36, "bold"), fill="#FF4500")  # OrangeRed for O
        
        # Check for a winner
        if check_winner():
            winner = current_player
            messagebox.showinfo("Game Over", f"Player {winner} wins!")  # Show winner in message box
            canvas.unbind("<Button-1>")  # Disable further clicks
            return  # End the function

        # Check for a tie
        if check_tie():
            messagebox.showinfo("Game Over", "It's a tie!")  # Show tie message
            canvas.unbind("<Button-1>")  # Disable further clicks
            return  # End the function

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Function to check if there's a winner
def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

# Function to check if the game is a tie
def check_tie():
    return all(cell != "" for row in board for cell in row)

# Function to reset the game
def reset_game(canvas):
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    canvas.delete("all")  # Clear the canvas
    draw_grid(canvas)  # Redraw the grid
    canvas.create_text(250, 50, text="Player X's turn", font=("Arial", 16), fill="#000000")  # Black text
    canvas.bind("<Button-1>", lambda event: player_move(event, canvas))  # Re-enable clicks

# Set up the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.configure(bg="#F5F5F5")  # Light gray background

# Create canvas widget for the game board with a sky blue background
canvas = tk.Canvas(root, width=500, height=500, bg="#87CEEB")
canvas.pack(pady=10)

# Draw the initial game grid
draw_grid(canvas)

# Add instructions with a darker color
canvas.create_text(250, 50, text="Player X's turn", font=("Arial", 16), fill="#2E8B57")  # SeaGreen color

# Bind the player move function to mouse clicks
canvas.bind("<Button-1>", lambda event: player_move(event, canvas))

# Add a button to reset the game with updated styling
reset_button = tk.Button(root, text="Reset Game", command=lambda: reset_game(canvas), bg="#de0ffff", fg="white", font=("Arial", 14))
reset_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
