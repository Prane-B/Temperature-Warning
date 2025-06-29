import psutil
import pygame
from time import sleep

all_temps = []
run = True
while run:
    temps = psutil.sensors_temperatures()
    if not temps:
        print("No temperature sensors found.")
    else:
        for entries in temps.values():
            for entry in entries:
                all_temps.append(entry.current)
        if all_temps:
            avg_temp = sum(all_temps) / len(all_temps)
            if avg_temp > 90:
                run = False
            sleep(5)
            print(avg_temp)
        else:
            print("No temperature readings available.")
pygame.init()
screen = pygame.display.set_mode((1000,1000))
img = pygame.image.load("images.png")
bigimg = pygame.transform.scale(img,(1000,1000))
while True:
    screen.blit(bigimg,(0,0))
    pygame.display.flip()
