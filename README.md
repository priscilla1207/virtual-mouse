# Virtual Mouse using OpenCV

A hand gesture-controlled virtual mouse built using Python, OpenCV, and MediaPipe.
This project allows users to control the computer cursor using finger movements captured through a webcam.

## Features

* Move cursor using hand gestures
* Left click functionality
* Real-time hand tracking
* Smooth cursor movement
* Webcam-based interaction
* Built with Computer Vision techniques

## Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI
* NumPy

## How It Works

The webcam captures hand movements in real time.
MediaPipe detects hand landmarks and tracks finger positions.
Specific gestures are mapped to mouse actions like cursor movement and clicking.

## Installation

Clone the repository:

```bash
git clone https://github.com/priscilla1207/virtual-mouse.git
```

Move into the project folder:

```bash
cd virtual-mouse
```

Install dependencies:

```bash
pip install opencv-python mediapipe pyautogui numpy
```

## Run the Project

```bash
python mouse.py
```

## Controls

| Gesture                     | Action      |
| --------------------------- | ----------- |
| Index Finger Up             | Move Cursor |
| Index + Middle Finger Close | Left Click  |

## Future Improvements

* Right click support
* Drag and drop functionality
* Volume control gestures
* Multi-hand support
* Improved gesture accuracy

## Project Status

Completed and open-source on GitHub.

#demo

## Demo Video

https://github.com/priscilla1207/virtual-mouse/assets/

## Author

Priscilla1207
