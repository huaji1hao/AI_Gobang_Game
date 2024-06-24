from visualization import *
from board import *


class goBang():
    """Play goBang on an `height` by `width` board, needing `k` in a row (colomn or diagnoal) to win.
    'X' plays first against 'O'."""

    def __init__(self, height=16, width=16, k=5):
        self.height = height
        self.width = width
        self.k = k 
        self.catch = False
        self.attack = False
        self.now_board = False
        self.squares = {(x, y) for x in range(width) for y in range(height)}
        self.initial = Board(height=height, width=width, to_move='X', utility=0) #initially, the utility function is 0

        # visualize the game
        self.visualize = Visualize()
        self.visualize.draw_board()

    def actions(self, board):
        """Legal moves are any square not yet taken."""
        return self.squares - set(board)
    
    def result(self, board, square):
        """Place a marker for current player on square."""
        player = board.to_move
        board = board.new({square: player}, to_move=('O' if player == 'X' else 'X'))
        win = k_in_row(board, player, square, self.k)
        board.utility = (0 if not win else + pow(1000,self.k+1) if player == 'X' else -pow(1000,self.k+1))
        return board

    def utility(self, board, player):
        """Return the terminal state utility value corresponding to different players;
        pow(1000,6) for win, -pow(1000,6) for loss, 0 otherwise."""
        return board.utility if player == 'X' else -board.utility
    
    def is_terminal(self, board):
        """A board is a terminal state if it is won or there are no empty squares."""
        return board.utility != 0 or len(self.squares) == len(board)
    
    def has_neibour(self, square, place):  
        """Is this square has neibour?
        agent will not place a piece if it has no neibour pieces on the board
        this method can reduce the size of the problem by not examing pieces with no neibours"""
        
        x, y = square
        place_temp = place.copy() 

        # allow the first move to be placed as the neighbor of the center piece   
        if len(place_temp) == self.height*self.width:  # if the board is empty
            return True if (x, y) == (round(self.height/2) - 1, round(self.width/2) - 1) else False 
 
        for i in range(-1, 2):
            for j in range(-1, 2):
                 # identify the squares have neibour pieces
                if not ((x+i, y+j) in place_temp) and ((x+i, y+j) in self.squares):   
                    return True
        return False

    def board_status(self, board, player, k):
        """The method checking if player has k pieces in a line. 
         Along the line, count the number of one-side dead, two-side dead and life ending squares
         life => no piece on both ending sides of the line;
         one_dead => no piece on one ending side of the line;
         both_dead => both ending sides occupied
         """
        
        # The following variables define the number of live, sleeping and dead pieces
        life = 0
        one_dead = 0
        both_dead = 0

        # The following variables define how to detect multiple live pieces
        two = set()
        three = set()
        three_four = set()
        four = set()

        # all the pieces on the board
        history_steps = set(board)
        # my pieces on the board
        player_history_steps = set()
        for step in history_steps:
            if board[step] == player: player_history_steps.add(step)

        def add_to_two_set(points):
            for p in points:
                two.add(p)

        def add_to_three_set(points):
            for p in points:
                three.add(p)

        def add_to_three_four_set(points):
            for p in points:
                three_four.add(p)

        def add_to_four_set(points):
            for p in points:
                four.add(p)

        # Check if the positions are available for pieces
        def is_available(points): 
            for p in points:
                if p in history_steps or p not in self.squares: return False
            return True
        
        # Check if the positions are my pieces
        def self_pieces(points): 
            for p in points:
                if p not in player_history_steps: return False
            return True

        # Check if the position is endpoint
        def is_endpoint(point):
            (x, y) = point
            cnt = 0
            for (dx, dy) in ((0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)):
                if (x + dx, y + dy) in player_history_steps: 
                    cnt += 1
                    if (x - dx, y - dy) in player_history_steps: cnt -= 1
            return True if cnt == 0 or cnt == 1 or cnt == 2 else False
        decrease = 0.9
        for (x, y) in player_history_steps:
            if not is_endpoint((x, y)): continue
            for (dx, dy) in ((0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)):
                chs = []
                for i in range(-1, 6):
                    chs.append((x + i * dx, y + i * dy))
                # OOOOO Chinese Terminology as: 成五 
                if self_pieces([chs[1], chs[2], chs[3], chs[4], chs[5]]): 
                    life += 17454 if k == True else 9610
                # +OOOO+ Chinese Terminology as: 活四
                my_pieces = [chs[1], chs[2], chs[3], chs[4]]
                if is_available([chs[0], chs[5]]) and self_pieces(my_pieces): 
                    if self.catch == True and k == True: life += 500
                    add_to_three_four_set(my_pieces)
                    add_to_four_set(my_pieces)
                    life += 4731 if k == True else 3606
                # OOOO+ Chinese Terminology as: 连冲四
                my_pieces = [chs[1], chs[2], chs[3], chs[4]]
                if is_available([chs[5]]) and self_pieces(my_pieces): 
                    add_to_three_four_set(my_pieces)
                    add_to_four_set(my_pieces)
                    life += 2647 if k == True else 1961
                # +OOOO Chinese Terminology as: 连冲四
                my_pieces = [chs[1], chs[2], chs[3], chs[4]]
                if is_available([chs[0]]) and self_pieces(my_pieces): 
                    add_to_three_four_set(my_pieces)
                    add_to_four_set(my_pieces)
                    life += 2647 if k == True else 1961
                # OO+OO Chinese Terminology as: 跳冲四
                my_pieces = [chs[1], chs[2], chs[4], chs[5]]
                if is_available([chs[3]]) and self_pieces(my_pieces): 
                    add_to_three_four_set(my_pieces)
                    add_to_four_set(my_pieces)
                    life += 2647 if k == True else 1961
                # O+OOO Chinese Terminology as: 跳冲四
                my_pieces = [chs[1], chs[3], chs[4], chs[5]]
                if is_available([chs[2]]) and self_pieces(my_pieces): 
                    add_to_three_four_set(my_pieces)
                    add_to_four_set(my_pieces)
                    life += 2647 if k == True else 1961
                # OOO+O Chinese Terminology as: 跳冲四
                my_pieces = [chs[1], chs[2], chs[3], chs[5]]
                if is_available([chs[4]]) and self_pieces(my_pieces): 
                    add_to_three_four_set(my_pieces)
                    add_to_four_set(my_pieces)
                    life += 2647 if k == True else 1961
                # +OOO+ Chinese Terminology as: 连活三
                my_pieces = [chs[1], chs[2], chs[3]]
                if is_available([chs[0], chs[4]]) and self_pieces(my_pieces):
                    add_to_three_set(my_pieces)
                    add_to_three_four_set(my_pieces)
                    life += 1731 if k == True else 1525
                # +OO+O+ Chinese Terminology as: 跳活三
                my_pieces = [chs[1], chs[2], chs[4]]
                if is_available([chs[0], chs[3], chs[5]]) and self_pieces(my_pieces): 
                    add_to_three_set(my_pieces)
                    add_to_three_four_set(my_pieces)
                    life += 1547 if k == True else 1143 * decrease
                # +O+OO+ Chinese Terminology as: 跳活三
                my_pieces = [chs[1], chs[3], chs[4]]
                if is_available([chs[0], chs[2], chs[5]]) and self_pieces(my_pieces): 
                    add_to_three_set(my_pieces)
                    add_to_three_four_set(my_pieces)
                    life += 1547 if k == True else 1143 * decrease
                # O+O+O Chinese Terminology as: 眠三
                if is_available([chs[2], chs[4]]) and self_pieces([chs[1], chs[3], chs[5]]):
                    one_dead += 656 if k == True else 500 * decrease
                # +OOO Chinese Terminology as: 眠三
                if is_available([chs[0]]) and self_pieces([chs[1], chs[2], chs[3]]):
                    one_dead += 656 if k == True else 500
                # OOO+ Chinese Terminology as: 眠三
                if is_available([chs[4]]) and self_pieces([chs[1], chs[2], chs[3]]):
                    one_dead += 656 if k == True else 500
                # OO+O Chinese Terminology as: 眠三
                if is_available([chs[3]]) and self_pieces([chs[1], chs[2], chs[4]]):
                    one_dead += 656 if k == True else 500 * decrease
                # O+OO Chinese Terminology as: 眠三
                if is_available([chs[2]]) and self_pieces([chs[1], chs[3], chs[4]]):
                    one_dead += 656 if k == True else 500 * decrease
                # +OO+ Chinese Terminology as: 连活二
                my_pieces = [chs[1], chs[2]]
                if is_available([chs[0], chs[3]]) and self_pieces(my_pieces): 
                    add_to_two_set(my_pieces)
                    life += 453 if k == True else 242
                # +O+O+ Chinese Terminology as: 跳活二
                my_pieces = [chs[1], chs[3]]
                if is_available([chs[0], chs[2], chs[4]]) and self_pieces(my_pieces): 
                    add_to_two_set(my_pieces)
                    one_dead += 256 if k == True else 242 * decrease
                # +O++O+ Chinese Terminology as: 大跳活二
                my_pieces = [chs[1], chs[4]]
                if is_available([chs[0], chs[2], chs[3], chs[5]]) and self_pieces(my_pieces):
                    add_to_two_set(my_pieces)
                    one_dead += 256 if k == True else 242 * decrease
                # +OO Chinese Terminology as: 眠二
                if is_available([chs[0]]) and self_pieces([chs[1], chs[2]]):
                    one_dead += 120 if k == True else 75
                # OO+ Chinese Terminology as: 眠二
                if is_available([chs[3]]) and self_pieces([chs[1], chs[2]]):
                    one_dead += 120 if k == True else 75
                # +O+ Chinese Terminology as: 活一
                if is_available([chs[0], chs[2]]) and self_pieces([chs[1]]):
                    life += 42 if k == True else 26
                # +O Chinese Terminology as: 眠一
                if is_available([chs[0]]) and self_pieces([chs[1]]):
                    both_dead += 5 if k == True else 8
                # O+ Chinese Terminology as: 眠一
                if is_available([chs[2]]) and self_pieces([chs[1]]):
                    both_dead += 5 if k == True else 8

        # Extra bonus when there are multiple live pieces on the field
        if len(four) > 4: 
            life += 800 if k == True else 800 
        if len(three_four) > 4: 
            life += 700 if k == True else 700
            if board.to_move == player and self.now_board == True: self.catch = True
        if len(three) > 3: 
            life += 600 if k == True else 600
            if board.to_move == player and self.now_board == True: self.catch = True

        return life, one_dead, both_dead
        
    def get_heuristic_score(self, board, player):
        """Estimate non-terminal board's utility, given the current player.
        Taking the 'board status' into consideration, estimation utility value as a score evaluating the posibility of the player winning the game.
        Return the socre."""

        score = 0
        # Determine whether my side is attacking or the enemy is attacking
        k = self.attack
        
        life, one_dead, both_dead = self.board_status(board, player, k)

        # Give different levels of rewards to live, sleep and dead pieces
        score += life * 1
        score += one_dead * 1
        score += both_dead * 1
        
        return score

    def board_score(self, board, square):
        """Utilize the heuristic method to estimate the utility of the game board
        that applying potential move specified by `squre`. 
        The new board's utility estimation takes both players into consideration. """
        
        player = board.to_move
        
        # update the board by performing the move specified by squre
        board = board.new({square: player}, to_move=('O' if player == 'X' else 'X'))
        # calculate the board estimated utility taking both 
        adjust_weight = 2.4  # you can try a different adjust_weight to see what will happen
        self.attack = True
        board_score = self.get_heuristic_score(board, player) 
        self.attack = False
        board_score -= adjust_weight * self.get_heuristic_score(board, ('O' if player == 'X' else 'X'))
        return board_score
    
    def display(self, board): print(board)

    def is_strong(self, board):
        # determine whether the now_board has a three-three or three-four or four-four
        _, _, _ = self.board_status(board, board.to_move, self.attack)
        self.now_board = False


def k_in_row(board, player, square, k):
    """True if player has k pieces in a line through square."""
    def in_row(x, y, dx, dy): return 0 if board[x, y] != player else 1 + in_row(x + dx, y + dy, dx, dy)
    return any(in_row(*square, dx, dy) + in_row(*square, -dx, -dy) - 1 >= k
               for (dx, dy) in ((0, 1), (1, 0), (1, 1), (1, -1)))
