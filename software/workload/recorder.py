import numpy as np
import cv2
from PyQt5.QtWidgets import QApplication
import sys

class Recorder():
    def playVideo(self):
        cap = cv2.VideoCapture('output.mp4')

        while(cap.isOpened()):
            ret, frame = cap.read()
            nframe = cv2.flip(frame, 1)

            cv2.imshow('frame', nframe)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def recordVideo(self, e):
        cap = cv2.VideoCapture(0)

        # 640*480, 30fps is the maximum quality of the camera
        cap.set(3, 640)
        cap.set(4, 480)

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('output.mp4',fourcc, 30.0, (640,480))

        #print(cap.get(cv2.CAP_PROP_FPS))

        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret==True:
                nframe = cv2.flip(frame, 1)

                # write the flipped frame
                out.write(nframe)

                cv2.imshow('frame', nframe)
                if e.is_set():
                    break

        # Release everything if job is finished
        cap.release()
        out.release()
        cv2.destroyAllWindows()
