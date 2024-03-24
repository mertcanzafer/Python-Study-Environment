import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

# Capture your vide using VideoCaptrure object
# This zero number is the initial camera from your computer
cap = cv2.VideoCapture(0)

if not cap.isOpened():

    raise ValueError("The camera wasn't found!!!!")

# VideoCapture.set(propld,value)
# propId : Property identifier from cv::VideoCaptureProperties (eg. cv::CAP_PROP_POS_MSEC, cv::CAP_PROP_POS_FRAMES, ...) or one from Additional flags for video I/O  API  backends
# value: Value of the property.

cap.set(3, 1280)
cap.set(4, 720)

# Set mehtod is a boolean method that returns true if the property is supported by backend used by the VideoCapture instance.
# detectionCon -> Minimum detection confidence

_detector_hand = HandDetector(detectionCon=0.7)

Initial_distance = None
img_scale = 0

# Center points
center_x, center_y = 300, 500


while True:

    Is_read, img = cap.read()
    # Cap.read() function : captures frames from a video file or a camera connected to the computer.
    # Returns a tuple of two variables, first one is an boolean value to check wheter it is readed or not.
    # Second one is an Numpy Array which is a frame.
    hands, img = _detector_hand.findHands(img)
    # Read our current image
    image1 = cv2.imread(
        'FoodPic.jpg')

    if (len(hands) == 2):

        # Both hands must be on the screen.
        # plan ur gesture which you want to use i use the thumb and index finger
        # hand[0] == right hand & hand[1] == left hand.
        print(_detector_hand.fingersUp(
            hands[1]), _detector_hand.fingersUp(hands[1]))
        if (_detector_hand.fingersUp(hands[1]) == [1, 1, 0, 0, 0] and _detector_hand.fingersUp(hands[0]) == [1, 1, 0, 0, 0]):
            # print("correct action of hand")
            # now lets find the distance from the hand
            lmlist0 = hands[0]['lmlist']
            lmlist1 = hands[1]['lmlist']

            # get the length using tip of finger

            if (Initial_distance == None):

                length, info, img = _detector_hand.findDistance(
                    lmlist0[8], lmlist1[8], img)
                # print(length)
                Initial_distance = length
            length, info, img = _detector_hand.findDistance(
                lmlist0[8], lmlist1[8], img)
            # decrese the sensitivity by making a int
            img_scale = int((length - Initial_distance) // 2)
            # print(image_scale)
            # find the center point of the distance
            # which is loacted in info -> findDistance

            center_x, center_y = info[4:]

    else:
        # we make the distance to 0 when hands are taken away from screen
        Initial_distance = None

    try:
        # store the image in a variable
        image1 = cv2.imread(
            'FoodPic.jpg')
        # get the height and width of the given image 250*250
        h1, w1 = image1.shape

        new_height, new_width = ((h1 + img_scale) // 2) * \
            2, ((w1 + img_scale) // 2) * 2

        image1 = cv2.resize(image1, (new_width, new_height))

        # slizing the image and overlaying it shit a image by 10 should increase both the same value
        # keep the image in the center of the width
        # cx == height

        img[center_y - new_height // 2: center_y +
            new_height // 2, center_x - new_width // 2: center_x + new_width // 2] = image1
        cv2.imshow("image", img)

        key = cv2.waitKey(1)
        if (key == ord('c')):
            break
    except:
        pass
