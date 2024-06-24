# Gobang AI 五子棋 AI

## Introduction | 介绍

This project implements a Gobang (Five in a Row) game with an AI opponent using the minimax and alpha-beta pruning algorithms. The game can be played between two human players, a human player and an AI, or between two AIs.

本项目实现了一个五子棋游戏，使用了极小化极大算法和alpha-beta剪枝算法的AI对手。游戏可以在人类玩家之间进行，也可以在人类玩家与AI之间进行，或者在两个AI之间进行。

## Features | 特性

- **Human vs Human**: Play Gobang with a friend.
- **Human vs AI**: Test your skills against an AI opponent.
- **AI vs AI**: Watch two AIs compete against each other.



- **人类玩家对战人类玩家**: 和朋友一起玩五子棋。
- **人类玩家对战AI**: 测试你对抗AI对手的技能。
- **AI对战AI**: 观看两个AI之间的对决。

## Installation | 安装

1. Clone the repository | 克隆仓库

    ```bash
    git clone https://github.com/huaji1hao/AI_Gobang_Game.git
    ```

2. Install the required dependencies | 安装所需依赖

    ```bash
    pip install pygame
    ```

## Usage | 用法

Run the `main.py` file to start the game. You can choose different game modes by uncommenting the corresponding lines in the `main` function.

运行 `main.py` 文件以启动游戏。你可以通过取消注释 `main` 函数中的相应行来选择不同的游戏模式。

```bash
python main.py
```
## Game Modes | 游戏模式

**Human vs Human:**

```python
play_game(goBang(), dict(X=human_mouse_player, O=human_mouse_player), verbose=False).utility
```

**Human vs AI (alpha-beta search):**

```python
play_game(goBang(), dict(X=player(limited_alphabeta_search), O=human_mouse_player), verbose=False).utility
```

**AI (alpha-beta search) vs Human:**

```python
play_game(goBang(), dict(X=human_mouse_player, O=player(limited_alphabeta_search)), verbose=False).utility
```

**AI (alpha-beta search) vs AI (alpha-beta search):**

```python
play_game(goBang(), dict(X=player(limited_alphabeta_search), O=player(limited_alphabeta_search)), verbose=False).utility
```

**AI (alpha-beta search) vs AI (minimax search):**

```python
play_game(goBang(), dict(X=player(limited_alphabeta_search), O=player(limited_minimax_search)), verbose=False).utility
```



## File Structure | 文件结构

- `visualization.py`: Contains the code for visualizing the Gobang board and pieces using Pygame.
- `board.py`: Defines the Board class to manage the state of the Gobang game.
- `game.py`: Implements the rules and logic for the Gobang game.
- `search.py`: Implements the minimax and alpha-beta pruning algorithms for the AI.
- `play_game.py`: Provides functions to play the game with different players (human or AI).
- `main.py`: The entry point of the application to start the game.



- `visualization.py`: 包含使用Pygame可视化五子棋棋盘和棋子的代码。
- `board.py`: 定义了用于管理五子棋游戏状态的Board类。
- `game.py`: 实现了五子棋游戏的规则和逻辑。
- `search.py`: 实现了用于AI的极小化极大算法和alpha-beta剪枝算法。
- `play_game.py`: 提供了使用不同玩家（人类或AI）进行游戏的函数。
- `main.py`: 应用程序的入口点，用于启动游戏。



## License | 许可证

This project is licensed under the MIT License.

本项目采用MIT许可证。

## Contributing | 贡献

Contributions are welcome! Please fork the repository and submit a pull request.

欢迎贡献代码！请fork仓库并提交pull request。

## Acknowledgments | 致谢

- Pygame: The library used for game visualization.
- All contributors and developers who made this project possible.



- Pygame: 用于游戏可视化的库。
- 所有让这个项目成为可能的贡献者和开发者