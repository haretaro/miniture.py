import HsiMod
import math
from PIL import Image
import numpy as np

inputFile = 'yagi.jpg'
outputFile = 'output.jpg'
inputImage = Image.open(inputFile)

pixels = HsiMod.toMatrix(inputImage)
pixels = HsiMod.hsiMod(pixels,(0,2,1))
outdata = HsiMod.toData(pixels)

outputImage = Image.new('RGB',inputImage.size)
outputImage.putdata(outdata)
outputImage.save(outputFile,'JPEG',quality=100,optimize=True)
