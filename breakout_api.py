import breakout

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


def move_paddle(x):
	movedPaddle = breakout.gameState.paddle.x + x
	return movedPaddle
	#x is an int

def set_paddle(x):
	#x is an int
	breakout.gameState.paddle.x = x
	return gameState.paddle.x

def move_ball(x, y):
	newXLocation = breakout.gameState.ball.x + x
	newYLocation = breakout.gameState.ball.y + y

def get_bricks():
	return breakout.gameState.board


def get_num_bricks():
    ans = 0
    for column in bricks:
        for brick in column:
            ans += 1
    return ans

def set_bricks():


def set_brick(b, on):
	#b is an int, on is a boolean(could be an int)
