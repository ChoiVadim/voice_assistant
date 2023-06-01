import pygame

def play_audio(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)

def main():
    play_audio("text_to_speech_test.mp3")

if __name__ == "__main__":
    main()