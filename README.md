# face_sleep_detection
face_sleep_detection
# Drowsiness Detection Project

This project detects drowsiness using a webcam feed and OpenCV. It identifies whether a person is potentially falling asleep by detecting the absence of a face.

## Prerequisites

Before running the code, make sure you have the following installed:

*   **Python:** Python 3.6 or higher is required. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

*   **pip:** The Python package installer, `pip`, is needed to install the required libraries.  It usually comes with Python installations. Verify that it is installed with `pip --version`.

*   **OpenCV:** OpenCV (cv2) is used for image processing and face detection. Install it using pip:

    ```
    pip install opencv-python
    ```

## Installation and Setup

1.  **Download the code:** Save the `detect_drowsiness.py` file (or whatever you named it) to a directory on your computer.

2.  **(Optional) Create a virtual environment:** It is highly recommended to create a virtual environment to isolate the project's dependencies:

    ```
    python -m venv venv  # Create a virtual environment named "venv"
    ```

    *   Activate the virtual environment:

        ```
        venv\Scripts\activate  # On Windows
        source venv/bin/activate  # On macOS/Linux
        ```

3.  **Install Dependencies:** If you're using a virtual environment, make sure it's activated before installing the dependencies. Then, install OpenCV:

    ```
    pip install opencv-python
    ```

## Running the Code

1.  **Open a terminal or command prompt.**

2.  **Navigate to the project directory:**

    ```
    cd /path/to/your/project/directory
    ```

3.  **Run the script:**

    ```
    python detect_drowsiness.py
    ```

4.  **Using the program**:

    *   A window displaying the webcam feed will appear.
    *   If the program detects the absence of a face, it will display the text "FALLING ASLEEP!" on the frame.
    *   Press the 'q' key to exit the program.

## Troubleshooting

*   **`ModuleNotFoundError: No module named 'cv2'`:** This error means that the `cv2` module (OpenCV) is not installed correctly or not found by the Python interpreter. Make sure you have installed `opencv-python` using `pip install opencv-python`.  If you're using a virtual environment, make sure it's activated.
*   **Camera Access Issues:** The program may not be able to access your camera. Check the following:
    *   Make sure your camera is properly connected and turned on.
    *   Close any other applications that might be using the camera (e.g., Skype, Zoom).
    *   Check your operating system's camera privacy settings to ensure that Python is allowed to access the camera.
*   **Performance:** If the program runs slowly, try reducing the frame size in the code (the `resize` function). However, this may also reduce the accuracy of the face detection.

## Important Notes

*   **Accuracy:** This project uses a basic Haar cascade classifier for face detection, which may not be as accurate or robust as more advanced methods.
*   **Lighting Conditions:** Face detection is sensitive to lighting conditions. Make sure the lighting is good in your environment.
*   **Simplified Drowsiness Check:** The drowsiness detection is based solely on the presence or absence of a face. This is a simplified approach and may not be reliable in all situations.

This `README.md` file should give your friend a clear set of instructions for setting up and running the drowsiness detection project. Remember to replace `"detect_drowsiness.py"` with the actual name of your Python script. I hope they enjoy the project!

