# Auto Lock Win 10
This mini-script verifies the authenticity of the owner. If it doesn't find them, Windows will fall asleep.

# How to run
## 1) Upload your photo to the "studied" folder.
## 2) You should download [dependencies](https://github.com/ageitgey/face_recognition#installation) on python.
## 3) Start [run.pyw](https://github.com/enotit/AutoLockWin/run.py).


# How it works
When computer's webcam doesn`t see your face a long of time, Windows will fall asleep. 
The script has 5 attempts with an interval of 2 seconds to find a face.
When computer sees your face, the script makes an interval of 5 seconds.

You can assign a task to the task scheduler on windows.

# Thanks 
1) [StackOverflow](https://stackoverflow.com/questions/15921203/how-to-create-a-system-tray-popup-message-with-python-windows)
2) [ageitgey for module on py](https://github.com/ageitgey/face_recognition#installation)