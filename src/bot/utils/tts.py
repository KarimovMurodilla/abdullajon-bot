import requests

from src.configuration import conf


class Tts:
    def __init__(self):
        self.url = "https://api.muxlisa.uz/v1/api/services/tts/"
        self.token = conf.TTS_TOKEN
        self.speaker_id = 1

    def text_to_speech(self, text: str, file_path: str) -> str:
        payload = f"token={self.token}&text={text}&speaker_id={self.speaker_id}"

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(self.url, headers=headers, data=payload)

        with open(file_path, "wb") as f:
            f.write(response.content)

        return file_path
