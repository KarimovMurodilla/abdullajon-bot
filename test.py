import requests
import time

from src.configuration import conf

# Укажите ваш ключ API и URL-адрес конечной точки
api_key = conf.TTS_TOKEN
region = 'eastus'  # Например, 'eastus'
endpoint = f'https://{region}.tts.speech.microsoft.com/cognitiveservices/v1'

# Текст для озвучивания
text = "Salom"

# Заголовки
headers = {
    'Ocp-Apim-Subscription-Key': api_key,
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
response = requests.post(endpoint, headers=headers, data=ssml)

# Проверка успешности запроса и сохранение аудиофайла
if response.status_code == 200:
    with open('output.mp3', 'wb') as audio_file:
        audio_file.write(response.content)
    print("Аудиофайл успешно сохранен как output.mp3")
else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)
