commands = []
import time

from Detection.DepthDetection import *
from Detection.MarkerDetection import *
from Detection.QRCodeDetection import *
from Detection.BarcodeDetection import *
from Detection.ColorDetection import *
from Detection.ObjectDetection import *
from Detection.ContourDetection import *
from Detection.EllipseDetection import *
# from Drawing.DrawWay import *
from Drawing.ParseArduino import eval as evl
from Drawing.ParseArduino import evalM as evlM
from Drawing.ParseArduino import waitArduino
# from Tests.test import *
from BasicFunctions import *
import cv2
import sys
depth = False
marker = True
qrcode = True
bottles = False
objects = True
test = False
colors = False
ellipse = False

plane = "objects()"

def depth():
    drawContours(globalName, frame, 500, False)

def marker():
    drawMarkers(globalName, frame, calibrateByMarker = True)
def qrcode():
    drawDecodedQRcode(globalName, frame)

def bottles():
    drawObjects(globalName, frame, filter="bottle", return_bottle_imgs = True)

def objects():
    drawObjects(globalName, frame, filter="all", return_bottle_imgs = True)


iseval = False
# main.calibrateByMarker = False

globalName = "Depth"

distToObject = 0

path = ["f(900)", "r(90)", "f(400)"]
fr = True

#print(sys.argv)
if "-e" in sys.argv:
    evl(sys.argv[2].replace("[","(").replace("]", ")"))
    iseval = True
    exit()
elif "-em" in sys.argv:
    evlM(sys.argv[2].replace("[","(").replace("]", ")"))
    iseval = True
    exit()
if __name__ == "__main__" and not iseval:
  #  evlM("zero()")
    # writeToFile("Commands.txt", "", clear=True)
#    frame = get_video()
    cv2.namedWindow(globalName, cv2.WND_PROP_FULLSCREEN)
#    evl("f(1000)")
    #follow(path)

    while 1:
        start_time = time.time()
        frame = get_video()
        #frame = getCamVideo()
        # detectContours(globalName+"1",get_video())
        #waitArduino()

        #dm = getDepthMap()
        #getBrightest(dm, 100)
        #cv2.circle(frame, minLoc, 5, 3,(0,255,0),2)
 #       print(frame)
        #cv2.imshow("Monipulator Cam", get_depth())

        for t in plane.split("|"):
            exec(t)
        print("FPS: ", 1.0 / (time.time() - start_time))
        k = cv2.waitKey(5) & 0xFF
        if k == ord('q'):
            break
        elif k == ord('d'):
            depth = (not depth)
        elif k == ord('m'):
            marker = (not marker)
        elif k == ord('n'):
            qrcode = (not qrcode)
        elif k == ord('b'):
            bottles = (not bottles)
        elif k == ord('o'):
            objects = (not objects)
        elif k == ord('p'):
            calibrateByMarker = not calibrateByMarker
        elif k == ord('e'):
            ellipse = not ellipse
        elif k == ord('r'):
            reset()
        elif k == ord('g'):
            evl("b(670)")
    cv2.destroyAllWindows()
