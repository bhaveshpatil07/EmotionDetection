from EmotionDetection.emotion_detection import emotion_detector
import unittest


class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):
        response1 = emotion_detector('I am glad this happened')
        self.assertEqual(response1["dominant_emotion"], "joy")

        response1 = emotion_detector('I am really mad about this')
        self.assertEqual(response1["dominant_emotion"], "anger")

        response1 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(response1["dominant_emotion"], "disgust")

        response1 = emotion_detector('I am so sad about this')
        self.assertEqual(response1["dominant_emotion"], "sadness")

        response1 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(response1["dominant_emotion"], "fear")      

unittest.main()