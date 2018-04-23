import breakout_api as bk

custom_state = {'frame': 141, 'ball.y': 249.57173370360204, 'ball.x': 556.7646532495212, 'ball.yAcc': 2.57498037404092, 'score': 1, 'ball.alive': True, 'ball.xAcc': -4.28596267754446, 'paddle.x': 392, 'paddle.y': 450, 'ball.angle': 120.99719262137975, 'ball.remaining': 1, 'ball.speed': 5, 'board': [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1,   1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0]]}

state = bk.create_custom_state(custom_state)
# state = bk.create_default_state()
bk.game(state)
