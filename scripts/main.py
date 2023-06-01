import webbrowser
from datetime import datetime

from generate_response import generate_response
from speech_to_text import speech_to_text
from text_to_speech import text_to_speech
from play_audio import play_audio
from picture_generator import image_generation

def main():

    while(True):

        print("I'm listening...\n")
        my_message = speech_to_text()
        print(f"You: {my_message}\n")

        if my_message.strip().lower().replace(".", "") in ['нарисуй', "draw", "그려 줘", "그려 주세요"]:

            play_audio("sound/ok.mp3")
            prompt = speech_to_text()

            if prompt:

                print(f"Drawing: {prompt}. Please wait a second, thanks\n")
                play_audio("sound/drawing.mp3")

                created_image_url = list(image_generation(prompt))[0]
                webbrowser.open(created_image_url, new=0, autoraise=True)
                play_audio("sound/done.mp3")

            else: 
                play_audio("sound/sorry.mp3")
        

        else: #chatGPT response 
            
            gpt_response = generate_response(my_message)
            print(f"ChatGTP: {gpt_response}\n")

            #made a uniq filename
            date_string = datetime.now().strftime("%d%m%Y%H%M%S")
            filename = "sound/gpt_response/voice"+date_string+".mp3"

            text_to_speech(gpt_response, filename)
            play_audio(filename)


if __name__ == "__main__":
    main()