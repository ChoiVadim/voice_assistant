import openai
import speech_recognition as sr

def speech_to_text():

    r = sr.Recognizer()
    r.energy_threshold = 4000

    try:
        with sr.Microphone() as source:
            print("I'm listening...")
            audio = r.listen(source, timeout = 10)

        with open("sound/microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())

        #openai whisper speech to text 
        audio_file= open("sound/microphone-results.wav", "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file).text
    except:
        transcript = ''

    return transcript

def main():
    print(speech_to_text())

if __name__ == "__main__":
    main()