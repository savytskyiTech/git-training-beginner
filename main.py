def print_board(board):
	for row in board:
		print(" | ".join(row))
		print("-" * 5)

def check_winner(board, player):
	# Check rows, columns, and diagonals
	for i in range(3):
		if all([cell == player for cell in board[i]]):
			return True
		if all([board[j][i] == player for j in range(3)]):
			return True
	if all([board[i][i] == player for i in range(3)]):
		return True
	if all([board[i][2 - i] == player for i in range(3)]):
		return True
	return False

def is_full(board):
	return all([cell != " " for row in board for cell in row])

def tic_tac_toe():
	board = [[" " for _ in range(3)] for _ in range(3)]
	current_player = "X"
	while True:
		print_board(board)
		print(f"Player {current_player}'s turn.")
		try:
			row = int(input("Enter row (0, 1, 2): "))
			col = int(input("Enter col (0, 1, 2): "))
		except ValueError:
			print("Invalid input. Please enter numbers 0, 1, or 2.")
			continue
		if row not in range(3) or col not in range(3):
			print("Invalid position. Try again.")
			continue
		if board[row][col] != " ":
			print("Cell already taken. Try again.")
			continue
		board[row][col] = current_player
		if check_winner(board, current_player):
			print_board(board)
			print(f"Player {current_player} wins!")
			break
		if is_full(board):
			print_board(board)
			print("It's a draw!")
			break
		current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
	tic_tac_toe()
