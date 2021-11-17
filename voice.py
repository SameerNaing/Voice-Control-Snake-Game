import speech_recognition as sr
import pyautogui


class VoiceControl:
    def __init__(self):
        self.stop_listening = None
        self.__setup()

    def __callback(self, recognizer, audio):
        try:
            text = recognizer.recognize_google(audio)
            if text == "up":
                pyautogui.press("up")
            elif text == "down":
                pyautogui.press("down")
            elif text == "right":
                pyautogui.press("right")
            elif text == "left":
                pyautogui.press("left")
        except:
            pass

    def __setup(self):
        r = sr.Recognizer()
        mic = sr.Microphone()

        with mic as source:
            r.adjust_for_ambient_noise(source)

        self.stop_listening = r.listen_in_background(
            source=mic, callback=self.__callback, phrase_time_limit=5)
