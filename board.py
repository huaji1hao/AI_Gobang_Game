from collections import defaultdict

class Board(defaultdict):
    """
    棋盘类，包含当前要下棋的玩家、一个缓存的效用值，以及一个 {(x, y): player} 的字典，
    其中 player 是 'X' 或 'O'。
    
    A board has the player to move, a cached utility value, 
    and a dict of {(x, y): player} entries, where player is 'X' or 'O'.
    """
    empty = '.'  # 表示空位的符号 Symbol for an empty cell
    off = '#'    # 表示无效位置的符号 Symbol for an invalid position
    
    def __init__(self, width=16, height=16, to_move=None, **kwds):
        """
        初始化棋盘。
        
        Initialize the board.
        
        参数 Parameters:
        - width: 棋盘的宽度 Width of the board
        - height: 棋盘的高度 Height of the board
        - to_move: 当前要下棋的玩家 Player to move
        - kwds: 其他关键字参数 Other keyword arguments
        """
        self.__dict__.update(width=width, height=height, to_move=to_move, **kwds)
        
    def new(self, changes: dict, **kwds) -> 'Board':
        """
        根据给定的 {(x, y): contents} 变化字典，返回一个应用了这些变化的新棋盘。
        
        Given a dict of {(x, y): contents} changes, return a new Board with the changes.
        
        参数 Parameters:
        - changes: 要应用的变化字典 Dictionary of changes to apply
        - kwds: 其他关键字参数 Other keyword arguments
        
        返回 Returns:
        - 应用了变化的新棋盘 A new board with the applied changes
        """
        board = Board(width=self.width, height=self.height, **kwds)
        board.update(self)
        board.update(changes)
        return board

    def __missing__(self, loc):
        """
        当访问的键不存在时调用。返回对应位置的默认值。
        
        Called when the accessed key is missing. Returns the default value for the location.
        
        参数 Parameters:
        - loc: 位置 (x, y) Location (x, y)
        
        返回 Returns:
        - 对应位置的默认值 Default value for the location
        """
        x, y = loc
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.empty  # 如果在棋盘范围内，返回空位 If within board range, return empty cell
        else:
            return self.off    # 如果不在棋盘范围内，返回无效位置 If outside board range, return invalid position
            
    def __hash__(self):
        """
        计算棋盘的哈希值。基于棋盘状态和当前要下棋的玩家。
        
        Compute the hash value of the board. Based on the board state and the player to move.
        
        返回 Returns:
        - 棋盘的哈希值 Hash value of the board
        """
        return hash(tuple(self.items())) + hash(self.to_move)
    
    def __repr__(self):
        """
        返回棋盘的字符串表示。每一行由空格分隔的棋子组成。
        
        Return the string representation of the board. Each row consists of pieces separated by spaces.
        
        返回 Returns:
        - 棋盘的字符串表示 String representation of the board
        """
        def row(y): 
            return ' '.join(self[x, y] for x in range(self.width))
        return '\n'.join(map(row, range(self.height))) + '\n'
