#!usr/bin/env python
import pygame,sys
import random,time

#General setup
pygame.init()
clock = pygame.time.Clock()

#Setting up the window
screen_width = 1280
screen_height = 960
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('PongMania')

#pygame.Rect co-ordinates
ball = pygame.Rect(screen_width//2-15,screen_height//2-15,30,30)
player = pygame.Rect(screen_width//2 - 70, screen_height - 20, 140,10)
opponent = pygame.Rect(screen_width//2 - 70, 20, 140,10)

#defining colors
bg_color=pygame.Color('grey12')
light_grey =(200,200,200)
ball_c=['pink','lightgreen','lightblue','lightgreen','pink','lightblue']
ball_color=pygame.Color(ball_c[random.randint(0,5)])
#defining the speed of the ball
ball_speed_y=7*random.choice((-1,1))
ball_speed_x=7*random.choice((1,-1))

#texts
player_score=0
opponent_score=0
player_score1=None
opponent_score1=None

game_font=pygame.font.SysFont('comicsansms',38)

def ball_animation():

    global player_score1,opponent_score1,game_start,ball_speed_x,ball_speed_y,player_score,opponent_score,game_start,countdown,opponent
    #moving the ball
    ball.y+=ball_speed_y
    ball.x+=ball_speed_x

    #bouncing the ball over the screen
        ball_speed_x *= -1
        
    if ball.top<=0 or ball.bottom>=screen_height:
        ball.center=(screen_width//2,screen_height//2)
        player_score1=player_score
        opponent_score1=opponent_score
        player_score=0
        opponent_score=0
        ball_speed_x=0
        ball_speed_y=0
        game_start=1
        pygame.mixer.music.load('over.mp3')
        pygame.mixer.music.play(0)

    #bounce the ball if the ball hits player/opponent and updating the score
    if ball.colliderect(player):
        ball_speed_y*=-1
        player_score+=random.randint(6,7)
        pygame.mixer.music.load('hit.mp3')
        pygame.mixer.music.play(0)
        
    elif ball.colliderect(opponent):
        ball_speed_y*=-1
        opponent_score+=random.randint(6,7)
        pygame.mixer.music.load('hit.mp3')
        pygame.mixer.music.play(0)


def opponent_AI():
    global opponent,ball
    if opponent.x<ball.x and opponent.right<=screen_width:
        opponent.x+=7
    elif opponent.x>ball.x and opponent.left>=0:
        opponent.x-=7

game_start = None
text1=game_font.render("You won!",True,ball_color)
text2=game_font.render("You lost!",True,ball_color)
text3=game_font.render("You drew!",True,ball_color)
#Gameloop
while True:
    #Checking if the user presses the close button using loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #uninitializes the pygame
            sys.exit() #quits the program
    
    #getting the keypresses
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT and player.right<=screen_width:
            player.x+=7
        if event.key==pygame.K_LEFT and player.left>=0:
            player.x-=7
        if event.key==pygame.K_SPACE:
            ball_speed_x=7
            ball_speed_y=7 
            game_start=None

    #opponent AI
    opponent_AI()

    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen, ball_color, ball)
    pygame.draw.line(screen, light_grey, (0,screen_height//2), (screen_width,screen_height//2))
    pygame.draw.circle(screen, light_grey, (screen_width//2,screen_height//2), 200, 1)

    #calling all animation related to the ball
    ball_animation()

    #Scoreboard
    player_text=game_font.render(f"YOU: {player_score}",True,pygame.Color('white'))
    opponent_text=game_font.render(f"BOT: {opponent_score}",True,pygame.Color('white'))
    screen.blit(player_text,(screen_width//2-40,screen_height//2+100))
    screen.blit(opponent_text,(screen_width//2-40,screen_height//2-100))

    end_text1=game_font.render("Press Space to restart",True,ball_color)
    end_text2=game_font.render("Developed by Abhinandan Shrestha",True,ball_color)

    if game_start:
        screen.blit(end_text1,(screen_width//2-130,screen_height//2-130))
        screen.blit(end_text2,(screen_width//2-210,screen_height-80))
        if player_score1>opponent_score1:
            screen.blit(text1,(screen_width//2-55,screen_height//2-170))
        elif player_score1<opponent_score1:
            screen.blit(text2,(screen_width//2-55,screen_height//2-170))
        else:
            screen.blit(text3,(screen_width//2-55,screen_height//2-170))

    #updating the window/screen
    pygame.display.flip()
    clock.tick(60)



