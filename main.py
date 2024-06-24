from play_game import *

def main():
    """
    主函数，用于启动五子棋游戏。

    Main function to start the Gobang game.
    """
    # 启动游戏并设置玩家策略
    # Start the game with specified player strategies
    
    # 方式1：人类玩家对战人类玩家
    # Mode 1: Human player vs. Human player
    # play_game(goBang(), dict(X=human_mouse_player, O=human_mouse_player), verbose=False).utility
    
    # 方式2：AI玩家（alpha-beta搜索）对战人类玩家
    # Mode 2: AI player (alpha-beta search) vs. Human player
    play_game(goBang(), dict(X=player(limited_alphabeta_search), O=human_mouse_player), verbose=False).utility
    
    # 方式3：人类玩家对战AI玩家（alpha-beta搜索）
    # Mode 3: Human player vs. AI player (alpha-beta search)
    # play_game(goBang(), dict(X=human_mouse_player, O=player(limited_alphabeta_search)), verbose=False).utility
    
    # 方式4：AI玩家（alpha-beta搜索）对战AI玩家（alpha-beta搜索）
    # Mode 4: AI player (alpha-beta search) vs. AI player (alpha-beta search)
    # play_game(goBang(), dict(X=player(limited_alphabeta_search), O=player(limited_alphabeta_search)), verbose=False).utility
    
    # 方式5：AI玩家（alpha-beta搜索）对战AI玩家（minimax搜索）
    # Mode 5: AI player (alpha-beta search) vs. AI player (minimax search)
    # play_game(goBang(), dict(X=player(limited_alphabeta_search), O=player(limited_minimax_search)), verbose=False).utility

if __name__ == '__main__':
    main()
