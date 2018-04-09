import unittest
import breakout_api as api

class TestBreakoutAPI(unittest.TestCase):

    def test_move_paddle(self):
        ball = Ball()
        api.set_state(''' not sure how we're setting state yet ''')
        self.assertEqual(api.get_state(), ball.x)
