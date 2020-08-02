import cv2
import numpy as np
import out as out
import pyautogui
import sounddevice
from scipy.io.wavfile import write



#Screen Recording
screen_size=(1920,1080)
fourcc= cv2.VideoWriter_fourcc(*"XVID")
out= cv2.VideoWriter("output.mp4",fourcc,20.0,(screen_size))

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("show",frame)
    if cv2.waitKey(1)==ord("q"):
        break