import cv2

from detector import PersonDetector
from pose_estimator import PoseEstimator

detector = PersonDetector()
pose_estimator = PoseEstimator()

cap = cv2.VideoCapture("../data/sample1.mp4")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    persons = detector.detect(frame)

    for (x1, y1, x2, y2) in persons:

        roi = frame[y1:y2, x1:x2]

        result = pose_estimator.process(roi)

        if result.pose_landmarks:

            pose_estimator.drawer.draw_landmarks(
                roi,
                result.pose_landmarks,
                pose_estimator.mp_pose.POSE_CONNECTIONS
            )

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

    cv2.imshow("Fall Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()