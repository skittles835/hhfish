import pygame
from pygame.locals import *
import sys

pygame.init()
screen_info = pygame.display.Info()

screen_size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()


color = (0, 127, 255)

def main():
  while True:
    clock.tick(60)
    screen.fill(color)
    pygame.display.flip()

if __name__ == '__main__':
  main()