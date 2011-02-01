#/bin/python 
import cv, sys 
        
file = sys.argv[1]
image = cv.LoadImage(file)  
image_gray = cv.CreateImage(cv.GetSize(image), image.depth, 1)
k, v = cv.ExtractSURF(image_gray, None, cv.CreateMemStorage(),
                      (1, 300, 3, 1))

for (x, y, laplacian, size, dir, hessian) in k:
    cv.Circle(image_gray, (x,y), 0, cv.CV_RGB(255, 255, 255))
    cv.SaveImage(sys.argv[2], img)
