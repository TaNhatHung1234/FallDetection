import mediapipe as mp

class PoseEstimator:

    def __init__(self):

        self.mp_pose = mp.solutions.pose

        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            model_complexity=1
        )

        self.drawer = mp.solutions.drawing_utils

    def process(self, roi):

        rgb = roi[:,:,::-1]

        result = self.pose.process(rgb)

        return result