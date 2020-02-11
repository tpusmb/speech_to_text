from basic_speech_to_text import speech_to_text
from plant_intent_recognizer.detect_intent import RasaIntent


class VocalController:

    def __init__(self):
        self.rasa_intent = RasaIntent()

    def run(self):
        while True:
            text = speech_to_text()
            print(f"text: {text}")
            if text:
                intent = self.rasa_intent.detect_intent(text)
                print(f"intent: {intent}\n")


if __name__ == '__main__':
    VocalController().run()
