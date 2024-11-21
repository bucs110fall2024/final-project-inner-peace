import pygame
class Enemy(pygame.sprite.Sprite):
    def __init__(self, health, mana):
        '''
        create an enemy object
        health(int): starting amount of health of the enemy
        mana(int): starting amount of mana of the enemy
        '''
        pass

    def attack(self, hit):
        '''
        hit(int): attacks the player by a certain amount
        '''
        pass

    def defend(self, shield):
        '''
        shield(int): defend against the player by a certain amount
        '''
        pass
    