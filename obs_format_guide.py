'''
The act function is expecting a numpy array with shape (None, 84, 84, 4) as input.

The following code snippet shows how I accomplished this using the Breakout .png images.
This is intended as a guide only, and should not be expected to compile without additional tweak.

Change the following code so that "filepaths" is a list of length 4 with the filepath of 4 successive .png files.

Also, I've omitted setting up the act function, but you can find this in the XAI_IS_test.py file.
'''

import numpy as np
import pandas as pd
import breakout_api as bk
from RL_test import *
from scipy.misc import imread
from PIL import Image


def process_observation(observation):
    assert observation.ndim == 3  # (height, width, channel)
    INPUT_SHAPE = (84, 84)
    top_clip = 34
    bottom_clip = 210-top_clip-160


    img = Image.fromarray(observation[top_clip:-bottom_clip,:,:])
    img = img.resize(INPUT_SHAPE).convert('L')  # resize and convert to grayscale
    processed_observation = np.array(img)
    assert processed_observation.shape == INPUT_SHAPE
    return processed_observation.astype('uint8')

def main():
        state = bk.create_default_state()
	game = state.game_num
	frame = state.frame

	#TODO Change for your own file structure
	directory = "gameImages/"+str(game).zfill(4)
	filepaths = [directory + "/" + str(i).zfill(5) +".png" for i in range(int(frame-3), int(frame+1))]

	#TODO Load act function. See XAI_IS_test.py for guidance.
        
        act = build_act(
                make_obs_ph=lambda name: U.Uint8Input(env.observation_space.shape, name=name),
                q_func=dueling_model,
                num_actions=n_actions)
	obs = np.rollaxis(np.asarray([process_observation(imread(f)) for f in filepaths]),0,3)
	action, q_values = act(obs[None])
	

if __name__ == "__main__":
	main()
