from PIL import Image
import numpy as np

def focusSimulation(matrix,size):
  (width,height) = size
  temp = matrix.copy()
  default = height*2//5
  processLine = default
  print('defocusing:')
  while processLine > 2:
    print(processLine)
    for p in range(width*height):
      i = p%width
      j = p//width
      if j > processLine:
        break
      if i == 0 or i==width-1 or j == 0:
        continue

      #defocus upward, then downward
      for k in range(2):
        temp[p] = (2*matrix[p]
            + matrix[p+1]
            + matrix[p-1]
            + matrix[p+width]
            + matrix[p-width])/6
        p=(height-1-j)*width + i
	
    processLine = int(processLine/1.2)
    matrix = temp.copy()
  return matrix
