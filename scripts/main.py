import webbrowser
from datetime import datetime

from generate_response import generate_response
from speech_to_text import speech_to_text
from text_to_speech import text_to_speech
from play_audio import play_audio
from picture_generator import image_generation

def main():

    prompt = [{"role": "system", "content": """As an AI language model, I try my best to understand and respond 
    in the language that is used to communicate with me. If you ask me a question in English, I will respond in 
    English. If you ask me a question in Korean, I will respond in Korean. If you ask me a question in Russian, 
    I will respond in Russian."""}]
    # prompt = [{"role": "system", "content": "As your best friend, I try my best to understand and respond on your questions."}]
    
    while(True):

        my_message = speech_to_text()
        print(f"\nHuman: \033[94m{my_message}\033[0m")

        if my_message.strip().lower().replace(".", "") in ['нарисуй', "draw a picture", "그려 줘", "그려 주세요", "그려줘"]:
            play_audio("sound/ok.mp3")
            prompt = speech_to_text()

            if prompt:

                print(f"Drawing: {prompt}. Please wait a second, thanks\n")
                play_audio("sound/drawing.mp3")
                
                created_image_urls = image_generation(prompt, 4)
                for url in created_image_urls:
                    webbrowser.open(url, new=0, autoraise=True)
                play_audio("sound/done.mp3")

            else: 
                play_audio("sound/sorry.mp3")
        

        else: #chatGPT response 

            prompt.append({"role":"user","content":my_message})
            gpt_response = generate_response(prompt)

            print(f"AI: \033[92m{gpt_response}\033[0m\n")
            prompt.append({"role": "system", "content": gpt_response})

            #made a uniq filename
            date_string = datetime.now().strftime("%d%m%Y%H%M%S")
            filename = "sound/gpt_response/voice"+date_string+".mp3"

            text_to_speech(gpt_response, filename)
            play_audio(filename)


if __name__ == "__main__":
    main()