import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:

    print("Grabando...")
    audio_data = r.record(source, duration=30)

    print("Reconociendo...")
    text = r.recognize_google(audio_data, language="es-ES")
    
    print("Texto reconocido:")
    print(text)
