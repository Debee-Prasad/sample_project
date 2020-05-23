import speech_recognition as sr
def main():
    voice = "Recording_4.wav"
    r= sr.Recognizer()
    with sr.AudioFile(voice) as source:
        r.adjust_for_ambient_noise(source)
        print("Converting Audio file to Text")

        audio = r.listen(source)

        try:
            print("Converted Audio is :\n"+r.recognize_google(audio))
        except Exception as e:
            print(e)

if __name__=="__main__":
    main()