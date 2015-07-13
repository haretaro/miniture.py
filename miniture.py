import sys
import HsvMod
import Focus
import math
from PIL import Image
import numpy as np

inputFile = sys.argv[1]
outputFile = 'output.jpg'
inputImage = Image.open(inputFile)
pixelsMatrix = HsvMod.toMatrix(inputImage)
pixelsMatrix = HsvMod.hsvMod(pixelsMatrix,(0,2,1))

pixelsMatrix = Focus.focusSimulation(pixelsMatrix,inputImage.size)

outdata = HsvMod.toData(pixelsMatrix)
outputImage = Image.new('RGB',inputImage.size)
outputImage.putdata(outdata)

outputImage.save(outputFile,'JPEG',quality=100,optimize=True)
