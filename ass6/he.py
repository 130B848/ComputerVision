import cv2
import math
import numpy as np

def histogram_equalization(input):
    count = [0 for i in xrange(256)]
    accuRatio = [0.0 for i in xrange(256)]

    rows = input.shape[0]
    cols = input.shape[1]
    total = float(rows * cols)
    
    for i in range(rows):
        for j in range(cols):
            count[input[i, j]] += 1
 
    accuRatio[0] = count[0] / total
    for i in range(1, 256):
        accuRatio[i] = count[i] / total + accuRatio[i - 1]

    for i in range(256):
        #print i, accuRatio[i]
        accuRatio[i] = int(math.ceil(255 * accuRatio[i]))

    output = np.copy(input)
    for i in range(rows):
        for j in range(cols):
            output[i, j] = accuRatio[input[i, j]]

    return output


src = cv2.imread("underexposed.png", cv2.IMREAD_GRAYSCALE)
output = histogram_equalization(src)
cv2.imwrite("histogram_equalization.png", output)
