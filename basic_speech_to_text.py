"""
File to manage the speech to text for our plant.
"""
from contextlib import suppress
from typing import Union

import speech_recognition as sr


def speech_to_text(noise_level: int = None) -> Union[None, str]:
    """
    Function called to listen and convert to text the answer of the user.
    Note that the user have to talk in french.
    :param: noise_level the level of ambient noise used to detect the end of a phrase
    :return: The answer of the user
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if noise_level:
            r.energy_threshold = noise_level
        else:
            r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    with suppress(sr.UnknownValueError, sr.RequestError):
        # Call the google voice recognizer
        return r.recognize_google(audio, language="fr-FR")


if __name__ == "__main__":
    print(speech_to_text())
