import cv2
import numpy as np

drawing_averages = []
for imageNumber in range(1,51):

    img = cv2.imread('C:\\Users\\ghalya\\Pictures\\Hands\\Saunders_hand\\al_r_' + str(imageNumber) + '.png', 0)

    if img is None:
        print "Error loading image"
        exit()
    newImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    #cv2.imshow('Image', img)


    # define the list of boundaries
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

    drawing_averages.append([xAvg, yAvg])
    #print("xAvg: ", xAvg, " yAvg: ", yAvg)
    cv2.circle(newImg, (xAvg, yAvg), 5, (0, 0, 255), -1)
    #cv2.imshow("image", newImg)
    #cv2.imwrite("C:\Users\ghalya\Pictures\genLEL.png", newImg)
    cv2.waitKey(0)

print drawing_averages
count = xTotal = yTotal = 0
for i, j in drawing_averages:
    xTotal += i
    yTotal += j
    count += 1
print "average:", xTotal/count, yTotal/count,
