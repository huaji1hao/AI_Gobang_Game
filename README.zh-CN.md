# 五子棋 AI

[English](README.md)

## 介绍

本项目实现了一个五子棋游戏，使用了极小化极大算法和alpha-beta剪枝算法的AI对手。游戏可以在人类玩家之间进行，也可以在人类玩家与AI之间进行，或者在两个AI之间进行。

## 特性

- **人类玩家对战人类玩家**: 和朋友一起玩五子棋。
- **人类玩家对战AI**: 测试你对抗AI对手的技能。
- **AI对战AI**: 观看两个AI之间的对决。

## 安装

1. 克隆仓库

    ```bash
    git clone https://github.com/huaji1hao/AI_Gobang_Game.git
    ```

2. 安装所需依赖

    ```bash
    pip install pygame
    ```

## 用法

运行 `main.py` 文件以启动游戏。你可以通过取消注释 `main` 函数中的相应行来选择不同的游戏模式。

```bash
python main.py
```
## 游戏模式

**人类玩家对战人类玩家:**

```python
play_game(goBang(), dict(X=human_mouse_player, O=human_mouse_player), verbose=False).utility
```

**人类玩家 vs AI (alpha-beta剪枝):**

```python
play_game(goBang(), dict(X=player(limited_alphabeta_search), O=human_mouse_player), verbose=False).utility
```

**AI (alpha-beta剪枝) vs 人类玩家:**

```python
play_game(goBang(), dict(X=human_mouse_player, O=player(limited_alphabeta_search)), verbose=False).utility
```

**AI (alpha-beta剪枝) vs AI (alpha-beta剪枝):**

```python
play_game(goBang(), dict(X=player(limited_alphabeta_search), O=player(limited_alphabeta_search)), verbose=False).utility
```

**AI (alpha-beta剪枝) vs AI (minimax搜索):**

```python
play_game(goBang(), dict(X=player(limited_alphabeta_search), O=player(limited_minimax_search)), verbose=False).utility
```



## 文件结构

- `visualization.py`: 包含使用Pygame可视化五子棋棋盘和棋子的代码。
- `board.py`: 定义了用于管理五子棋游戏状态的Board类。
- `game.py`: 实现了五子棋游戏的规则和逻辑。
- `search.py`: 实现了用于AI的极小化极大算法和alpha-beta剪枝算法。
- `play_game.py`: 提供了使用不同玩家（人类或AI）进行游戏的函数。
- `main.py`: 应用程序的入口点，用于启动游戏。
