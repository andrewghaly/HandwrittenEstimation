import cv2
import numpy as np

def imageToAnalyze(image_path):

    drawingAverage = []
    img = cv2.imread(image_path, 0)

    if img is None:
        print "Error loading image"
        exit()
    newImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    #cv2.imshow('Image', img)


    # define the list of boundaries
    #color range hit or not
    boundaries = [
        ([151], [255]),
    ]


    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        #apply the mask
        mask = cv2.inRange(img, lower, upper)
        output = cv2.bitwise_and(img, img, mask=mask)

        # show the images
        #cv2.imshow("images", np.hstack([img, output]))
        #cv2.imwrite('C:\Users\ghalya\Pictures\lol_testlulz.png', np.hstack([img, output]))

    height, width = img.shape
    points = 0
    xSum = 0
    ySum = 0
    for i in range(0, width):
        for j in range(0, height):
            if img[j][i] <= 150:
                points += 1
                xSum += i
                ySum += j

    xAvg = xSum/points
    yAvg = ySum/points

    #print("xAvg: ", xAvg, " yAvg: ", yAvg)
    cv2.circle(newImg, (xAvg, yAvg), 5, (0, 0, 255), -1)
    #cv2.imshow("image", newImg)
    #cv2.imwrite("C:\Users\ghalya\Pictures\genLEL.png", newImg)
    cv2.waitKey(0)
    drawingAverage.append([xAvg, yAvg])
    return drawingAverage