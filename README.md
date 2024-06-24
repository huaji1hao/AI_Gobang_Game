# Gobang AI

[中文版 zh-CN](README.zh-CN.md)

## Introduction

This project implements a Gobang (Five in a Row) game with an AI opponent using the minimax and alpha-beta pruning algorithms. The game can be played between two human players, a human player and an AI, or between two AIs.

## Features

- **Human vs Human**: Play Gobang with a friend.
- **Human vs AI**: Test your skills against an AI opponent.
- **AI vs AI**: Watch two AIs compete against each other.

## Installation

1. Clone the repository

    ```bash
    git clone https://github.com/huaji1hao/AI_Gobang_Game.git
    ```

2. Install the required dependencies

    ```bash
    pip install pygame
    ```

## Usage

Run the `main.py` file to start the game. You can choose different game modes by uncommenting the corresponding lines in the `main` function.

```bash
python main.py
```
## Game Modes

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

## File Structure

- `visualization.py`: Contains the code for visualizing the Gobang board and pieces using Pygame.
- `board.py`: Defines the Board class to manage the state of the Gobang game.
- `game.py`: Implements the rules and logic for the Gobang game.
- `search.py`: Implements the minimax and alpha-beta pruning algorithms for the AI.
- `play_game.py`: Provides functions to play the game with different players (human or AI).
- `main.py`: The entry point of the application to start the game.

## Showcase

<img src="https://eumcm.com/file/59f01c88a0176af796468.png" width="560" height="560" />
