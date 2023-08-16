import unittest
from fastapi.testclient import TestClient
from .main import app
import os


class TestAudioUpload(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)
        self.valid_audio = "path_to_valid_audio.mp3"  # replace with path to a valid audio file < 125MB
        self.large_audio = "path_to_large_audio.mp3"  # replace with path to an audio file > 125MB
        self.invalid_file = "path_to_image.jpg"  # replace with path to a non-audio file

    def test_valid_audio_upload(self):
        with open(self.valid_audio, "rb") as f:
            response = self.client.post("/upload/", files={"file": f})
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed, e.g., checking the content of the response

    def test_large_audio_upload(self):
        with open(self.large_audio, "rb") as f:
            response = self.client.post("/upload/", files={"file": f})
        self.assertEqual(response.status_code, 400)
        self.assertIn("File too large", response.text)

    def test_invalid_file_type_upload(self):
        with open(self.invalid_file, "rb") as f:
            response = self.client.post("/upload/", files={"file": f})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid audio file format", response.text)

    def tearDown(self):
        # Clean up any temporary files or resources if needed
        pass

if __name__ == "__main__":
    unittest.main()

