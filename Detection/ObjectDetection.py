from main import *
from BasicFunctions import *
from Drawing.ParseArduino import eval
from Drawing.ParseArduino import evalM
import numpy as np
import imutils
import cv2
from time import sleep as delay

rows = open("NNDataset/synset_words.txt").read().strip().split("\n")
	

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]

COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# load our serialized model from disk
net = cv2.dnn.readNetFromCaffe("NNDataset/MobileNetSSD_deploy.prototxt.txt",
	"NNDataset/MobileNetSSD_deploy.caffemodel")

shift = 0
fr = 60
runId = 0
firstRun = True

dists = 0

px = None

def reset():
	runId = 0

def drawObjects(name, frame, filter = "all", return_bottle_imgs = False):
	global fr, shift, runId, dists, firstRun, px, marker
	marker = True
	img = None
	label = "None"	

	frame = imutils.resize(frame, width=400)

	(h, w) = frame.shape[:2]
	frame = cv2.resize(frame, (300, 300))
	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843,
	(300, 300), 127.5)
	net.setInput(blob)
	detections = net.forward()


	for i in np.arange(0, detections.shape[2]):
		confidence = detections[0, 0, i, 2]
		img=None

		idx = int(detections[0, 0, i, 1])
		box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = box.astype("int")
		psx = startX

		startX = startX-((endX-startX)/2)
		endX = endX-((endX-psx)/2)

		centerX = int((startX+endX))
		centerY = int((startY+endY))

		if confidence * 100 >= fr and (filter == "all" or CLASSES[idx] == filter):
			label = "{}".format(CLASSES[idx], confidence * 100)
		if return_bottle_imgs:
			startX += shift
			endX -= shift
			startY += shift+20
			endY -= shift
			i += 1
			y = startY - 15 if startY - 15 > 15 else startY + 15
			if filter == "bottle":
				text = ""
				dist = getDist(map(centerX-5, 0, w, 0, 300), map(centerY, 0, h, 0, 320))
				if int(dist) != 0:
					angle = int(getAngleFromDepth(centerX-1, centerY-1, dist, w)/1.45)				
				if px == None:
					px = centerX
				if firstRun:
					mmTime = 10.02
					#evalM('nice1()')
					#waitArduino()
					eval('gt(' + str(angle) + ', ' + str(int(dist)-350) + ')')
					#waitArduino(False)
					#evalM('nice2(' + str(mmTime*(int(dist)-350)) + ')')
					#runId += 1
					#exit()
					#px = centerX
					firstRun = False
				#cv2.rectangle(frame, fixPoint(startX, startY), fixPoint(endX, endY),
				#COLORS[idx], 2)
#				cv2.putText(frame, real_color + str(dist), (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255, 2)

		
		if label in ["person", "bottle"]:
			y = startY - 15 if startY - 15 > 15 else startY + 15
			cv2.putText(frame, label, (int(startX), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, COLORS[int(idx)], 2)
			cv2.rectangle(frame, (int(startX), int(startY)), (int(endX), int(endY)), COLORS[int(idx)], 2)
	cv2.imshow(name, frame)
