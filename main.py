import webbrowser
from datetime import datetime

from generate_response import generate_response
from speech_to_text import speech_to_text
from text_to_speech import text_to_speech
from play_audio import play_audio
from picture_generator import image_generation


def main():

    while(True):

        my_message = speech_to_text()
        print(f"You: {my_message}\n")

        if my_message.lower() in ['нарисуй', 'нарисуй.']:

            play_audio("sound/okidraw.mp3")
            prompt = speech_to_text()
            if prompt:
                print(f"Drawing: {prompt}\nPlease wait a second, thanks")
                play_audio("sound/drawing.mp3")

                created_image_url = list(image_generation(prompt))[0]
                webbrowser.open(created_image_url, new=0, autoraise=True)
                play_audio("sound/done.mp3")
            else: print("I didn't hear what need to draw, sorry")
        
        else:
            gpt_response = generate_response(my_message)
            print(f"ChatGTP: {gpt_response}\n")

            #made a uniq filename
            date_string = datetime.now().strftime("%d%m%Y%H%M%S")
            filename = "sound/gpt_response/voice"+date_string+".mp3"

            text_to_speech(gpt_response, filename)
            play_audio(filename)

if __name__ == "__main__":
    main()