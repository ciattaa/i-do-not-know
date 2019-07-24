# -*- coding: utf-8 -*-




#import modules
 
import pygame

import random

import time


def draw_apple(apple_X,apple_Y):
    pygame.draw.rect(display, player_color, pygame.Rect(apple_X, apple_Y,10,10))
def generate_apple():
    apple_X= random.randint(1,50) *10
    apple_Y= random.randint(1,50) *10
    return apple_X, apple_Y
def collision_with_apple(snake_head, apple_X, apple_Y,grow): 
    if snake_head[0] == apple_X and snake_head[1] ==apple_Y:
        apple_X,apple_Y = generate_apple()
        grow = True
    return apple_X, apple_Y,grow
def collision_with_boundaries(snake_head):

    # if snake is outside of boundaries return 1
    if snake_head[0]>=display_width or snake_head[0] < 0 or snake_head[1]>=display_height or snake_head[1]<0:
        return 1 
    return 0
def collision_with_self(snake_head, snake_position):
    for position in snake_position[1:]:
        if snake_head[0] == position[0] and snake_head[1] == position[1]:
            return 1
        return 0
def generate_snake(snake_head, snake_position, button_direction,grow):
 
    #uses button_direction to decide where snake head will go
    if button_direction ==1:
            snake_head[0] += 10
    elif button_direction ==0:
        snake_head[0] -= 10
    elif button_direction ==2:
        snake_head[1] += 10
    elif button_direction ==3:
        snake_head[1] -= 10
    snake_position.insert(0,list(snake_head))
    if grow != True:
        snake_position.pop()
    return snake_position
            

def display_snake(snake_position):

    #uses list of snake's positions to display snake
    for position in snake_position:
        pygame.draw.rect(display, apple_color, pygame.Rect(position[0], position[1],10,10))

def play_game(snake_head, snake_position, button_direction):

    crashed = False
    grow = False
    apple_X, apple_Y = generate_apple()
    while crashed is not True:

        for event in pygame.event.get():

            #ends game if you click on X
            if event.type == pygame.QUIT:
                crashes = True

            #sets variable used to move snake using arrow keys
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    button_direction = 0
                elif event.key == pygame.K_RIGHT:
                    button_direction = 1
                elif event.key == pygame.K_UP:
                    button_direction = 3
                elif event.key == pygame.K_DOWN:
                    button_direction = 2                    


        #moves snake position
        snake_position = generate_snake(snake_head, snake_position, button_direction, grow)
        grow = False
        

        #display background and snake
        display.fill(window_color)
        display_snake(snake_position)
        draw_apple(apple_X,apple_Y)
        pygame.display.update()
        apple_X, apple_Y, grow = collision_with_apple(snake_head, apple_X, apple_Y, grow)  
       
        #ends game loop if snake leaves the boundary
        if collision_with_boundaries(snake_head) == 1:
            crashed = True
        if collision_with_self(snake_head, snake_position) == 1:
            crashed = True


        clock.tick(20)



if __name__ == "__main__":

    # set variables

    display_width = 500

    display_height = 500

    player_color = (17,0,0)

    window_color = (80,181,139)
    
    apple_color = (201,28,48)

    clock=pygame.time.Clock()

    

    #create the snake

    snake_head = [250,250]

    snake_position = [[250,250],[240,250],[230,250]]



    #initialize pygame modules    

    pygame.init()

    

    #display game window

    display = pygame.display.set_mode((display_width,display_height))

    display.fill(window_color)

    pygame.display.set_caption("Snake Game")

    pygame.display.update()

    

    #start the game loop

    play_game(snake_head, snake_position, 1)



    pygame.quit()