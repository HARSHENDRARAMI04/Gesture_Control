# Gesture-Controlled Navigation

This project implements a gesture-based navigation system using a webcam, OpenCV, and MediaPipe. It allows users to control browser navigation and scrolling with hand gestures.

## Features
- **Swipe Left** → Moves to the previous page/tab (`Alt + Left`)
- **Swipe Right** → Moves to the next page/tab (`Alt + Right`)
- **Swipe Up** → Scrolls up
- **Swipe Down** → Scrolls down

## Tech Stack
- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

## Installation

### Prerequisites
Ensure you have Python installed on your system.

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/Gesture-Controlled-Navigation.git
   cd Gesture-Controlled-Navigation
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```sh
   python gesture_control.py
   ```
2. Use hand gestures in front of the webcam to navigate:
   - Move hand **left** → Swipe Left
   - Move hand **right** → Swipe Right
   - Move hand **up** → Scroll Up
   - Move hand **down** → Scroll Down
3. Press `q` to exit the application.

## Project Structure
```
Gesture-Controlled-Navigation/
│── gesture_control.py  # Main script for gesture recognition
│── requirements.txt    # List of dependencies
│── README.md           # Project documentation
```

## Contributing
Feel free to fork the repository and contribute. Open a pull request with any improvements or bug fixes.


