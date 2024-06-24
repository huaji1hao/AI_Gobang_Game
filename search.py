from visualization import *
import math

def limited_minimax_search(game, state, DEPTH_LIMIT = 2):
    """Search game tree to determine best move; return (value, move) pair. DEPTH_LIMIT is the depth limit of the search tree."""
    player = state.to_move

    def max_value(state, DEPTH_LIMIT):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()   
        if game.is_terminal(state) :
             return game.utility(state, player), None
        v, move = -infinity, None
        place = game.actions(state)
        for a in place:
            if game.has_neibour(a, place):  
                if DEPTH_LIMIT == 0: 
                    # A decision tree whose size is the depth power of the current number of pieces on the field
                    return game.board_score(state, a), None
                if DEPTH_LIMIT != 0:
                    v2, _ = min_value(game.result(state, a), DEPTH_LIMIT - 1)
                if v2 > v:
                    v, move = v2, a
        return v, move

    def min_value(state, DEPTH_LIMIT):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()   
        if game.is_terminal(state):
             return game.utility(state, player), None
        v, move = +infinity, None
        place = game.actions(state)
        for a in place:
            if game.has_neibour(a,place):
                if DEPTH_LIMIT == 0:
                    # Since it is the opponent's node, take the negative
                    return -game.board_score(state, a), None
                if DEPTH_LIMIT != 0:
                    v2, _ = max_value(game.result(state, a), DEPTH_LIMIT-1)
                if v2 < v:
                    v, move = v2, a        
        return v, move
    v, move = max_value(state, DEPTH_LIMIT)
    return v, move

infinity = math.inf

def limited_alphabeta_search(game, state, DEPTH_LIMIT = 2):
    """Search game to determine best action; use alpha-beta pruning. DEPTH_LIMIT is the depth limit of the search tree."""

    player = state.to_move
    game.now_board = True
    game.is_strong(state)
    
    def max_value(state, alpha, beta, DEPTH_LIMIT):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()   
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = -infinity, None
        place = game.actions(state)
        for a in place:
            if game.has_neibour(a, place): 
                if DEPTH_LIMIT == 0:
                    # A decision tree whose size is the depth power of the current number of pieces on the field
                    return game.board_score(state, a), None
                if DEPTH_LIMIT != 0:
                    v2, _ = min_value(game.result(state, a), alpha, beta, DEPTH_LIMIT - 1)
                if v2 > v:
                    v, move = v2, a
                    alpha = max(alpha, v)
                if alpha >= beta: # beta cut-off
                    return v, move
                
        return v, move

    def min_value(state, alpha, beta, DEPTH_LIMIT):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()   
        if game.is_terminal(state):
            return game.utility(state, player), None
        v, move = +infinity, None
        place = game.actions(state)
        for a in place:
            if game.has_neibour(a, place):
                if DEPTH_LIMIT == 0:
                    # Since it is the opponent's node, take the negative
                    return -game.board_score(state, a), None
                if DEPTH_LIMIT != 0:
                    v2, _ = max_value(game.result(state, a), alpha, beta,DEPTH_LIMIT-1)
                if v2 < v:
                    v, move = v2, a
                    beta = min(beta, v)
                if beta <= alpha: # alpha cut-off
                    return v, move
                
        return v, move

    v, move = max_value(state, -infinity, +infinity, DEPTH_LIMIT)
    
    return v, move