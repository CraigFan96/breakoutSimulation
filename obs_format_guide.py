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
import os
import numpy as np
import time
import tensorflow as tf
import tensorflow.contrib.layers as layers
import baselines.common.tf_util as U
import cv2

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

def play(img, act):
    frame = 3
    state = bk.create_default_state()
    game = 0
    directory = "gameImages/"+str(game).zfill(4)
    filepaths = [directory + "/" + str(i).zfill(5) +".png" for i in range(int(frame-3), int(frame+1))]
    obs = process_observation(cv2.imread(filepaths[0]))
    j = 0
    while True:
        j += 1
        action, q_values = act(np.array(img)[None])
        print(action)
        if action >= 3:
            action -= 2
        if action == 1:
            obs, rew, done = bk.next_state(state, "left")
        elif action == 2:
            obs, rew, done = bk.next_state(state, "right")
        else:
            obs, rew, done = bk.next_state(state, "none")
        print(action, rew)
        if done:
            print("DONEDONE")
            break

def main():
    state = bk.create_default_state()
    game = state.game_num
    frame = 3

    #TODO Change for your own file structure
    directory = "gameImages/"+str(game).zfill(4)
    filepaths = [directory + "/" + str(i).zfill(5) +".png" for i in range(int(frame-3), int(frame+1))]

    observations = []
    for i in filepaths:
        observations.append(process_observation(cv2.imread(i)))
    observations = np.reshape(np.asarray(observations), (84, 84, 4))
    print(observations, observations.shape)
    #TODO Load act function. See XAI_IS_test.py for guidance. 
    with U.make_session(4) as sess:
        n_actions = 6
        act = build_act(
                make_obs_ph=lambda name: U.Uint8Input(observations.shape, name=name),
                q_func=dueling_model,
                num_actions=n_actions)
        saver = tf.train.Saver()
        saver.restore(sess, "model-atari-prior-duel-breakout-1/saved")

        play(observations, act)

if __name__ == "__main__":
    main()
