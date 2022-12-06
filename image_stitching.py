#CODE BY DASHPREET SINGH
#IMAGE STITCHING OPENCV

from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import re




folder = r'C:\Users\KUNAL SINGH\OneDrive\Desktop\image_stitching\img\folder_3'

output = r'C:\Users\KUNAL SINGH\OneDrive\Desktop\image_stitching\output_data\pic.jpg'


print("[INFO] loading images...")

imagePaths = sorted(list(paths.list_images(folder)))
images = []
imgs = []

for imagePath in imagePaths:
	image = cv2.imread(imagePath)
	images.append(image)
    
# print(type(images))
   

for i in range(len(imagePaths)):
    imgs.append(cv2.imread(imagePaths[i]))
    # imgs[i]=cv2.resize(imgs[i],(0,0),fx=0.1,fy=0.1) #resize 
    imgs[i] = cv2.resize(imgs[i],(600, 500))



print("[INFO] stitching images...")
stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
	


(status, stitched) = stitcher.stitch(imgs)
# print(status,stitched)



if status == 0:
	
    cv2.imwrite(output, stitched)
    print("STITCH SUCCESSFULLY")
    cv2.imshow("STITCHED IMAGE", stitched)
    cv2.waitKey(0)

elif status == 1:
    print("[INFO] Error 1 occurs (KEYPOINTS FAILED ERROR)")
elif status == 2:
    print("[INFO] Error 2 occurs (IMAGE HOMOGRAPY MATRIX ERROR)")
elif status == 3:
    print("[INFO] Error 3 occurs (CAMERA PARAMETER ADJUST ERROR)")
else:
	pass
    
    





    