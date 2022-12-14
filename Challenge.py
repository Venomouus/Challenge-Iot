import speech_recognition as sr
import pyttsx3, speech_recognition as sr
import pyttsx3

en = pyttsx3.init()

msg = "Seja Bem vindo ao nosso programa de acessibilidade!" 

en.say(msg)
en.runAndWait()

engine = pyttsx3.init()

voices = engine.getProperty("voices") 
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', 1)
engine.setProperty("rate", 155)


engine.runAndWait() 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n  Listening...\n")
        speak('ouvindo.')
        r.adjust_for_ambient_noise = 1.25
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("  Recognizing...\n")
        speak('Reconhecendo.')
        query = r.recognize_google(audio, language='pt')
    except:
        return "©empty_^_^_queryª"
    return query

print("( ͡° ͜ʖ ͡°)")
speak("Iniciando a conversão")
if __name__ == "__main__":
    while True:

        query = command().lower()
        if '1' in query:
            speak(query)
            break
        else:
            print("Voce disse...\n")
            print(query)
            break
