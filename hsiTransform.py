import sys
import HsiMod
import math
from PIL import Image
import numpy as np

inputFile = sys.argv[1]
outputFile = 'output.jpg'
inputImage = Image.open(inputFile)

if len(sys.argv) > 4:
    mod = tuple(float(sys.argv[x]) for x in [2,3,4])
else:
    mod = (0,2,1)

pixels = HsiMod.toMatrix(inputImage)
pixels = HsiMod.hsiMod(pixels,mod)
outdata = HsiMod.toData(pixels)

outputImage = Image.new('RGB',inputImage.size)
outputImage.putdata(outdata)
outputImage.save(outputFile,'JPEG',quality=100,optimize=True)
