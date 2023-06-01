from langdetect import detect
import boto3

def text_to_speech(text, file_name):    #made text to a audio file 

    lang = detect(text)
    
    if lang == 'ru':
        voice = 'Tatyana'
        engine = 'standard'
    elif lang == 'ko':
        voice = 'Seoyeon'
        engine = 'neural'
    else: 
        voice = 'Salli'
        engine = 'neural'

    polly = boto3.client('polly')

    response = polly.synthesize_speech(
        Text=text,
        VoiceId=voice,
        OutputFormat='mp3',
        Engine=engine
    )
    
    with open(file_name, "wb") as f:
        f.write(response['AudioStream'].read())

def main():
    text_to_speech(input(), "text_to_speech_test.mp3")

if __name__ == "__main__":
    main()