"""
The MIT License (MIT)

Copyright © 2022 «enotit»

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import face_recognition
import cv2
from win32api import *
import win32gui as wingui
import sys, os
import win32con
import time
import ctypes
import threading


class WindowsBalloonTip:
    def push(self, title, msg):
        message_map = {
                win32con.WM_DESTROY: self.OnDestroy,
        }
        wc = wingui.WNDCLASS()
        hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = str("PythonTaskbar")
        wc.lpfnWndProc = message_map # could also specify a wndproc.
        try:
            self.classAtom = wingui.RegisterClass(wc)
        except:
            pass
        # Create the Window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = wingui.CreateWindow( self.classAtom, "Taskbar", style, \
                0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, \
                0, 0, hinst, None)
        wingui.UpdateWindow(self.hwnd)
        iconPathName = os.path.abspath(os.path.join(sys.path[0], "./src/icon.ico" ))
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
        try:
           hicon = wingui.LoadImage(hinst, iconPathName, \
                    win32con.IMAGE_ICON, 0, 0, icon_flags)
        except:
          hicon = wingui.LoadIcon(0, win32con.IDI_APPLICATION)
        flags = wingui.NIF_ICON | wingui.NIF_MESSAGE | wingui.NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER+20, hicon, "tooltip")
        wingui.Shell_NotifyIcon(wingui.NIM_ADD, nid)
        wingui.Shell_NotifyIcon(wingui.NIM_MODIFY, \
                         (self.hwnd, 0, wingui.NIF_INFO, win32con.WM_USER+20,\
                          hicon, "Balloon  tooltip",msg,200,title))
        time.sleep(2)
        wingui.DestroyWindow(self.hwnd)
        

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        wingui.Shell_NotifyIcon(wingui.NIM_DELETE, nid)
        PostQuitMessage(0) # Terminate the app.



w=WindowsBalloonTip()
def push_notify(title, msg):
    threading.Thread(target=w.push, args=(title, msg)).start()


# Create arrays of known face encodings
known_face_encodings = []

for path in os.listdir("./studied/"):
    try:
        encoding = face_recognition.face_encodings(face_recognition.load_image_file("./studied/"+path))[0]
        known_face_encodings.append(encoding)
    except:
        print(f"Error with image {'./studied/'+path}")


push_notify("Successfully", "Programm has been started")

# Set webcam(.com)
video_capture = cv2.VideoCapture(0)

# Initialize some variables
face_locations = []
face_encodings = []
attempts = 0
running = True

while running:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    
    if len(face_locations) == 0:
        attempts += 1
    is_Auth_Person = False
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        if True in matches:
            time.sleep(5)
            attempts = 0
            is_Auth_Person = True
            break
    
    if not is_Auth_Person:
        if attempts == 5:
            push_notify("Alert", "You have one last chance")
        if attempts >= 6:
            push_notify("ERROR", "I go to bed")
            # A lot of attempts, go to bed        
            ctypes.windll.user32.LockWorkStation()
            break
        attempts += 1

    time.sleep(3)
    cv2.waitKey(1)


# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
# toaster.on_destroy()
