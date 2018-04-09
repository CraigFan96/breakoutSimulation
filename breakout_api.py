import breakout

def create_default_ball:
	return Ball()

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
"""
def is_valid_state(state):


def set_state(state):
	gameState.board = state.board
	gameState.ball = state.ball
	gameState.score = state.score
	gameState.paddle = state.paddle
"""

def move_paddle(x):
	movedPaddle = breakout.gameState.paddle.x + x
	return movedPaddle

def set_paddle(x):
	#x is an int
	breakout.gameState.paddle.x = x
	return gameState.paddle.x

def move_ball(x, y):
	gameState.ball.x = breakout.gameState.ball.x + x
	gameState.ball.y = breakout.gameState.ball.y + y
	return gameState

def get_bricks():
	return breakout.gameState.board

def get_num_bricks():
    currBoard = gameState.board
    total = 0
    for rowOfBlocks in currBoard:
            for block in rowOfBlocks:
            total += block
    return total

def set_bricks(newBlocks):
	#6 rows, 18 columns
	gameState.board = newBlocks
	return gameState.board

def set_brick(rowVal, colVal, on):
	#b is an int, on is a boolean(could be an int)
	if on == 0:
		gameState.board[rowVal][colVal] = 0
	else:
		gameState.board[rowVal][colVal] = 1
