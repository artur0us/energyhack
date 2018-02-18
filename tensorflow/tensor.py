import os
import tensorflow as tf
import time
import csv
import matplotlib.pyplot as plt
import math

mod = None

# Used to supress AVX warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

NUM_EXAMPLES = 0

trainx = []
trainy = []
	
x = None
y = None

h1 = None
hypothesis = None
cost = None

saver = None
sess = None

def initialize(MOD):
	global mod
	mod = MOD

	INPUT = 0
	HIDDEN = 4
	OUTPUT = 1

	global NUM_EXAMPLES
	with open('normalized_' + mod + '_dataset.csv', 'r') as csvfile:
	    input_data = csv.reader(csvfile, delimiter = ';')
	    for row in input_data:
	    	INPUT = len(row) - 1
	    	NUM_EXAMPLES += 1
	    	trainx_row = []
	    	for i in range(INPUT):
	    		trainx_row.append(float(row[i]))
	    	trainx.append(trainx_row)
	        trainy.append([float(row[INPUT])])
	        # print trainx
	        # print trainy

	print INPUT
	print NUM_EXAMPLES

	global x
	global y
	x = tf.placeholder(tf.float32, shape = [NUM_EXAMPLES, INPUT], name = 'inputs')
	y = tf.placeholder(tf.float32, shape = [NUM_EXAMPLES, OUTPUT], name = 'labels')

	# Define weights
	weights1 = tf.Variable(tf.random_normal([INPUT, HIDDEN]), name = "weights1")
	weights2 = tf.Variable(tf.random_normal([HIDDEN, OUTPUT]), name = "weights2")

	# Define the BIAS node
	bias1 = tf.Variable(tf.zeros([HIDDEN]), name = "bias1")
	bias2 = tf.Variable(tf.zeros([OUTPUT]), name = "bias2")

	global h1
	# Feed forward to the hidden layer
	h1 = tf.nn.relu(tf.matmul(x, weights1) + bias1)

	global hypothesis
	# Feedforward to the output layer - hypothesis is what the neural network thinks it should output for a given input.
	hypothesis = tf.nn.relu(tf.matmul(h1, weights2) + bias2)

	global cost
	# Setup the cost function and set the traning method
	# We are using the squared error (ACTUAL - DESIRED)
	cost = tf.reduce_sum(tf.square(hypothesis - y))

	# Initialise the variables and create a session
	init = tf.global_variables_initializer()

	global saver
	# 'Saver' op to save and restore all the variables
	saver = tf.train.Saver()

	global sess
	# Initialise the session
	sess = tf.Session()

	# Run the session
	sess.run(init)

def restore():
	print 'restoring...'
	saver.restore(sess, 'cache/' + mod + '/model.ckpt')
	print("Model restored from file")

def test():
	t_start = time.clock()
	hp, ct = sess.run([hypothesis, cost], feed_dict = {x: trainx, y: trainy})
	t_end = time.clock()

	result = []
	expects = []
	print("Hypothesis Target Error")
	for i in range(len(hp)):
		result.append(math.sqrt(hp[i][0]))
		expects.append(math.sqrt(trainy[i][0]))

	plt.plot(result, 'r-', linewidth = 0.3)
	plt.plot(expects, 'b-', linewidth = 0.3)
	plt.show()

	print('Cost: ', ct)
	print('Elapsed time: ', t_end - t_start)

def train(rate, epochs, outputInterval):
	# Choose a training approach - effectively backprop
	train_step = tf.train.GradientDescentOptimizer(rate).minimize(cost)

	t_start = time.clock()

	for i in range(epochs):
		sess.run(train_step, feed_dict = {x: trainx, y: trainy})
		
		if i % outputInterval == 0:
			print('\n')
			print('Epoch ', i)
			hp, ct = sess.run([hypothesis, cost], feed_dict = {x: trainx, y: trainy})
			t_end = time.clock()

			print('Cost: ', ct)
			print('Elapsed time: ', t_end - t_start)

	t_end = time.clock()

	print('\n')
	print('Elapsed time: ', t_end - t_start)
	print('Number of epochs: ', epochs)

	print('\n')
	print("Model saved in file " + saver.save(sess, 'cache/' + mod + '/model.ckpt'))