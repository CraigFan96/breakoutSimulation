import breakout

def create_default_ball:
	return Ball()

def get_state(state):
	currState = {}
	currState[xPosition] = state.ball.x
	currState[yPosition] = state.ball.y
	currState[speed] = state.ball.speed
	#xAngle = 
	#yAngle = 
	#ballAcceleration = 
	currState[xPaddlePosition] = state.paddle.x
	currState[yPaddlePosition] = state.paddle.y
	currState[bricks] = state.board
	return currState
"""
def is_valid_state(state):


def set_state(state):
	gameState.board = state.board
	gameState.ball = state.ball
	gameState.score = state.score
	gameState.paddle = state.paddle
"""

def move_paddle(state, x):
	state.paddle.x = state.paddle.x + x
	return gameState.paddle.x

def set_paddle(state, x):
	state.paddle.x = x
	return gameState.paddle.x

def move_ball(state, x, y):
	state.ball.x = state.ball.x + x
	state.ball.y = state.ball.y + y
	return gameState.ball

def get_bricks(state):
	return state.board

def get_num_bricks(state):
	currBoard = state.board
	total = 0
	for rowOfBlocks in currBoard:
		for block in rowOfBlocks:
		total += block
	return total

def set_bricks(state, newBlocks):
	#6 rows, 18 columns
	state.board = newBlocks
	return state.board

def set_brick(state, rowVal, colVal, on):
	#b is an int, on is a boolean(could be an int)
	if on == 0:
		state.board[rowVal][colVal] = 0
	else:
		state.board[rowVal][colVal] = 1

	return state.board
