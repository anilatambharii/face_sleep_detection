import cv2

# Load the Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to check if a person is falling asleep
def check_drowsiness(frame, face_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    if len(faces) > 0:
        # Person is present
        return False  # Not falling asleep (just present for simplicity)
    else:
        # No face detected, assume falling asleep
        return True

# Main function
def main():
    # Initialize video capture
    cap = cv2.VideoCapture(0)  # Use 0 for default camera

    if not cap.isOpened():
        print("Error: Could not open camera.  Check camera connections and permissions.")
        return  # Exit the program

    while True:
        # Read frame from the video stream
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame from camera.  Check camera connections and permissions.")
            break

        # Check for drowsiness
        drowsy = check_drowsiness(frame, face_cascade)

        if drowsy:
            cv2.putText(frame, "FALLING ASLEEP!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Display the frame
        cv2.imshow("Frame", frame)

        # Check for 'q' key press to exit
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    # Release video capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("[INFO] Starting drowsiness detection...")
    main()
