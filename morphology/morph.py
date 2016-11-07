import cv2

def dilation(inFile, outFile, seHeight, seWidth):
        img = cv2.imread(inFile, cv2.IMREAD_GRAYSCALE)

        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if img[i][j] == 0:
                    ii = i
                    while (ii < img.shape[0]) and (ii - i < seHeight):
                        jj = j
                        while (jj < img.shape[1]) and (jj - j < seWidth):
                            if img[ii][jj]:
                                img[i][j] = 255
                                ii = img.shape[0]
                                jj = img.shape[1]

                            jj += 1
                        ii += 1

        cv2.imwrite(outFile, img)

def erosion(inFile, outFile, seHeight, seWidth):
    img = cv2.imread(inFile, cv2.IMREAD_GRAYSCALE)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j]:
                ii = i
                while (ii < img.shape[0]) and (ii - i < seHeight):
                    jj = j
                    while (jj < img.shape[1]) and (jj - j < seWidth):
                        if img[ii][jj] == 0:
                            img[i][j] = 0
                            ii = img.shape[0]
                            jj = img.shape[1]

                        jj += 1
                    ii += 1

    cv2.imwrite(outFile, img)

seHeight = input("Please input the height of structing element (pixel): ")
seWidth = input("Please input the width of structing element (pixel): ")
dilation("lena-binary.bmp", "dilation.bmp", seHeight, seWidth)
erosion("lena-binary.bmp", "erosion.bmp", seHeight, seWidth)
