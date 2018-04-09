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

def is_valid_state(state):


def set_state(state):


def move_paddle(x):
	movedPaddle = gameState.paddle.x + x
	return movedPaddle
	#x is an int

def set_paddle(x):
	#x is an int
	gameState.paddle.x = x
	return gameState.paddle.x

def move_ball(x, y):
	newXLocation = gameState.ball.x + x
	newYLocation = gameState.ball.y + y

def get_bricks():
	return gameState.board


def get_num_bricks():


def set_bricks():


def set_brick(b, on):
	#b is an int, on is a boolean(could be an int)