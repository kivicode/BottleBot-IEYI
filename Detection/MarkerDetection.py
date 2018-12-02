from BasicFunctions import *
from Drawing.ParseArduino import eval as evl
import cv2
import cv2.aruco as aruco
import main

font = cv2.FONT_HERSHEY_PLAIN

ft = True


def drawMarkers(name, frame, calibrateByMarker=False, goalMarker=-1, dist=0):
    global ft
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters = aruco.DetectorParameters_create()

    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    (h, w) = frame.shape[:2]
    detect = aruco.drawDetectedMarkers(frame, corners)

    if len(corners) >= 1:
        rect = cv2.boxPoints(cv2.minAreaRect(corners[0]))
        id_count = 0
        current = np.int0(rect)
        midx = 0
        midy = 0
        for pos in current:
            midx += pos[0]
            midy += pos[1]
            if calibrateByMarker and ids[0][0] == goalMarker:
                cv2.circle(frame, (pos[0], pos[1]), 3, (255, 255, 0), 2)
        midx /= len(current)
        midy /= len(current)
        dist = int((int(getDist(midx + 10, midy - 10)) + 20) * 0.837)
        angle = int(getAngleFromDepth(midx, midy, dist, w)*0.57)
        if calibrateByMarker and ids[0][0] == goalMarker and ft:
            cv2.drawContours(frame, [np.int0(rect)], -1, (0, 0, 255), 3)
            mov = "gt(" + str(angle) + ", " + str(dist+50) + ")"
            evl(mov)
            print(mov)
            ft = False
        id_count += 1
    cv2.imshow(name, detect)


def getName(id):
    name = ''

    if id == 1:
        name = 'A'
    elif id == 2:
        neme = 'B'
    elif id == 3:
        neme = 'C'
    elif id == 4:
        neme = 'D'
    elif id == 5:
        neme = 'E'
    elif id == 6:
        neme = 'F'
    elif id == 7:
        neme = 'G'
    elif id == 8:
        neme = 'H'
    elif id == 9:
        neme = 'I'
        return name
