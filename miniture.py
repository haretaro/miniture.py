import sys
import HsiMod
import Focus
import math
from PIL import Image
import numpy as np

inputFile = sys.argv[1]
outputFile = 'output.jpg'
inputImage = Image.open(inputFile)
pixelsMatrix = HsiMod.toMatrix(inputImage)
pixelsMatrix = HsiMod.hsiMod(pixelsMatrix,(0,2,1))

pixelsMatrix = Focus.focusSimulation(pixelsMatrix,inputImage.size)

outdata = HsiMod.toData(pixelsMatrix)
outputImage = Image.new('RGB',inputImage.size)
outputImage.putdata(outdata)

outputImage.save(outputFile,'JPEG',quality=100,optimize=True)
