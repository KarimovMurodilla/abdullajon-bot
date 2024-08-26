from openai import OpenAI

from src.configuration import conf

class ChatGPT:
    def __init__(self):
        self.client = OpenAI(
            api_key=conf.OPENAI_KEY
        )

    def add_message(self, message: str):
        self.messages = [
            {
                "role": "system",
                "content": "Your name is Abdullajon, you are virtual assistent. Speak only in Uzbek language"
            },
            {
                "role": "user",
                "content": message
            }
        ]
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=self.messages
        )

        return completion.choices[0].message.content
