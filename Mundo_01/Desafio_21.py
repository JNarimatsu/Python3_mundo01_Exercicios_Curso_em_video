#Tocando um mp3
import pygame
import os

# Verifique o diretório de trabalho
print(os.getcwd())

# Inicialize o mixer do Pygame
pygame.mixer.init()

# Carregue a música
pygame.mixer.music.load("exe21.mp3")  # ajuste o caminho se necessário
pygame.mixer.music.play()

# Execute um loop ou aguarde a música tocar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)


