#faça um programa em python que abra e reproduza o áudio de um arquivo MP3 com modulos
from time import sleep
import pygame
from time import sleep
pygame.init()
pygame.mixer.music.load("summertime.mp3")
pygame.mixer.music.play()

print('PLAY')
sleep(123)

print('end :)')