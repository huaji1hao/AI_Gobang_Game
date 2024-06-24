from play_game import *

def main():
    # play_game(goBang(), dict(X=human_mouse_player, O=human_mouse_player), verbose=False).utility
    play_game(goBang(), dict(X=player(limited_alphabeta_search), O=human_mouse_player), verbose=False).utility
    # play_game(goBang(), dict(X=human_mouse_player, O=player(limited_alphabeta_search)), verbose=False).utility
    # play_game(goBang(), dict(X=player(limited_alphabeta_search), O=player(limited_alphabeta_search)), verbose=False).utility
    # play_game(goBang(), dict(X=player(limited_alphabeta_search), O=player(limited_minimax_search)), verbose=False).utility

if __name__ == '__main__':
    main()