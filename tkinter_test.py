# USAGE
# tkinter_test.py

# import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import random
import cv2

def select_image():
	# grab a reference to the image panels
	global panelA, panelB

	# open a file chooser dialog and allow the user to select an input
	# image
	path = filedialog.askopenfilename()
	print(path)

	# -*- coding: utf-8 -*-
	"""t81_558_class_09_3_transfer_cv.ipynb

	Automatically generated by Colaboratory.

	Original file is located at
	    https://colab.research.google.com/github/jeffheaton/t81_558_deep_learning/blob/master/t81_558_class_09_3_transfer_cv.ipynb
	"""

	import pandas as pd
	import numpy as np
	import os
	import tensorflow.keras
	import matplotlib.pyplot as plt
	from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
	from tensorflow.keras.applications import MobileNet
	from tensorflow.keras.preprocessing import image
	from tensorflow.keras.applications.mobilenet import preprocess_input
	from tensorflow.keras.preprocessing.image import ImageDataGenerator
	from tensorflow.keras.models import Model
	from tensorflow.keras.optimizers import Adam

	
	# from keras.layers import Dense
	# from keras.models import model_from_json
	# from tensorflow.keras.preprocessing.image import img_to_array
	from tensorflow.keras.models import load_model
	import numpy
	import os

	"""We are now ready to see how our new model can predict dog breeds.  The URLs in the code below provide several example dogs to look at.  Feel free to add your own."""

	##### Load the model
	# from tensorflow.keras.models import model_from_json
	# with open('model.json', 'r') as f:
	# 	json = f.read()
	# m1 = model_from_json(json)

	model = load_model('keras_model.h5')

	# Commented out IPython magic to ensure Python compatibility.
	# %matplotlib inline
	from PIL import Image, ImageFile
	from matplotlib.pyplot import imshow
	import requests
	import numpy as np
	from io import BytesIO
	from IPython.display import display, HTML
	from tensorflow.keras.applications.mobilenet import decode_predictions

	IMAGE_WIDTH = 224
	IMAGE_HEIGHT = 224
	IMAGE_CHANNELS = 3

	def make_square(img):
		cols, rows = img.size

		if rows > cols:
			pad = (rows - cols) / 2
			img = img.crop((pad, 0, cols, cols))
		else:
			pad = (cols - rows) / 2
			img = img.crop((0, pad, rows, rows))

		return img

	# for url in images:
	#     x = []
	#     ImageFile.LOAD_TRUNCATED_IMAGES = False
	#     response = requests.get(url)
	#     img = Image.open("20.jpg")
	# #1,5
	#     img.load()
	#     img = img.resize((IMAGE_WIDTH,IMAGE_HEIGHT),Image.ANTIALIAS)
	#
	#     x = image.img_to_array(img)
	#     x = np.expand_dims(x, axis=0)
	#     x = preprocess_input(x)
	#     pred = m1.predict(x)
	#
	#     display("___________________________________________________________________________________________")
	#     display(img)
	#     print(np.argmax(pred,axis=1))
	#
	# x = []
	img = Image.open(path)

	img.load()
	img = img.resize((IMAGE_WIDTH, IMAGE_HEIGHT), Image.ANTIALIAS)
	#
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	x = preprocess_input(x)
	pred = model.predict(x)
	#

	display(img)
	op = np.argmax(pred, axis=1)
	print(op)
	
	# ensure a file path was selected
	if len(path) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image = cv2.imread(path)
		image = cv2.resize(image, (250, 610))
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		edged = cv2.Canny(gray, 50, 100)
		edged = cv2.resize(image, (250, 610))




		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		# convert the images to PIL format...
		image = Image.fromarray(image)
		edged = Image.fromarray(edged)

		# ...and then to ImageTk format
		image = ImageTk.PhotoImage(image)
		edged = ImageTk.PhotoImage(edged)

		# if the panels are None, initialize them
		if panelA is None or panelB is None:
			# the first panel will store our original image
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left")

			# while the second panel will store the edge map
			panelB = Label(image=edged)
			panelB.image = edged
			panelB.pack(side="right")

		# otherwise, update the image panels
		else:
			# update the pannels
			panelA.configure(image=image)
			panelB.configure(image=edged)
			panelA.image = image
			panelB.image = edged

# initialize the window toolkit along with the two image panels
root = Tk()
panelA = None
panelB = None

# Using cv2.imshow() method
# Displaying the image
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")



# kick off the GUI
root.geometry("600x500+100+50")
root.mainloop()