import breakout

def create_default_ball:
	return Ball()

def get_state():
	currState = {}
	currState[xPosition] = gameState.ball.x
	currState[yPosition] = gameState.ball.y
	currState[speed] = gameState.ball.speed
	#xAngle = 
	#yAngle = 
	#ballAcceleration = 
	currState[xPaddlePosition] = gameState.paddle.x
	currState[yPaddlePosition] = gameState.paddle.y
	currState[bricks] = gameState.board
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
	movedPaddle = gameState.paddle.x + x
	return movedPaddle

def set_paddle(x):
	gameState.paddle.x = x
	return gameState.paddle.x

def move_ball(x, y):
	gameState.ball.x = gameState.ball.x + x
	gameState.ball.y = gameState.ball.y + y
	return gameState.ball

def get_bricks():
	return gameState.board

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

	return gameState.board
