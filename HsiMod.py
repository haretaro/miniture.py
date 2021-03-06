import numpy as np
import math
from PIL import Image

hsiTransform = np.array([
	[1/math.sqrt(2),-1/math.sqrt(2),0],
	[1/(math.sqrt(2)*math.sqrt(3)),1/(math.sqrt(2)*math.sqrt(3)),-2/(math.sqrt(2)*math.sqrt(3))],
	[1/math.sqrt(3),1/math.sqrt(3),1/math.sqrt(3)]])

def getHsiModulationTransform(mod):
	(h,s,v) = mod
	hsiModulation = np.array([
		[s*math.cos(h), -s*math.sin(h),0],
		[s*math.sin(h), s*math.cos(h),0],
		[0,0,v]])
	return np.linalg.inv(hsiTransform).dot(hsiModulation).dot(hsiTransform)

def hsiMod(pixels,mod,annotation=True):
	(h,s,v) = mod
	transform = getHsiModulationTransform(mod)
	if annotation:	
		print('transform matrix:')
		print(transform)
	if annotation:
		print('input[0-4]')
		print(pixels[:4])
	pixels=[transform.dot(pixel) for pixel in pixels]
	if annotation:
		print('output[0-4]')
		print(pixels[:4])
	return pixels

def toMatrix(image):
	data = image.getdata()
	pixelsMatrix = np.array(data)
	return pixelsMatrix

def toData(matrix):
	outdata = [tuple(int(p) for p in pixel.T.tolist()) for pixel in matrix]
	return outdata
