from typing import Callable, Dict, List

from basic_speech_to_text import speech_to_text
from plant_intent_recognizer.detect_intent import RasaIntent, Intent

CALLBACK_INTENTS: Dict[Intent, List[Callable[[], None]]] = {}


def register_function_for_intent(intent: Intent):
    """Register a function to be called every time an intent is detected by VoiceController"""
    def inner_decorator(f):
        def wrapped(*args, **kwargs):
            response = f(*args, **kwargs)
            return response

        print(f"Registering {f} for intent: {intent.value}")
        functions = CALLBACK_INTENTS.get(intent, [])
        functions.append(f)
        CALLBACK_INTENTS[intent] = functions
        return wrapped

    return inner_decorator


def _trigger_function_on_intent(intent: Intent):
    """Trigger all function registered for this intent"""
    if intent not in CALLBACK_INTENTS:
        return
    functions = CALLBACK_INTENTS[intent]
    for f in functions:
        f()


class VoiceController:

    def __init__(self):
        self.rasa_intent = RasaIntent()

    def run(self):
        while True:
            text = speech_to_text()
            print(f"text: {text}")
            if text:
                intent = self.rasa_intent.detect_intent(text)
                print(f"intent: {intent}\n")
                _trigger_function_on_intent(intent)


if __name__ == '__main__':
    """Example on how to use the register_function_for_intent wrapper"""
    @register_function_for_intent(intent=Intent.SALUTATION)
    def greeting():
        print("Hello !")


    @register_function_for_intent(intent=Intent.SALUTATION)
    def greeting2():
        print("Hello 2 !")


    @register_function_for_intent(intent=Intent.FIN)
    def goodbye():
        print("goodbye !")


    vc = VoiceController()
    vc.run()
