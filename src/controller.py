import pygame
from src.player import Player
from src.enemy import Enemy
class Controller:
  def __init__(self):
    #setup pygame data
    pygame.init()
    pygame.event.pump()
    
  def mainloop(self):
    while True:
      
      #Event Loop
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               exit()
      
      #Updates
      
      #Redraw

      #Display
    
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
      
      #event loop

      #update data

      #redraw
      pass
  def gameloop(self):
      #event loop

      #update data

      #redraw
      pass
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
      pass
