#Cross spread implemetation

import cv2
import numpy as np
import dlib 

def process_eye(split):
	split = cv2.GaussianBlur(split,(5,5),0)
	split = cv2.adaptiveThreshold(split,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
	split = cv2.dilate(split, None, iterations=1)
	return split

def filter_eye(split):
	split = cv2.medianBlur(split,5)
	split = cv2.bilateralFilter(split,9,75,75)
	return split

def cross_spread(split):
	flag = 0
	first= [0,0]
	last = [split.shape[0],split.shape[1]]
	for i in range(split.shape[0]):
		for j in range(split.shape[1]):
			if split[i][j]==0 and flag == 0:
				first = [i,j]
				i = split.shape[0]-1
			elif split[i][j]==0:
				last = [i,j]
				i = split.shape[0]-1
	centre = [(last[0]+first[0])/2, (last[1]+first[1])/2]
	return centre

# Video capture via webcam
cam = cv2.VideoCapture(-1)
cam.set(3,640)
cam.set(4,480)
video_capture = cam

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('../dlibcascades/shape_predictor_68_face_landmarks.dat')


while True:
    # Capture frame-by-frame
	ret, frame = video_capture.read()
	if ret:
		frame_color = frame
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		dets = detector(frame, 1)
		for k, d in enumerate(dets):
	        # Get the landmarks/parts for the face in box d.
			shape = predictor(frame, d)
	        # print(type(shape.part(1).x))
			cv2.circle(frame_color,(shape.part(36).x,shape.part(36).y),2,(0,0,255))
			cv2.circle(frame_color,(shape.part(39).x,shape.part(39).y),2,(0,0,255))
			cv2.circle(frame_color,(shape.part(42).x,shape.part(42).y),2,(0,0,255))
			cv2.circle(frame_color,(shape.part(45).x,shape.part(45).y),2,(0,0,255))
			x1 = shape.part(36).x
			y1 = shape.part(37).y-2
			x2 = shape.part(39).x
			y2 = shape.part(40).y+2
			split = frame[y1:y2,x1:x2]
			split = process_eye(split)
			split = filter_eye(split)
			centre = cross_spread(split)
			frame[y1:y2,x1:x2]=split
			cv2.rectangle(frame_color,(x1,y1), (x2,y2), (0, 0, 255), 2)
			print split.shape
			# print centre
			cv2.circle(frame_color,(x1+centre[1],y1+centre[0]),2,(0,0,255))
			x1 = shape.part(42).x
			y1 = shape.part(43).y-2
			x2 = shape.part(45).x
			y2 = shape.part(46).y+2
			split = frame[y1:y2,x1:x2]
			split = process_eye(split)
			split = filter_eye(split)
			centre = cross_spread(split)
			frame[y1:y2,x1:x2]=split
			cv2.rectangle(frame_color,(x1,y1), (x2,y2), (0, 0, 255), 2)
			cv2.circle(frame_color,(x1+centre[1],y1+centre[0]),2,(0,0,255))
		
		# Display the resulting frame
        cv2.imshow('Video', frame_color)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()
