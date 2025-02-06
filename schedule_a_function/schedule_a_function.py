import time
import pygame

def schedule_function(when: float, fun, music, *alert: str):
    while True:
        if round(when, 1) == round(time.time(), 1):
            # fun(music)
            print(*alert)
            break


def play_alarm(music: str):
    pygame.mixer.init()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


schedule_function(time.time()+1, play_alarm,
                  "/home/alhas/Excercises/hip-hop-news-271179.mp3", 'Yo!', 'How Are you?')
