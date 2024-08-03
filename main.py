import speech_recognition
from AppOpener import open, close
from playsound import playsound
import pyttsx3
import chatgpt

def voise():
    engine = pyttsx3.init()
    engine.say("Меня зовут жарвис")
    engine.runAndWait()

# os

a = chatgpt

recognizer = speech_recognition.Recognizer()
while True:
    def audio_rec():
        with speech_recognition.Microphone() as source:
            print("Man eshitvomman...")
            audio = recognizer.listen(source)
        print("Ovozni teks qivomman...")
        try:
            text = recognizer.recognize_google(audio, language='en-En')
            return text
        except speech_recognition.UnknownValueError:
            print("I couldn't understand what you said :(")
        return None

    result = audio_rec()

    if result:
        print(result)

    if result.lower() == "hello":
        print("Меня зовут Джарвис")
        playsound('voices/Salom_Jr.mp3')
        continue

    elif result.lower() == "hello jarvis":
        # voice = open("voices/pastlives.mp3", "rb")
        playsound('voices/H_mr.mp3')
        continue
    elif result.lower() == "i am mister" or result.lower() == "i am mr":
        playsound('voices/MR.mp3')
        continue
    elif result.lower() == "i am okay" or result.lower() == "i'm okay":
        playsound('voices/open_pr.mp3')
        continue
    elif result.lower() == "no problem":
        playsound('voices/open-pr.mp3')
        continue
    elif result.lower() == "open telegram":
        print("Telegram ochildi")
        open("telegram", match_closest=True)
        playsound('voices/tg_open.mp3')
        continue
    elif result.lower() == "stop telegram":
        close("telegram", match_closest=True)
        playsound('voices/tg_sd.mp3')
        continue
    elif result.lower() == "open youtube":
        print("You tube ochildi")
        open("you tube", match_closest=True)
        playsound('voices/yt_open.mp3')
        continue
    elif result.lower() == "stop youtube":
        close("you tube", match_closest=True)
        playsound('voices/yt_sd.mp3')
        continue
    elif result.lower() == "open google":
        open("google chrome", match_closest=True)
        playsound('voices/gg_open.mp3')
        continue
    elif result.lower() == "stop google":
        close("google chrome", match_closest=True)
        playsound('voices/gg_sd.mp3')
        continue
    elif result.lower() == "stop" or result.lower() == "stop jarvis":
        engine = pyttsx3.init()
        engine.say("Я закончил")
        engine.runAndWait()
        break
    elif result.lower() == "i am miss" or result.lower() == "i'm miss":
        playsound('voices/MS.mp3')
        continue
    elif result.lower() == "i am okay" or result.lower() == "i'm okay":
        playsound('voices/open_pr.mp3')
        continue
    elif result.lower() == "no problem":
        playsound('voices/open-pr.mp3')
        continue
    elif result.lower() == "open telegram":
        print("Telegram ochildi")
        open("telegram", match_closest=True)
        playsound('voices/tg_open.mp3')
        continue
    elif result.lower() == "stop telegram":
        close("telegram", match_closest=True)
        playsound('voices/tg_sd.mp3')
        continue
    elif result.lower() == "open youtube":
        print("You tube ochildi")
        open("you tube", match_closest=True)
        playsound('voices/yt_open.mp3')
        continue
    elif result.lower() == "stop youtube":
        close("you tube", match_closest=True)
        playsound('voices/yt_sd.mp3')
        continue
    elif result.lower() == "open google":
        open("google chrome", match_closest=True)
        playsound('voices/gg_open.mp3')
        continue
    elif result.lower() == "stop google":
        close("google chrome", match_closest=True)
        playsound('voices/gg_sd.mp3')
        continue
    elif result.lower() == "stop" or result.lower() == "stop jarvis":
        engine = pyttsx3.init()
        engine.say("Я закончил")
        engine.runAndWait()
        break



    # elif result.lower() == "i am okay" or result.lower() == "i'm okay":
    #     playsound('voices/open_pr.mp3')
    #     continue
    #
    # elif result.lower() == "no problem":
    #     playsound('voices/open-pr.mp3')
    #     continue
    #
    # elif result.lower() == "open telegram":
    #     print("Telegram ochildi")
    #     open("telegram", match_closest=True)
    #     playsound('voices/tg_open.mp3')
    #     continue
    #
    # elif result.lower() == "stop telegram":
    #     close("telegram", match_closest=True)
    #     playsound('voices/tg_sd.mp3')
    #     continue
    #
    # elif result.lower() == "open youtube":
    #     print("You tube ochildi")
    #     open("you tube", match_closest=True)
    #     playsound('voices/yt_open.mp3')
    #     continue
    #
    # elif result.lower() == "stop youtube":
    #     close("you tube", match_closest=True)
    #     playsound('voices/yt_sd.mp3')
    #     continue
    #
    # elif result.lower() == "open google":
    #     open("google chrome", match_closest=True)
    #     playsound('voices/gg_open.mp3')
    #     continue
    #
    # elif result.lower() == "stop google":
    #     close("google chrome", match_closest=True)
    #     playsound('voices/gg_sd.mp3')
    #     continue
    #
    # elif result.lower() == "stop" or result.lower() == "stop jarvis":
    #     engine = pyttsx3.init()
    #     engine.say("Я закончил")
    #     engine.runAndWait()
    #     break