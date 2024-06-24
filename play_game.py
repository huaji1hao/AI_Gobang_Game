from game import *
from search import *
import random
import main


def play_game(game, strategies: dict, verbose=False):
    """Play a turn-taking game. `strategies` is a {player_name: function} dict,
    where function(state, game) is used to get the player's move."""
    state = game.initial
    visualize = game.visualize

    while not game.is_terminal(state): 
        player = state.to_move
        move = strategies[player](game, state)
        state = game.result(state, move)
        visualize.draw_piece(move, visualize.BLACK if player == 'X' else visualize.WHITE)
        print('Player', player, ':', move)
        if verbose: 
            print(state)
    print('Game over: utility', game.utility(state, 'X'), 'for X')
    
    # exit or restart the GUI
    again = visualize.draw_end_screen(1 if game.utility(state, 'X') > 0 else 2 if game.utility(state, 'X') < 0 else 0)
    if again == 0:
        main()
    else:
        pygame.quit()
        sys.exit()

    return state

def random_player(game, state): 
    if state.to_move == 'O':
        color = "white"
    else:
        color = "black"
    (x,y)=random.choice(list(game.actions(state)))
    game.visualize.draw_piece((x,y),color)
    return (x,y)

def human_player(game, state):
    """Make a move by reading input."""
    print(state)
    print('Legal moves are', game.actions(state))
    move = None
    while move not in game.actions(state):
        move = eval(input('Your move? '))
    # vis.draw_piece(move,"black")
    print(move)
    return move

def human_mouse_player(game, state):
    """Make a move by reading input."""
    move = None
    while move not in game.actions(state):
        move= game.visualize.get_input()
    return move

def player(search_algorithm):
    """A game player who uses the specified search algorithm"""
    return lambda game, state: search_algorithm(game, state)[1]