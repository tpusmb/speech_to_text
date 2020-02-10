#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File to manage the speech to text on our robots.
"""

import speech_recognition as sr


def speech_to_text():
    """
    Function called to listen and convert to text the answer of the user.
    Note that the user have to talk in french.
    :return: (string) The answer of the user
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        # Call the google voice recognizer and put the answer in the local
        # variable "text" as String
        text = r.recognize_google(audio, language="fr-FR")

        # Return a string containing the answer of the user
        return text
    except sr.UnknownValueError:
        return "None"
    except sr.RequestError as e:
        return "None"


if __name__ == "__main__":
    print(speech_to_text())
