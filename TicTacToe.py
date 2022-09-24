from IPython.display import clear_output

#BOARD
def display(row1):	
	clear_output()
	print(row1[0],"|", row1[1],"|", row1[2])
	print(row1[3],"|", row1[4],"|", row1[5])
	print(row1[6],"|", row1[7],"|", row1[8])

#POSITION SELECTION
def user_choice():
	# VARIABLES

	# Initial
	choice = ('initial_value')
	acceptable_range = range(1,11)
	within_range = False

	#TWO CONDIITONS TO CHECK
	# DIGIT OR WITHIN_RANGE == False
	while choice.isdigit() == False or within_range == False:
		choice = input("Please enter a number (1-9): (in relation to the position you want on the board)")
		
		#Digit Check
		if choice.isdigit() == False:
			print('Sorry that is not a digit')

		#Range Check
		if choice.isdigit() == True:
			if int(choice) in acceptable_range:
				within_range = True
			else: 
				within_range = False
				print('Sorry that is not within the acceptable range')
		
	return int(choice)-1

#CHOICE SELECTED
def replacement_choice(game_list, position, user_marker):
	while game_list[position] == 'X' or game_list[position] == 'O':
		print('This slot is already taken')
		position = user_choice()
	
	game_list[position] = user_marker
	return game_list

def player_input():
	marker = ''

	#KEEP ASKING PLAYER 1 to choose X or 0

	while marker != 'X' and marker != 'O':
		marker = input('Player 1, choose X or O: ').upper()

	player1 = marker

	if player1 == 'X':
		player2 = 'O'
	else:
		player2 = 'X'

	return (player1, player2)

#Continue playing
def gameon_choice():
	choice = 'wrong'

	while choice not in ['Y', 'N']:
		choice = input("Keep playing? (Y or N)").upper()

		if choice not in ['Y', 'N']:
			print("Sorry, I don't understand, please choose Y or N")

	if choice == 'Y':
		return True
	else:
		return False

#WINNER
def gamewinner_result(row):
	if row[0] == row[1] and row[2] == row[1]: 
		return True
	elif row[3] == row[4] and row[5] == row[4]: 
		return True
	elif row[6] == row[7] and row[8] == row[7]: 
		return True
	elif row[0] == row[3] and row[6] == row[3]: 
		return True
	elif row[1] == row[4] and row[7] == row[4]: 
		return True
	elif row[2] == row[5] and row[8] == row[5]: 
		return True
	elif row[0] == row[4] and row[8] == row[4]: 
		return True
	elif row[2] == row[4] and row[6] == row[4]: 
		return True
	else:
		return False

#TIE GAME
def tie_game(board):
	acceptable_values = ['X', 'O']
	count = 0

	for i in board:
		if i in acceptable_values:
			count += 1

	if count == len(board):
		return True
	else:
		return False

#PLAY
def game(game_on, game_winner, board, player1_marker, player2_marker):
	winner = 'Player'

	while game_winner == False:

		#check for TIE game
		if tie_game(board) == True:
			print('The game result is a tie!')
			break

		display(board)

		print('Player 1:')
		position = user_choice()
		board = replacement_choice(board, position, player1_marker)
		display(board)

		game_winner = gamewinner_result(board)
		
		if game_winner == True:
			winner = 'Player 1'
			break

		#check for TIE game
		if tie_game(board) == True:
			print('The game result is a tie!')
			return

		print('Player 2:')
		position = user_choice()
		board = replacement_choice(board, position, player2_marker)

		game_winner = gamewinner_result(board)
		winner = 'Player 2'

	print(winner, 'you win!')

#VARIABLES
game_on = True
game_winner = False
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


while game_on:
	player1_marker, player2_marker = player_input()
	game(game_on, game_winner, board, player1_marker, player2_marker)
	game_on = gameon_choice()
	board = [1, 2, 3, 4, 5, 6, 7, 8, 9]