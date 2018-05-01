import breakout

def create_default_ball():
    return breakout.Ball()

def create_defaul_paddle():
    return breakout.Paddle()

def create_default_board():
    return breakout.new_board()

def create_default_state():
    return breakout.GameState.default_state()

def create_custom_state(state_dict):
    return breakout.GameState.state_from_dict(state_dict)

def play_game(state, actor):
    while not state.ball.alive:
        action = actor.act()
        state = next_state(ball, action)

def next_state(state, action):
    breakout.screen.fill(breakout.commons.black)
    breakout.pygame.draw.rect(breakout.screen,breakout.commons.grey,breakout.commons.wallLeft)
    breakout.pygame.draw.rect(breakout.screen,breakout.commons.grey,breakout.commons.wallRight)
    breakout.pygame.draw.rect(breakout.screen,breakout.commons.grey,breakout.commons.wallTop)
    breakout.pygame.draw.rect(breakout.screen,breakout.commons.red,(state.ball.x,state.ball.y,3,3))#Change ball size
    breakout.breakout_drawing.print_board(state.board,breakout.commons.row_colors)
    breakout.breakout_drawing.print_paddle(state.paddle)
    breakout.pygame.display.update()
    new_state = breakout.next_state(state, action)
    return new_state, new_state.score - state.score, not new_state.ball.alive

def game(state=None):
    if state is None:
        breakout.game()
    else:
        breakout.game(state)

"""
def get_state():
    currState = {}
    currState[xPosition] = breakout.gameState.ball.x
    currState[yPosition] = breakout.gameState.ball.y
    currState[speed] = breakout.gameState.ball.speed
    #xAngle = 
    #yAngle = 
    #ballAcceleration = 
    currState[xPaddlePosition] = breakout.gameState.paddle.x
    currState[yPaddlePosition] = breakout.gameState.paddle.y
    currState[bricks] = breakout.gameState.board
    return currState

def is_valid_state(state):
def set_state(state):
        gameState.board = state.board
        gameState.ball = state.ball
        gameState.score = state.score
        gameState.paddle = state.paddle
"""

def move_paddle(gameState, x):
    movedPaddle = gameState.paddle.x + x
    return movedPaddle

def set_paddle(gameState, x):
    #x is an int
    gameState.paddle.x = x
    return gameState

def move_ball(gameState, x, y):
    gameState.ball.x += x
    gameState.ball.y += y
    return gameState

def get_bricks(gameState):
    return gameState.board

def get_num_bricks(gameState):
    currBoard = gameState.board
    total = 0
    for colOfBlocks in currBoard:
        for block in colOfBlocks:
            total += block
    return total

def set_bricks(gameState, newBlocks):
    #6 rows, 18 columns
    gameState.board = newBlocks
    return gameState.board

def set_brick(gameState, rowVal, colVal, on):
    #b is an int, on is a boolean(could be an int)
    if on == 0:
        gameState.board[rowVal][colVal] = 0
    else:
        gameState.board[rowVal][colVal] = 1
