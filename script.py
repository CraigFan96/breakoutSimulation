import math,sys,shutil,getpass,os,commons, breakout_drawing, highscore, breakout

def get_game_state(self):
        return {
            "ball.x": self.ball.x,
            "ball.y": self.ball.y,
            "ball.xAcc": self.ball.xPos,
            "ball.yAcc": self.ball.yPos,
            "paddle.x": self.paddle.x,
            "paddle.y": self.paddle.y,
            "board": self.board,
            "score": self.score
        }