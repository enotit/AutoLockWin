# Auto Lock Win 10
This mini-script verifies the authenticity of the owner. If it doesn't find them, Windows will fall asleep.

## How to run
1) Upload your photo to the ["studied"](https://github.com/enotit/AutoLockWin/tree/main/studied) folder.
2) You should download [dependencies](https://github.com/ageitgey/face_recognition#installation-options) on python.
3) Start [run.pyw](https://github.com/enotit/AutoLockWin/tree/main/run.pyw).


## How it works
When computer's webcam doesn`t see your face a long of time, Windows will fall asleep. 
The script has 5 attempts with an interval of 2 seconds to find a face.
When computer sees your face, the script makes an interval of 5 seconds.

You can assign a task to the task scheduler on windows.

## Thanks 
1) [StackOverflow](https://stackoverflow.com/questions/15921203/how-to-create-a-system-tray-popup-message-with-python-windows)
2) [ageitgey for module on py](https://github.com/ageitgey/face_recognition#installation)

![py](https://css-info.ru/wp-content/uploads/elementor/thumbs/3315-plvpzgwdlkkfqthi7evcumi14lkjvw0txhxmulwc6o.png)
![py](https://upload.wikimedia.org/wikipedia/commons/thumb/archive/4/48/20160616062729%21Windows_logo_-_2012_%28dark_blue%29.svg/120px-Windows_logo_-_2012_%28dark_blue%29.svg.png)
