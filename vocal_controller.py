from typing import Callable, Dict, List

from basic_speech_to_text import speech_to_text
from plant_intent_recognizer.detect_intent import RasaIntent, Intent


class VocalController:

    def __init__(self):
        self.rasa_intent = RasaIntent()
        self._callbacks: Dict[Intent, List[Callable[[], None]]] = {}

    def run(self):
        while True:
            text = speech_to_text()
            print(f"text: {text}")
            if text:
                intent = self.rasa_intent.detect_intent(text)
                print(f"intent: {intent}\n")
                self._trigger_function(intent)

    def register_function(self, f: Callable[[Intent], None], *, intent: Intent):
        """If com received a message with the given tag, trigger the function f"""
        functions = self._callbacks.get(intent, [])
        functions.append(f)
        self._callbacks[intent] = functions

    def _trigger_function(self, intent: Intent):
        """Trigger all function registered for this message (based on tag)"""
        if intent not in self._callbacks:
            return
        functions = self._callbacks[intent]
        for f in functions:
            f()


if __name__ == '__main__':
    def greeting():
        print("Hello !")

    vc = VocalController()
    vc.register_function(greeting, intent=Intent.SALUTATION)
    vc.run()

