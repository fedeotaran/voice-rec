import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    # read the audio data from the default microphone
    print("Grabando...")
    audio_data = r.record(source, duration=10)
    print("Reconociendo...")
    # convert speech to text
    text = r.recognize_google(audio_data, language="es-ES")
    
    print("Texto reconocido.")
    print(text)
