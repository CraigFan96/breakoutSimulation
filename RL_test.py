import argparse
import gym
import os
import breakout_api as bk
import numpy as np
import time
import tensorflow as tf
import tensorflow.contrib.layers as layers
import baselines.common.tf_util as U

from baselines.common.atari_wrappers_deprecated import wrap_dqn

from skimage import io


def build_act(make_obs_ph, q_func, num_actions, scope="deepq", reuse=None):
	"""Creates the act function:
	Parameters
	----------
	make_obs_ph: str -> tf.placeholder or TfInput
		a function that take a name and creates a placeholder of input with that name
	q_func: (tf.Variable, int, str, bool) -> tf.Variable
		the model that takes the following inputs:
			observation_in: object
				the output of observation placeholder
			num_actions: int
				number of actions
			scope: str
			reuse: bool
				should be passed to outer variable scope
		and returns a tensor of shape (batch_size, num_actions) with values of every action.
	num_actions: int
		number of actions.
	scope: str or VariableScope
		optional scope for variable_scope.
	reuse: bool or None
		whether or not the variables should be reused. To be able to reuse the scope must be given.
	Returns
	-------
	act: (tf.Variable, bool, float) -> tf.Variable
		function to select and action given observation.
`       See the top of the file for details.
	"""
	with tf.variable_scope(scope, reuse=reuse):
		observations_ph = U.ensure_tf_input(make_obs_ph("observation"))
		stochastic_ph = tf.placeholder(tf.bool, (), name="stochastic")
		update_eps_ph = tf.placeholder(tf.float32, (), name="update_eps")

		eps = tf.get_variable("eps", (), initializer=tf.constant_initializer(0))

		q_values = q_func(observations_ph.get(), num_actions, scope="q_func")
		deterministic_actions = tf.argmax(q_values, axis=1)

		batch_size = tf.shape(observations_ph.get())[0]
		random_actions = tf.random_uniform(tf.stack([batch_size]), minval=0, maxval=num_actions, dtype=tf.int64)
		chose_random = tf.random_uniform(tf.stack([batch_size]), minval=0, maxval=1, dtype=tf.float32) < eps
		stochastic_actions = tf.where(chose_random, random_actions, deterministic_actions)

		output_actions = tf.cond(stochastic_ph, lambda: stochastic_actions, lambda: deterministic_actions)
		update_eps_expr = eps.assign(tf.cond(update_eps_ph >= 0, lambda: update_eps_ph, lambda: eps))
		act = U.function(inputs=[observations_ph, stochastic_ph, update_eps_ph],
						 outputs=[output_actions, q_values],
						 givens={update_eps_ph: -1.0, stochastic_ph: True},
						 updates=[update_eps_expr])
		print("setting up act function...")
		return act

def dueling_model(img_in, num_actions, scope, reuse=False, layer_norm=False):
	"""As described in https://arxiv.org/abs/1511.06581"""
	with tf.variable_scope(scope, reuse=reuse):
		out = img_in
		with tf.variable_scope("convnet"):
			# original architecture
			out = layers.convolution2d(out, num_outputs=32, kernel_size=8, stride=4, activation_fn=tf.nn.relu)
			out = layers.convolution2d(out, num_outputs=64, kernel_size=4, stride=2, activation_fn=tf.nn.relu)
			out = layers.convolution2d(out, num_outputs=64, kernel_size=3, stride=1, activation_fn=tf.nn.relu)
		conv_out = layers.flatten(out)

		with tf.variable_scope("state_value"):
			state_hidden = layers.fully_connected(conv_out, num_outputs=512, activation_fn=None)
			if layer_norm:
				state_hidden = layer_norm_fn(state_hidden, relu=True)
			else:
				state_hidden = tf.nn.relu(state_hidden)
			state_score = layers.fully_connected(state_hidden, num_outputs=1, activation_fn=None)
		with tf.variable_scope("action_value"):
			actions_hidden = layers.fully_connected(conv_out, num_outputs=512, activation_fn=None)
			if layer_norm:
				actions_hidden = layer_norm_fn(actions_hidden, relu=True)
			else:
				actions_hidden = tf.nn.relu(actions_hidden)
			action_scores = layers.fully_connected(actions_hidden, num_outputs=num_actions, activation_fn=None)
			action_scores_mean = tf.reduce_mean(action_scores, 1)
			action_scores = action_scores - tf.expand_dims(action_scores_mean, 1)
		return state_score + action_scores

def make_env(game_name):
	env = gym.make(game_name + "NoFrameskip-v4")
	#env = bench.Monitor(env, None)
	env = wrap_dqn(env)
	return env

def play(game_name, env, act):
	obs = env.reset()
	j=0
	while True:
		j += 1
		img = env.render(mode='rgb_array')
		action, q_values = act(np.array(obs)[None])
		if game_name == "Breakout":
			if action > 3:
				action -= 2
		obs, rew, done, info = env.step(action)
		print(action, rew)
		
		if done:
			obs = env.reset()
			print("Episode finished after {} timesteps".format(j+1))
			break

def main():
	with U.make_session(4) as sess:
		env = make_env(args.env_name)
		n_actions = env.action_space.n
		print(env.observation_space.shape)
		if args.env_name == "Breakout":
			n_actions = 6
		act = build_act(
					make_obs_ph=lambda name: U.Uint8Input(env.observation_space.shape, name=name),
					q_func=dueling_model,
					num_actions=n_actions)
		saver = tf.train.Saver()
		saver.restore(sess, args.model_path)
		
		play(args.env_name, env, act)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Intervene on and save images')
	parser.add_argument('env_name', metavar='env_name', help='')
	parser.add_argument('model_path', metavar='model_path', help='')
	args = parser.parse_args()
	main()
