''' 
Steps in the function maybe not in ordered manner but I had given the name of the steps as I had created the game.
Follow the steps according to its number as it will help you more to understand the code. It will give you the same logic that I had used while designing this game.
'''

# Step-1: Designing Tic Tac Toe grid function
def tictactoe_grid(value):  
# printing the first three boxes of the 3X3 game board   
    print("\n")  
    print("\t      |      |")  
    print("\t    {} |  {}   |  {}".format(value[0], value[1], value[2]))  
    print('\t______|______|______')  
    print("\t      |      |") 
# printing the second three boxes of the 3X3 game board   
    print("\t   {}  |  {}   |  {}".format(value[3], value[4], value[5]))  
    print('\t______|______|______')  
    print("\t      |      |")
# printing the last three boxes of the 3X3 game board
    print("\t  {}   |  {}   |  {}".format(value[6], value[7], value[8]))  
    print("\t      |      |")  
    print("\n")

# tictactoe_grid("123456789") #Printing basic values and checking of the function is working or not

# STEP - 9: Designing Scorecard

# Defining my_scoreboard named function for displaying the score at the end
def my_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t         The SCORES       ")
    print("\t--------------------------------")
   
    list_of_the_two_players = list(score_board.keys())
    print("\t   ", list_of_the_two_players[0], "\t    ", score_board[list_of_the_two_players[0]])
    print("\t   ", list_of_the_two_players[1], "\t    ", score_board[list_of_the_two_players[1]])
   
    print("\t--------------------------------\n")

# STEP - 5: Validating the Win or Tie Situation

# Creating a win_validate named function to check for player win
def win_validate(position_player, player_current):
    win_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    for i in win_combinations:
        all_elements_present = True
        for j in i:
            if j not in position_player[player_current]:
                all_elements_present = False
                break
        if all_elements_present:
            return True
    return False

# Creating a tie validate function to check for player tie
def tie_validate(position_player):  
    if len(position_player['X']) + len(position_player['O']) == 9:  
        return True  
    return False

# STEP - 2: Using Data Structure to Store Data. We will be storing two data basically, 1st: Status of Grid and 2nd: The move of each player

def game_single(player_current):
# The player_current variable is used to store the move of the current player as 'X' or 'O'.
# function to highl  
    value = [' ' for i in range(9)]

# Using the data structure to store the filled positions denoted by X and O
    position_player = {'X' : [], 'O' : []}

# STEP - 3: Game Loop
    while True:
        tictactoe_grid(value)
        # Below trying to take input from the user and handling all possible exceptions that can occur.
        try:
            print(player_current, "turn. (CHOOSE YOUR BLOCK): ", end="")
            turn = int(input())
        except ValueError:
            print("Invalid Input! Please try again..")
            continue
        
        if (turn<1 or turn>9):
            print("Invalid Input(Enter value between 1-9)! Please try again..")
            continue

        if (value[turn-1] != " "):
            print("Position already filled! Please try again..")
            continue

    # STEP - 4: Updating Game Information

        # Updating the status of GameBoard
        value[turn-1] = player_current
        # Update the player's position on the grid
        position_player[player_current].append(turn)

        # Calling the UDF win_validate function to check for win
        if win_validate(position_player, player_current):
            tictactoe_grid(value)
            print("Congratulations!", player_current, "\nYou won the match.\n")
            return player_current

        # Calling the UDF tie_validate function to check for tie
        if tie_validate(position_player):
            tictactoe_grid(value)
            print("Good Game! The game has tied.\n")
            return 'D'
        
    # STEP - 6: Switching between the player (once chance of one player is executed)

        # Using if-else statement to make the switch between the players
        if (player_current == 'X'):
            player_current = 'O'
        else:
            player_current = 'X'

# STEP - 7: Recording player's name to observe on the Scorecard

if __name__ == "__main__":
    first_player = input("Enter Your Name (First Player): ")
    print('\n')
    second_player = input("Enter Your Name (Second Player): ")
    print('\n')

# STEP - 8: Capturing the game information

    # Capturing the player who chooses the X and O
    player_current = first_player

    # Capturing the player's choice
    player_choice = {'X' : "", 'O' : ""}

    # Storing the two possible options available
    option = ['X', 'O']

    # Storing the information that needs to be captured in the scoreboard
    score_board = {first_player: 0, second_player: 0}
    my_scoreboard(score_board)

# STEP - 10: Outer loop to make game flexible and allow multiple games

    # Using the while function for adding multiple series of games until the players call it an exit.
    while True:
    # Display menu for the players
        print(player_current, "you get the chance to make the choice for the series:")
        print("Please press 1 for X")
        print("Please press 2 for O")
        print("Please press 3 to Exit")

# STEP - 11: To Handle Exception and Allot the Selection of the Symbol for the Current Player for Each Iteration of the Game

        # The try-except block for the_turn input from the player  
        try:
            the_turn = int(input())     
        except ValueError:  
            print("This input is Invalid!!! Please Try Again\n")  
            continue  
        
        # if Elif else loop to define the condition for the selection made.   
        if the_turn == 1:  
            player_choice['X'] = player_current  
            if player_current == first_player:  
                player_choice['O'] = second_player  
            else:  
                player_choice['O'] = first_player  
        
        elif the_turn == 2:
            player_choice['O'] = player_current
            if player_current == first_player:
                player_choice['X'] = second_player
            else:
                player_choice['X'] = first_player

        elif the_turn == 3:
            print("Thanks for playing the game! Mayank Singh is Congratulating you for completing the round.")
            print("The final scores are:")
            my_scoreboard(score_board)
            break

        else:
            print("This is an Invalid choice!! Please try again\n")

# STEP - 12: Execution of the Game and Updating the Scoreboard Simultaneously

        # Capturing the winner of the single game
        winner = game_single(option[the_turn - 1]) 


        # As per the scores obtained the winner is getting updated on the scoreboard  
        if winner != 'D' :  
            player_won = player_choice[winner]  
            score_board[player_won] = score_board[player_won] + 1 
        my_scoreboard(score_board)

        # STEP - 13: Swapping the Chance Given to Choose the Symbol Between the Selecting Player

        # Swapping between the players after each game for who will choose X or O  
        if player_current == first_player:  
            player_current = second_player  
        else:  
            player_current = first_player