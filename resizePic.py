#!/bin/python3

__author__ = "simon"

from PIL import Image
import os,sys



def resize(path=".", format="png",height=1024,weight=768):
	'''
	Use PIL to resize the image
	'''
	for root,dir,files in os.walk(path):
		for item in files:
			if item.endswith(format):
				img = Image.open( path + os.sep+item)
				img_small = img.resize((height,weight))
				img_small.save( path+"/../small/" + item.split('.')[0] + '.jpg')



if __name__ == "__main__":
	resize(sys.argv[1])
