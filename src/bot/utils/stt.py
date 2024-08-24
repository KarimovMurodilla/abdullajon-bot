import ffmpeg
import speech_recognition as sr


class Stt:
    def convert_ogg_to_wav(self, path: str, input_file: str, output_file: str) -> str:
        try:
            input_f = f"{path}/{input_file}"
            output_f = f"{path}/{output_file}"
            ffmpeg.input(input_f).output(output_f).run()
            print(f"Conversion successful: {output_f}")
            return output_f
        except ffmpeg.Error as e:
            print(f"Error during conversion: {e}")

    def recognize_speech_from_file(self, path: str, file_name: str) -> str:
        recognizer = sr.Recognizer()

        wav_file = self.convert_ogg_to_wav(path, f"{file_name}.ogg", f"{file_name}.wav")

        with sr.AudioFile(wav_file) as source:
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data, language="uz-UZ")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Sorry, my speech service is down; {e}")
