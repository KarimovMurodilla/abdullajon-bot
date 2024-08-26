import requests
url = "https://api.muxlisa.uz/v1/api/services/tts/"

token = ""
text = "Nima gap"
speaker_id = 1

payload = f"token={token}&text={text}&speaker_id={speaker_id}"

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

with open("response.ogg", "wb") as f:
    f.write(response.content)
