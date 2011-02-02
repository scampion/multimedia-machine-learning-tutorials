#!/usr/bin/python
"""
This program is demonstration for face and object detection using haar-like features.
The program finds faces in a camera image or video stream and displays a red box around them.

Original C implementation by:  ?
Python implementation by: Roman Stanchak, James Bowman
"""
import sys
import os
import cv
from optparse import OptionParser
import Image 

min_size = (20, 20)
image_scale = 2
haar_scale = 1.2
min_neighbors = 2
haar_flags = 0

def detect_and_draw(img, cascade):
    gray = cv.CreateImage((img.width,img.height), 8, 1)
    small_img = cv.CreateImage((cv.Round(img.width / image_scale),
			       cv.Round (img.height / image_scale)), 8, 1)
    # convert color input image to grayscale
    cv.CvtColor(img, gray, cv.CV_BGR2GRAY)
    # scale input image for faster processing
    cv.Resize(gray, small_img, cv.CV_INTER_LINEAR)
    cv.EqualizeHist(small_img, small_img)
    if(cascade):
        t = cv.GetTickCount()
        faces = cv.HaarDetectObjects(small_img, cascade, cv.CreateMemStorage(0),
                                     haar_scale, min_neighbors, haar_flags, min_size)
        index = 0 
        if faces:
            for ((x, y, w, h), n) in faces:
                # the input to cv.HaarDetectObjects was resized, so scale the 
                # bounding box of each face and convert it to two CvPoints
                x1, y1 = (int(x * image_scale), int(y * image_scale))
                x2, y2 = (int((x + w) * image_scale), int((y + h) * image_scale))

                pi = Image.fromstring("L", cv.GetSize(gray), gray.tostring())
                pi = pi.crop((x1, y1, x2, y2))
                pi = pi.resize((64, 64), Image.ANTIALIAS)
                path = os.path.join(sys.argv[1])
                pi.save(path)
                index += 1 
        else:
            os.remove(sys.argv[1])

if __name__ == '__main__':
    cascade = cv.Load("haarcascade_frontalface_alt.xml")
    frame = cv.LoadImage(sys.argv[1])
    detect_and_draw(frame, cascade)
