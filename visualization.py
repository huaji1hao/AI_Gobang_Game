import pygame
import sys

# 游戏可视化
# Game visualization
class Visualize:
    def __init__(self):
        pygame.init()

        # 定义棋盘大小
        # Define board size
        self.Height = 15 
        self.Width = 15
        
        # 定义颜色
        # Define colors
        self.BLACK = (41, 36, 33)
        self.WHITE = (255, 245, 238)
        self.BROWN = (174, 112, 0)
        self.YELLOW =(210, 180, 140)

        # 定义棋盘和棋子的大小和位置
        # Define board and piece position and size
        self.WINDOW_SIZE = (700, 700)
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.pieces_surface = pygame.Surface(self.WINDOW_SIZE, pygame.SRCALPHA)
        self.highlight_surface = pygame.Surface(self.WINDOW_SIZE, pygame.SRCALPHA)

        # 设置窗口标题
        # Set window title
        pygame.display.set_caption("gobang")

        # 填充背景颜色
        # Fill background color
        self.screen.fill(self.YELLOW)

        # 定义字体
        # Define font
        self.font = pygame.font.Font(None, 40)

        # 定义棋盘和棋子的大小和位置
        # Define board and piece position and size
        self.BOARD_POSITION = (50, 50)
        self.CELL_SIZE = 40
        self.BOARD_SIZE = (self.CELL_SIZE*self.Height, self.CELL_SIZE*self.Width)
        
    # 绘制棋盘
    # Draw the board
    def draw_board(self):
        for i in range(self.Height+1):
            pygame.draw.line(self.screen, self.BLACK, 
                (self.BOARD_POSITION[0], self.BOARD_POSITION[1] + i*self.CELL_SIZE), 
                (self.BOARD_POSITION[0]+self.BOARD_SIZE[0], self.BOARD_POSITION[1] + i*self.CELL_SIZE))
        for i in range(self.Width+1):
            pygame.draw.line(self.screen, self.BLACK, 
                (self.BOARD_POSITION[0] + i*self.CELL_SIZE, self.BOARD_POSITION[1]), 
                (self.BOARD_POSITION[0] + i*self.CELL_SIZE, self.BOARD_POSITION[1]+self.BOARD_SIZE[1]))
        pygame.display.update()

    # 绘制棋子
    # Draw a piece
    def draw_piece(self, pos, color):
        # 在棋盘上绘制棋子，高亮最新的棋子
        # Draw a piece on the board, highlight the latest piece
        self.highlight_surface.fill(pygame.Color(0, 0, 0, 0))
        pygame.draw.circle(self.pieces_surface, color, 
            (self.BOARD_POSITION[0] + pos[0] * self.CELL_SIZE, self.BOARD_POSITION[1] + pos[1] * self.CELL_SIZE), 15)
        pygame.draw.circle(self.highlight_surface, self.WHITE, 
            (self.BOARD_POSITION[0] + pos[0] * self.CELL_SIZE, self.BOARD_POSITION[1] + pos[1] * self.CELL_SIZE), 15, width=3)
        self.screen.blits([(self.pieces_surface, (0, 0)), (self.highlight_surface, (0, 0))])
        pygame.display.update()
        
    # 绘制结束界面
    # Draw the end screen
    def draw_end_screen(self, winner):
        if winner == 1:
            text = self.font.render("Black wins!", True, self.BLACK)
        elif winner == 2:
            text = self.font.render("White wins!", True, self.BLACK)
        else:
            text = self.font.render("Draw!", True, self.BLACK)

        # 文本背景
        # Text background
        pygame.draw.rect(self.screen, self.WHITE, 
            (self.WINDOW_SIZE[0]/2 - text.get_width()/2 - 10, self.WINDOW_SIZE[1]/3 - text.get_height()/2 - 10, 
            text.get_width() + 20, text.get_height() + 20))
        pygame.draw.rect(self.screen, self.BLACK, 
            (self.WINDOW_SIZE[0]/2 - text.get_width()/2 - 10, self.WINDOW_SIZE[1]/3 - text.get_height()/2 - 10, 
            text.get_width() + 20, text.get_height() + 20), width=3)
        
        # 打印文本
        # Print text
        self.screen.blit(text, 
            (self.WINDOW_SIZE[0]/2 - text.get_width()/2, self.WINDOW_SIZE[1]/3 - text.get_height()/2))
        pygame.display.update()

        # 绘制重启和退出按钮
        # Draw restart and quit buttons
        pygame.draw.rect(self.screen, self.WHITE, 
            (self.WINDOW_SIZE[0]/2 - 115, self.WINDOW_SIZE[1]/3 + 50, 110, 50))
        pygame.draw.rect(self.screen, self.BLACK, 
            (self.WINDOW_SIZE[0]/2 - 115, self.WINDOW_SIZE[1]/3 + 50, 110, 50), width=3)
        pygame.draw.rect(self.screen, self.WHITE, 
            (self.WINDOW_SIZE[0]/2 + 5, self.WINDOW_SIZE[1]/3 + 50, 95, 50))
        pygame.draw.rect(self.screen, self.BLACK, 
            (self.WINDOW_SIZE[0]/2 + 5, self.WINDOW_SIZE[1]/3 + 50, 95, 50), width=3)     
        
        text = self.font.render("Restart", True, self.BLACK)
        self.screen.blit(text, 
            (self.WINDOW_SIZE[0]/2 - 110 + 50 - text.get_width()/2, self.WINDOW_SIZE[1]/3 + 50 + 25 - text.get_height()/2))
        text = self.font.render("Quit", True, self.BLACK)
        self.screen.blit(text, 
            (self.WINDOW_SIZE[0]/2 + 55 - text.get_width()/2, self.WINDOW_SIZE[1]/3 + 50 + 25 - text.get_height()/2))
        pygame.display.update()

        # 等待用户输入
        # Wait for user input
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if mouse_x > self.WINDOW_SIZE[0]/2 - 100 and mouse_x < self.WINDOW_SIZE[0]/2 and \
                        mouse_y > self.WINDOW_SIZE[1]/3 + 50 and mouse_y < self.WINDOW_SIZE[1]/3 + 50 + 50:
                        return 0 # 重启 Restart
                    elif mouse_x > self.WINDOW_SIZE[0]/2 and mouse_x < self.WINDOW_SIZE[0]/2 + 100 and \
                        mouse_y > self.WINDOW_SIZE[1]/3 + 50 and mouse_y < self.WINDOW_SIZE[1]/3 + 50 + 50:
                        return 1 # 退出 Quit

    # 获取鼠标点击位置
    # Get mouse click position
    def get_input(self):
        # 等待用户输入
        # Wait for user input
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()   
                
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # 四舍五入到最近的单元格
                    # Round to the nearest cell
                    x = round((mouse_x - self.BOARD_POSITION[0])/self.CELL_SIZE)
                    y = round((mouse_y - self.BOARD_POSITION[1])/self.CELL_SIZE)
                    # 检查点击是否在棋盘上，否则忽略
                    # Check if the click is on the board, if not ignore
                    if x < self.BOARD_SIZE[0] and y < self.BOARD_SIZE[1]:
                        return x, y
