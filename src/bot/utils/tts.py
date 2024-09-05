import requests

from src.configuration import conf


class Tts:
    def __init__(self):
        region = 'eastus'  # Например, 'eastus'
        self.url = f'https://{region}.tts.speech.microsoft.com/cognitiveservices/v1'
        self.speaker_id = 0

    def text_to_speech(self, text: str, file_path: str) -> str:
        # Заголовки
        headers = {
            'Ocp-Apim-Subscription-Key': conf.TTS_TOKEN,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': 'audio-16khz-32kbitrate-mono-mp3'
        }

        # Тело запроса в формате SSML (Speech Synthesis Markup Language)
        ssml = f"""
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="uz-UZ">
                <voice name="uz-UZ-MadinaNeural">
                    {text}
                </voice>
            </speak>
        """

        # Запрос к API
        response = requests.post(self.url, headers=headers, data=ssml)

        with open(file_path, "wb") as f:
            f.write(response.content)

        return file_path
