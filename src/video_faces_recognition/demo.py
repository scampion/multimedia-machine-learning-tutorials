#!/usr/bin/python
import sys
import os
import cv
from optparse import OptionParser
import Image 
import facerecognizer
import numpy as np 
import pca 

min_size = (20, 20)
image_scale = 2
haar_scale = 1.2
min_neighbors = 2
haar_flags = 0
cascade = cv.Load("haarcascade_frontalface_alt.xml")
font = cv.InitFont(cv.CV_FONT_HERSHEY_COMPLEX,0.5,1)

def detect_and_draw(img, cascade, input_name, index):
    gray = cv.CreateImage((img.width,img.height), 8, 1)
    small_img = cv.CreateImage((cv.Round(img.width / image_scale),
			       cv.Round (img.height / image_scale)), 8, 1)
    cv.CvtColor(img, gray, cv.CV_BGR2GRAY)
    cv.Resize(gray, small_img, cv.CV_INTER_LINEAR)
    cv.EqualizeHist(small_img, small_img)

    faces = cv.HaarDetectObjects(small_img, cascade, cv.CreateMemStorage(0),
                                 haar_scale, min_neighbors, 
                                 haar_flags, min_size)

    if faces:
        for ((x, y, w, h), n) in faces:
            x1, y1 = pt1 = (int(x * image_scale), int(y * image_scale))
            x2, y2 = pt2 = (int((x + w) * image_scale),
                            int((y + h) * image_scale))

            #Extract image face 
            pi = Image.fromstring("L", cv.GetSize(gray), gray.tostring())
            pi = pi.crop((x1, y1, x2, y2))
            pi = pi.resize((64, 64), Image.ANTIALIAS)
            f = np.array(pi.getdata())                
            
            #Get face signature 
            X_test_pca = facerecognizer.pca_sl.transform([f])

            #X_test_pca = facerecognizer.pca.transform(f, mean, compo)
            X_test_pca = facerecognizer.pca_sl.transform(f)
            #Call svm classifier 
            y_pred = facerecognizer.clf.predict(X_test_pca)
            name = facerecognizer.category_names[y_pred[0]]
            
            #Draw bbox and name
            cv.Rectangle(img, pt1, pt2, cv.RGB(255, 0, 0), 1, 8, 0)
            cv.PutText(img, name , (x1,y2), font,cv.RGB(255,0,0))

            index += 1 

    cv.ShowImage("result", img)
    return index

if __name__ == '__main__':
    input_name = sys.argv[1]
    capture = cv.CreateFileCapture(input_name)
    cv.NamedWindow("result", 1)

    frame_copy = None
    index = 0 
    while index < 1000 :
        frame = cv.QueryFrame(capture)
        if not frame:
            cv.WaitKey(0)
            break
        if not frame_copy:
            frame_copy = cv.CreateImage((frame.width,frame.height),
                                            cv.IPL_DEPTH_8U, frame.nChannels)
        if frame.origin == cv.IPL_ORIGIN_TL:
            cv.Copy(frame, frame_copy)
        else:
            cv.Flip(frame, frame_copy, 0)
            
        index = detect_and_draw(frame_copy, cascade, input_name, index)

        if cv.WaitKey(10) >= 0:
            break

    cv.DestroyWindow("result")
