import pygame
import pdb
import os
from pygame import mixer
from tkinter import *
from tkinter import messagebox


pygame.init()
width = 1000
height = 500
window = pygame.display.set_mode((width,height))

pygame.display.set_caption('LoFi Music Player - By Konory')

bg_img = pygame.image.load("wp8102840-pc-4k-aesthetic-wallpapers.jpg")
bg_img = pygame.transform.scale(bg_img,(width,height))
new_bg = pygame.image.load("wp5866591-all-anime-art-wallpapers.jpg")
new_bg = pygame.transform.scale(new_bg, (width, height))
pygame_icon = pygame.image.load("music-app.png")
pygame.display.set_icon(pygame_icon)

bg_img2 = pygame.image.load("wp6400060-aesthetic-on-pc-wallpapers.jpg")
bg_img2 = pygame.transform.scale(bg_img2,(width, height))
 
font = pygame.font.SysFont("arialblack", 40)
Text_color = (255,255,255)

mixer.init()
mixer.music.load("y2mate.com - Lazy 30 minutes Chill HipHop Lofi Beats to relax  study to.mp3")
mixer.music.play()



def newMusic():
    mixer.music.stop()
    mixer.music.load("music2.mp3")
    mixer.music.play()


def oldMusic():
    mixer.music.stop()
    mixer.music.load("y2mate.com - Lazy 30 minutes Chill HipHop Lofi Beats to relax  study to.mp3")
    mixer.music.play()  

def draw_text(text, font, Text_color, x, y):
    img = font.render(text, True, Text_color)
    window.blit(img, (x,y))

runing = True

window.blit(bg_img,(0,0))



while runing:
    
    draw_text("Press SPACE to see the shortcut.", font, Text_color, 135, 400)


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print("LOADING THE NEXT SONG...")
                window.blit(bg_img2,(0,0))
                pygame.display.update()
                newMusic()
            if event.key == pygame.K_UP:
                mixer.music.pause()
            if event.key == pygame.K_DOWN:
                mixer.music.play()
            if event.key == pygame.K_2:
                oldMusic()
                window.blit(bg_img, (0,0))
                pygame.display.update()
            if event.key == pygame.K_SPACE:
                messagebox.showinfo('Shortcut','1 --- First Song\n2 --- Second song\nKey Up --- Pause the music\nKey Down --- Resume The music')

        if event.type == pygame.QUIT:
            runing = False
    pygame.display.update()
pygame.quit()






























## Created By Konory