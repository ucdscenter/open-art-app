import numpy as np

import os
import cv2
from PIL import *
from PIL import Image
from scipy import spatial
import vptree
import pickle
import requests
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import vgg19
from tensorflow.keras.models import load_model

def cosine_similarity(vec1, vec2):
		return spatial.distance.cosine(vec1, vec2)

def euclidean(vec1,vec2):
	return spatial.distance.euclidean(vec1[0],vec2[0])


enc_model = load_model('similar_art/data/draft_one.h5')
path_hashes = pickle.load(open('similar_art/data/path_hashes.txt', 'rb'))
b = pickle.load(open('similar_art/data/wikiarts_encoding_dict.txt', 'rb'))



outputs_dict = dict([(layer.name, layer.output) for layer in enc_model.layers])
feature_extractor = keras.Model(inputs=enc_model.inputs, outputs=enc_model.layers[11].output)


def preprocess_data(image_path):
	#image = Image.open(image_path)
	image = image_path
	if image.mode != 'RGB':
		image = image.convert(mode='RGB')
	image = np.asarray(image, dtype = 'float32')/255.0
	comp = tf.image.resize_with_pad(image,target_height = 64,target_width = 64,method=tf.image.ResizeMethod.BILINEAR,antialias=False)
	comp = np.expand_dims(comp, axis = 0)
	return comp

def extract_similar_images(image_path, tree, max_results=10):
	im = preprocess_data(image_path)
	style_encs = feature_extractor(im)
	results = tree.get_n_nearest_neighbors(style_encs, max_results)
	return results

def similar_image_paths(results, max_results=10):
	paths = []
	for i in range(0, len(results)):
		paths.append(path_hashes[str(results[i][1].tolist())])

	return paths

def plot_similar_images( results, orig=None, max_results=10):
	if orig != None:
		orig_image = cv2.imread(orig)
		orig_corrected = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB)
		plt.imshow(orig_corrected)
		plt.figure(1)
		return
	for i in range(0, len(results)):
		print(path_hashes[str(results[i][1].tolist())])
		img = download_image(path_hashes[str(results[i][1].tolist())])
		pil_image = Image.open(img)
		opencvImage = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
		#im = cv2.imread(path_hashes[str(results[i][1].tolist())])
		im_corrected = cv2.cvtColor(opencvImage, cv2.COLOR_BGR2RGB)
		plt.imshow(im_corrected)
		plt.figure(i+2)