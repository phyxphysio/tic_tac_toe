import random

#Create gameboard
gameboard = '1|2|3\n4|5|6\n7|8|9'
winning_positions = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
winning_indices = [[gameboard.index(str(x)) for x in arr] for arr in winning_positions]

#Get input
def choose_symbol():
    player_symbol = None
    approved_symbols = ['x','o']
    while player_symbol not in approved_symbols:
        player_symbol = input('Welcome to tic tac toe!\nType x or o to choose your symbol.')
        if player_symbol not in approved_symbols:
            print('Invalid symbol. Choose either x or o.')
    print(gameboard)

    opponent_symbol = 'o' if player_symbol == 'x' else 'x'
    return player_symbol, opponent_symbol

def play(gameboard, player_symbol,opponent_symbol):
    
    #Opponent Moves
    possible_positions = [char for char in gameboard if char.isnumeric()]
    move = random.choice(possible_positions)
    print(f'Your opponent is placing an {opponent_symbol} at position {move}...')
    gameboard = gameboard.replace(move, opponent_symbol)
    if check_winner(gameboard, player_symbol, opponent_symbol):
        print(gameboard)
        play_again()
        return
    if is_draw(gameboard):
            print("It's a draw!")
            play_again()
            return

    print(gameboard) 

    #Player Moves
    position = input('Type a number to place your symbol there.')
    if position in gameboard and position.isnumeric():
        print(f'Placing {player_symbol} at position {position}...')
        gameboard = gameboard.replace(str(position), player_symbol)
        print(gameboard)
        if check_winner(gameboard, player_symbol, opponent_symbol):
            play_again()
            return
        

    else:
        print('That is not a valid position, try again!')
        play(gameboard, player_symbol, opponent_symbol)

    #Start next round
    play(gameboard, player_symbol, opponent_symbol)


    possible_positions = [char for char in gameboard if char.isnumeric()]
    move = random.choice(possible_positions)
    print(f'Your opponent is placing an {opponent_symbol} at position {move}...')
    gameboard = gameboard.replace(move, opponent_symbol)
    if check_winner(gameboard):
        print(gameboard)
        return

def check_winner(gameboard, player_symbol, opponent_symbol):
    for arr in winning_indices:
        if gameboard[arr[0]] in [player_symbol, opponent_symbol]:
            first_symbol = gameboard[arr[0]]
            if gameboard[arr[1]] == first_symbol and gameboard[arr[2]] == first_symbol:
                print(f'{first_symbol} wins!')
                return True

def is_draw(gameboard):
    return not any(char.isnumeric() for char in gameboard)

def play_again():
    answer = None
    while answer not in ['y','n']:
        answer = input('Type y to play again and n to exit')
    if answer == 'y':
        start_game()
    else:
        return 

def start_game():
    player_symbol, opponent_symbol = choose_symbol()
    play(gameboard,player_symbol=player_symbol,opponent_symbol=opponent_symbol  )

if __name__ == '__main__':
    start_game()