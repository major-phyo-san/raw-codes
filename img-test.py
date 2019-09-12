import numpy as np
import cv2
import imutils

imagePaths = ["images/m2.JPG","images/m1.JPG","images/m3.JPG"]
images = []
i=1


for imagePath in imagePaths:
	images.append(cv2.imread(imagePath))
	cv2.imshow("image"+str(i),images[i-1])
	cv2.waitKey(0) & 0xFF
	cv2.destroyAllWindows()
	i = i+1

stitcher = cv2.createStitcher(try_use_gpu=False)
(status, stitched) = stitcher.stitch(images)

if status == 0:
	stitched = cv2.copyMakeBorder(stitched, 10,10,10,10,
cv2.BORDER_CONSTANT, (0,0,0))
	gray = cv2.cvtColor(stitched, cv2.COLOR_BGR2GRAY)
	thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)[1]
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	c = max(cnts, key=cv2.contourArea)
	mask = np.zeros(thresh.shape, dtype="uint8")
	(x,y,w,h) = cv2.boundingRect(c)
	cv2.rectangle(mask,(x,y),(x+w,y+h),255,-1)
	minRect = mask.copy()
	sub = mask.copy()

	while cv2.countNonZero(sub) > 0:
		minRect = cv2.erode(minRect, None)
		sub = cv2.subtract(minRect, thresh)

	cnts = cv2.findContours(minRect.copy(), cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	c = max(cnts, key=cv2.contourArea)
	(x,y,w,h) = cv2.boundingRect(c)
	stitched = stitched[y:y + h, x:x + w]

	cv2.imshow("Pano Img", stitched)
	cv2.waitKey(0) & 0xFF
	cv2.destroyAllWindows()

	
	


