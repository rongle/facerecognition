import cv2
import sys
import numpy
import os

def face_recognize(filename):
  path = os.getcwd()
  filepath = ''
  for files in os.walk(path + '/videos/'):
    if filename in files[2]:
      filepath = path + '/videos/' + filename

  cascPath="haarcascade_frontalface_alt2.xml"
  faceCascade = cv2.CascadeClassifier(cascPath)
  #faceCascade.load(cascPath)

  video_capture = cv2.VideoCapture(filepath)

  #video_capture = cv2.VideoCapture(0)
  while True:
   # Capture frame-by-frame
     ret, frame = video_capture.read()
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     faces = faceCascade.detectMultiScale(
         gray,
         scaleFactor=1.1,
         minNeighbors=3,
         minSize=(30, 30),
         #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
     )

     # Draw a rectangle around the faces
     for (x, y, w, h) in faces: 
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "person", (x+w, y+h), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
     # Display the resulting frame
     cv2.imshow('Video', frame)
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break
  # When everything is done, release the capture
  video_capture.release()
  cv2.destroyAllWindows()