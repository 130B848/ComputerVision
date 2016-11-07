import cv2
import numpy
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# mB / mF : miu ==> group means
# between : sigma ==> group variances
# threshold : threshold ==> threshold value

def otsu(input, fore, back, histImage):
    sum = 0     # total number of
    sumB = 0    # sum of class background
    wB = 0      # probablity of background class separated by threshold
    wF = 0      # probablity of foreground class separated by threshold
    max = 0     # max value to find the variances of two classes
    threshold = 0   # init set threshold to 0, also the return value

    histogram = [0 for i in xrange(256)]
    accuRatio = [0 for i in xrange(256)]

    src = cv2.imread(input, cv2.IMREAD_GRAYSCALE)

    for i in xrange(src.shape[0]):
        for j in xrange(src.shape[1]):
            histogram[src[i][j]] += 1

    binSize = numpy.arange(1, 255, 3)
    plt.xlim([0, 260])
    plt.hist(histogram, bins = binSize, alpha = 0.5)
    plt.title("Histogram (black bg has been removed)")
    plt.xlabel("Grey Level (0 - 255)")
    plt.ylabel("Frequency")
    plt.savefig(histImage)

    for i in xrange(256):
        sum += i * histogram[i]

    pixelNum = src.shape[0] * src.shape[1]  # num of pixels in the input image

    for i in xrange(256):
        wB += histogram[i]
        if wB == 0:
            continue
        wF = pixelNum - wB
        if wF == 0:
            break
        sumB +=  i * histogram[i]
        mB = float(sumB) / wB   # class background
        mF = float(sum - sumB) / wF # class foreground
        between = wB * wF * (mB - mF)**2    # variances of these two classes
        if between > max:
            max = between
            threshold = i

    # Deep copy of src
    dstF = numpy.array(src)
    dstB = numpy.array(src)
    for i in range(src.shape[0]):
        for j in range(src.shape[1]):
            if src[i][j] >= threshold:
                dstF[i][j] = 255
            else:
                dstB[i][j] = 0

    cv2.imwrite(fore, dstF)
    cv2.imwrite(back, dstB)

    return threshold

print otsu("cherry.png", "fore_cherry.png", "back_cherry.png", "histogram.png")
