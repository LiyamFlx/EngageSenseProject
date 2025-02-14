import unittest
from src.main import analyze_engagement

class TestEngageSense(unittest.TestCase):

    def test_analyze_engagement(self):
        # Test case for analyze_engagement function
        input_data = {
            "audio": [0.5, 0.7, 0.6],
            "video": [0.8, 0.9, 0.85],
            "biometric": [0.6, 0.65, 0.7]
        }
        expected_output = {
            "engagement_score": 0.75,
            "details": {
                "audio_score": 0.6,
                "video_score": 0.85,
                "biometric_score": 0.65
            }
        }
        result = analyze_engagement(input_data)
        self.assertEqual(result, expected_output)

    def test_analyze_engagement_empty_input(self):
        # Test case for empty input
        input_data = {}
        expected_output = {
            "engagement_score": 0,
            "details": {
                "audio_score": 0,
                "video_score": 0,
                "biometric_score": 0
            }
        }
        result = analyze_engagement(input_data)
        self.assertEqual(result, expected_output)

    def test_analyze_engagement_partial_input(self):
        # Test case for partial input
        input_data = {
            "audio": [0.5, 0.7, 0.6]
        }
        expected_output = {
            "engagement_score": 0.6,
            "details": {
                "audio_score": 0.6,
                "video_score": 0,
                "biometric_score": 0
            }
        }
        result = analyze_engagement(input_data)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
