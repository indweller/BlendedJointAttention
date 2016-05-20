import cv2
import numpy as np
def get_cascades():
	faceCascade1 = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
	faceCascade2 = cv2.CascadeClassifier('haarcascades/haarcascade_profileface.xml')
	eyecascade1 = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
	eyecascade2 = cv2.CascadeClassifier('haarcascades/haarcascade_eye_tree_eyeglasses.xml')
def video_capture():
	cam = cv2.VideoCapture(-1)
	cam.set(3,640)
	cam.set(4,480)
	video_capture = cam
	return video_capture
#define main function
def pupil_detect():
	get_cascades()
	video_capture = video_capture()
	cam = cv2.VideoCapture(-1)
	cam.set(3,640)
	cam.set(4,480)
	video_capture = cam

	while True:
	    # Capture frame-by-frame
	    ret, frame = video_capture.read()
	    if ret:
	        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	        faces1 = faceCascade1.detectMultiScale(gray, 1.1, 5)
	        faces2 = faceCascade2.detectMultiScale(gray, 1.1, 5)
	        # Draw a rectangle around the faces
	        for (x, y, w, h) in faces1:
	            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
	            roi_gray = gray[y:y+h, x:x+w]
	            roi_color = frame[y:y+h, x:x+w]