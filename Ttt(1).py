##Ttt.py
#June 18 2020
#Arya Peer
#Draws a tic tac toe grid that closes after 5 seconds

#import and Initialize
import pygame
import sys
pygame.init()

#import fonts
font1 = pygame.font.SysFont("Times New Roman", 70)
font2 = pygame.font.SysFont("Times New Roman", 30)
font3= pygame.font.SysFont("Times New Roman", 20)

#set running as true to allow quit to function
running = True

#ensure no overlap - box 1,2,3,4,5,6,7,8,9 counted from left to right and top to bottom
b1=0
b2=0
b3=0
b4=0
b5=0
b6=0
b7=0
b8=0
b9=0

#make a display 
WIDTH = 300
HEIGHT = 350
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

#declare constant colors
RED = (255, 0, 0)
GREEN =(0, 255, 0)
BLUE =( 0, 0,255 )
CYAN =(0, 255, 255)
WHITE =(255, 255, 255)
BLACK =(0, 0, 0)
GREY = (128, 128, 128)

#label the window
pygame.display.set_caption("Ttt.py")

#title
gameWindow.fill(BLUE)
graphics = font2.render("TicTacToe.PY", 0, WHITE)
gameWindow.blit(graphics, (75, 220) ) 

#draw house
#house and door
pygame.draw.rect(gameWindow, WHITE, (100, 100, 50, 50), 1)
pygame.draw.rect(gameWindow, WHITE, (125, 125, 10, 25), 1)

#roof
pygame.draw.line(gameWindow, WHITE,(100, 100), (125,75), 1)
pygame.draw.line(gameWindow, WHITE,(150, 100), (125,75), 1)

#window
pygame.draw.rect(gameWindow, WHITE, (120, 120, -15, 15), 1)
pygame.draw.line(gameWindow, WHITE,(120, 127), (105,127), 1)
pygame.draw.line(gameWindow, WHITE,(112, 135), (112,120), 1)

#update display
pygame.display.update()
pygame.time.delay(2000) 

#clear title and show controls for player 1/O)
gameWindow.fill(WHITE)
playerIntro1 = font3.render("This game's controls for Player 1/O:", 0, BLACK)
gameWindow.blit(playerIntro1, (0, 300) )

#draw the intesecting lines
pygame.draw.line(gameWindow, BLACK,(100, 0), (100,300), 1)
pygame.draw.line(gameWindow, BLACK,(200, 0), (200,300), 1)
pygame.draw.line(gameWindow, BLACK,(0, 100), (300,100), 1)
pygame.draw.line(gameWindow, BLACK,(0, 200), (300,200), 1)

#The Locations and which key you need to hit to place your symbol in this location
topLeftIntro1 = font1.render("q", 0, BLACK) #top left
gameWindow.blit(topLeftIntro1, (25, 15) ) 

topMidIntro1 = font1.render("w", 0, BLACK) #top middle
gameWindow.blit(topMidIntro1, (125, 15) )

topRightIntro1 = font1.render("e", 0, BLACK)#top right
gameWindow.blit(topRightIntro1, (225, 15) ) 

leftCenterIntro1 = font1.render("a", 0, BLACK) # left of center
gameWindow.blit(leftCenterIntro1, (25, 115) )

trueCenterIntro1 = font1.render("s", 0, BLACK) # true center
gameWindow.blit(trueCenterIntro1, (125, 115) )

rightCenterIntro1 = font1.render("d", 0, BLACK) #right of center
gameWindow.blit(rightCenterIntro1, (225, 115) ) 

botLeftIntro1 = font1.render("z", 0, BLACK) #bottom left
gameWindow.blit(botLeftIntro1, (25, 215) )

botMidIntro1 = font1.render("x", 0, BLACK) # bottom middle
gameWindow.blit(botMidIntro1, (125, 215) ) 

botRightIntro1 = font1.render("c", 0, BLACK) #bottom right
gameWindow.blit(botRightIntro1, (225, 215) )

#update display
pygame.display.update()
pygame.time.delay(10000) #pause at this menu for 5 seconds

#Clear instructions for player 1 and show instructions for player 2
gameWindow.fill(WHITE)
playerIntro1 = font3.render("This game's controls for Player 2/X:", 0, BLACK)
gameWindow.blit(playerIntro1, (0, 300) )

#draw intersecting ttt lines 
pygame.draw.line(gameWindow, BLACK,(100, 0), (100,300), 1)
pygame.draw.line(gameWindow, BLACK,(200, 0), (200,300), 1)

pygame.draw.line(gameWindow, BLACK,(0, 100), (300,100), 1)
pygame.draw.line(gameWindow, BLACK,(0, 200), (300,200), 1)

#The Locations and which key you need to hit to place your symbol in this location:
topLeftIntro2 = font1.render("t", 0, BLACK)#Top left
gameWindow.blit(topLeftIntro2, (25, 15) ) 

topMidIntro2 = font1.render("y", 0, BLACK) # top middle
gameWindow.blit(topMidIntro2, (125, 15) )

topRightIntro2 = font1.render("u", 0, BLACK) # top right
gameWindow.blit(topRightIntro2, (225, 15) ) 

leftCenterIntro2 = font1.render("g", 0, BLACK) #left of center
gameWindow.blit(leftCenterIntro2, (25, 115) )

trueCenterIntro2 = font1.render("h", 0, BLACK) # true center
gameWindow.blit(trueCenterIntro2, (125, 115) )

rightCenterIntro2 = font1.render("j", 0, BLACK) #right of center
gameWindow.blit(rightCenterIntro2, (225, 115) ) 

botLeftIntro2 = font1.render("b", 0, BLACK)#bottom left
gameWindow.blit(botLeftIntro2, (25, 215) )

botMidIntro2 = font1.render("n", 0, BLACK)#bottom mid
gameWindow.blit(botMidIntro2, (125, 215) ) 

botRightIntro2 = font1.render("m", 0, BLACK)#bottom right
gameWindow.blit(botRightIntro2, (225, 215) )

pygame.display.update()
pygame.time.delay(10000) 


#CLEAR EVERYTHING AND START THE GAME
gameWindow.fill(WHITE)
#draw vertical ttt lines
pygame.draw.line(gameWindow, BLACK,(100, 0), (100,300), 1)
pygame.draw.line(gameWindow, BLACK,(200, 0), (200,300), 1)

#draw horizontal ttt lines
pygame.draw.line(gameWindow, BLACK,(0, 100), (300,100), 1)
pygame.draw.line(gameWindow, BLACK,(0, 200), (300,200), 1)

#update the display to show the tic tac toe board
pygame.display.update()

while running:
    #calculate total value and check if it is divisible by 7 so that we can ensure that people don't place more than one of their symbols per turn
    totalValue=b1+b2+b3+b4+b5+b6+b7+b8+b9
    totalValueModSeven=totalValue%7

    #look for events happening in the pygame
    for event in pygame.event.get():
        #look for quit (pressing the x at top right)
        if event.type == pygame.QUIT:
            gameWindow.fill(BLUE)
            exitPrompt = font2.render("GOODBYE", 0, WHITE) #define what to display
            gameWindow.blit(exitPrompt, (75, 120) ) # display in centre of window
            pygame.display.update()
            pygame.time.delay(2000) 
            running = False
            pygame.quit()
        #look for key presses
        if event.type == pygame.KEYDOWN:
            #if q is pressed and box 1 does not have anything within it place the o
            if event.key == pygame.K_q and b1 ==0 and (totalValueModSeven== 0 or totalValue == 0):
                topLeft = font1.render("O", 0, BLACK)
                gameWindow.blit(topLeft, (25, 15) ) 
                pygame.display.update()
                pygame.time.delay(1500)
                b1 = 5
            #else if w is pressed and box 2 does not have anything within it place the o
            elif event.key == pygame.K_w and b2==0 and (totalValueModSeven== 0 or totalValue == 0) :
                topMid = font1.render("O", 0, BLACK)
                gameWindow.blit(topMid, (125, 15) ) 
                pygame.display.update()
                pygame.time.delay(1500) 
                b2=5
            #else if e is pressed and box 3 does not have anything within it place the o
            elif event.key == pygame.K_e and b3==0 and (totalValueModSeven== 0 or totalValue == 0) :
                topRight = font1.render("O", 0, BLACK)
                gameWindow.blit(topRight, (225, 15) ) 
                pygame.display.update()
                pygame.time.delay(1500)
                b3=5
            #else if a is pressed and box 4 does not have anything within it place the o
            elif event.key == pygame.K_a and b4==0 and (totalValueModSeven== 0 or totalValue == 0):
                leftCenter = font1.render("O", 0, BLACK)
                gameWindow.blit(leftCenter, (25, 115) )
                pygame.display.update()
                pygame.time.delay(1500)
                b4=5
            #else if s is pressed and box 5 does not have anything within it place the o
            elif event.key == pygame.K_s and b5==0 and (totalValueModSeven== 0 or totalValue == 0):
                trueCenter = font1.render("O", 0, BLACK)
                gameWindow.blit(trueCenter, (125, 115) )
                pygame.display.update()
                pygame.time.delay(1500)
                b5=5
            #else if d is pressed and box 6 does not have anything within it place the o
            elif event.key == pygame.K_d and b6==0 and (totalValueModSeven== 0 or totalValue == 0):
                rightCenter = font1.render("O", 0, BLACK)
                gameWindow.blit(rightCenter, (225, 115) ) 
                pygame.display.update()
                pygame.time.delay(1500)
                b6=5
            #else if z is pressed and box 7 does not have anything within it place the o
            elif event.key == pygame.K_z and b7==0 and (totalValueModSeven== 0 or totalValue == 0):
                botLeft = font1.render("O", 0, BLACK)
                gameWindow.blit(botLeft, (25, 215) ) 
                pygame.display.update()
                pygame.time.delay(1500)
                b7=5
            #else if x is pressed and box 8 does not have anything within it place the o
            elif event.key == pygame.K_x and b8==0 and (totalValueModSeven== 0 or totalValue == 0):
                botMid = font1.render("O", 0, BLACK)
                gameWindow.blit(botMid, (125, 215) ) 
                pygame.display.update()
                pygame.time.delay(1500)
                b8=5
            #else if c is pressed and box 9 does not have anything within it place the o
            elif event.key == pygame.K_c and b9==0 and (totalValueModSeven== 0 or totalValue == 0):
                botRight = font1.render("O", 0, BLACK)
                gameWindow.blit(botRight, (225, 215) ) 
                pygame.display.update()
                pygame.time.delay(1500)
                b9=5

            #right hand side X player
            #else if t is pressed and box 1 does not have anything within it place the x 
            elif event.key == pygame.K_t and b1==0 and totalValueModSeven !=0:
                topLeft = font1.render("X", 0, BLACK)
                gameWindow.blit(topLeft, (25, 15) ) 
                pygame.display.update()
                pygame.time.delay(1500)
                b1=2
            #else if y is pressed and box 2 does not have anything within it place the x 
            elif event.key == pygame.K_y and b2==0 and totalValueModSeven !=0:
                topMid = font1.render("X", 0, BLACK)
                gameWindow.blit(topMid, (125, 15) ) 
                pygame.display.update()
                pygame.time.delay(1500) 
                b2=2
            #else if u is pressed and box 3 does not have anything within it place the x
            elif event.key == pygame.K_u and b3==0 and totalValueModSeven !=0:
                topRight = font1.render("X", 0, BLACK)
                gameWindow.blit(topRight, (225, 15) ) 
                pygame.display.update()
                pygame.time.delay(1500)
                b3=2
            #else if g is pressed and box 4 does not have anything within it place the x
            elif event.key == pygame.K_g and b4==0 and totalValueModSeven !=0:
                leftCenter = font1.render("X", 0, BLACK)
                gameWindow.blit(leftCenter, (25, 115) )
                pygame.display.update()
                pygame.time.delay(1500)
                b4=2
            #else if h is pressed and box 5 does not have anything within it place the x
            elif event.key == pygame.K_h and b5==0 and totalValueModSeven !=0:
                trueCenter = font1.render("X", 0, BLACK)
                gameWindow.blit(trueCenter, (125, 115) )
                pygame.display.update()
                pygame.time.delay(1500)
                b5=2
            #else if j is pressed and box 6 does not have anything within it place the x
            elif event.key == pygame.K_j and b6==0 and totalValueModSeven !=0:
                rightCenter = font1.render("X", 0, BLACK)
                gameWindow.blit(rightCenter, (225, 115) ) 
                pygame.display.update()
                pygame.time.delay(1500)
                b6=2
            #else if b is pressed and box 7 does not have anything within it place the x
            elif event.key == pygame.K_b and b7==0 and totalValueModSeven !=0:
                botLeft = font1.render("X", 0, BLACK)
                gameWindow.blit(botLeft, (25, 215) ) 
                pygame.display.update()
                pygame.time.delay(1500)
                b7=2
            #else if n is pressed and box 8 does not have anything within it place the x
            elif event.key == pygame.K_n and b8==0 and totalValueModSeven !=0:
                botMid = font1.render("X", 0, BLACK)
                gameWindow.blit(botMid, (125, 215) ) 
                pygame.display.update()
                pygame.time.delay(1500)
                b8=2
            #else if m is pressed and box 9 does not have anything within it place the x
            elif event.key == pygame.K_m and b9==0 and totalValueModSeven !=0:
                botRight = font1.render("X", 0, BLACK)
                gameWindow.blit(botRight, (225, 215) ) 
                pygame.display.update()
                pygame.time.delay(1500)
                b9=2
            #else if p is pressed restart the loop
            elif event.key == pygame.K_p:
                gameWindow.fill(WHITE)
                restart = font2.render("Tic Tac Toe", 0, BLACK) #define what to display
                gameWindow.blit(restart, (75, 120) ) # display in centre of window
                pygame.display.update()
                pygame.time.delay(2000)
                #fill the window
                gameWindow.fill(WHITE)
                #draw vertical lines
                pygame.draw.line(gameWindow, BLACK,(100, 0), (100,300), 1)
                pygame.draw.line(gameWindow, BLACK,(200, 0), (200,300), 1)

                #draw horizontal lines
                pygame.draw.line(gameWindow, BLACK,(0, 100), (300,100), 1)
                pygame.draw.line(gameWindow, BLACK,(0, 200), (300,200), 1)
                #update the display to show the tic tac toe board
                pygame.display.update()
                b1=0
                b2=0
                b3=0
                b4=0
                b5=0
                b6=0
                b7=0
                b8=0
                b9=0
            #end if 
        #end if
            
            #check if player 2 has won by checking if any rows, columns or diagonals have a sum of 6 as every box with an x is it has a value of 2 and when you add them together you get six
            if b1+b2+b3 == 6:#top row  = 6 which means only x's in this area which means that player 2 won
                gameWindow.fill(WHITE)
                graphics = font2.render("X/Player 2 Won", 0, BLACK) #define what to display
                gameWindow.blit(graphics, (0, 120) ) # display in centre of window
                graphics2 = font2.render("Press P to Play again", 0, BLACK) #define what to display
                gameWindow.blit(graphics2, (0, 170) )
                graphics3 = font3.render("Press x at top right to leave", 0, BLACK) #define what to display
                gameWindow.blit(graphics3, (0, 270 ) )
                pygame.display.update()
                pygame.time.delay(2000)
            elif b4+b5+b6 == 6:#middle row = 6 which means only x's in this area which means that player 2 won
                gameWindow.fill(WHITE)
                graphics = font2.render("X/Player 2 Won", 0, BLACK) #define what to display
                gameWindow.blit(graphics, (0, 120) ) # display in centre of window
                graphics2 = font2.render("Press P to Play again", 0, BLACK) #define what to display
                gameWindow.blit(graphics2, (0, 170) )
                graphics3 = font3.render("Press x at top right to leave", 0, BLACK) #define what to display
                gameWindow.blit(graphics3, (0, 270 ) )
                pygame.display.update()
                pygame.time.delay(2000)
            elif b7+b8+b9 == 6:#bottom row = 6 which means only x's in this area which means that player 2 won
                gameWindow.fill(WHITE)
                graphics = font2.render("X/Player 2 Won", 0, BLACK) #define what to display
                gameWindow.blit(graphics, (0, 120) ) # display in centre of window
                graphics2 = font2.render("Press P to Play again", 0, BLACK) #define what to display
                gameWindow.blit(graphics2, (0, 170) )
                graphics3 = font3.render("Press x at top right to leave", 0, BLACK) #define what to display
                gameWindow.blit(graphics3, (0, 270 ) )
                pygame.display.update()
                pygame.time.delay(2000)
            elif b1+b4+b7 == 6:#Left Collumn = 6 which means only x's in this area which means that player 2 won
                gameWindow.fill(WHITE)
                graphics = font2.render("X/Player 2 Won", 0, BLACK) #define what to display
                gameWindow.blit(graphics, (0, 120) ) # display in centre of window
                graphics2 = font2.render("Press P to Play again", 0, BLACK) #define what to display
                gameWindow.blit(graphics2, (0, 170) )
                graphics3 = font3.render("Press x at top right to leave", 0, BLACK) #define what to display
                gameWindow.blit(graphics3, (0, 270 ) )
                pygame.display.update()
                pygame.time.delay(2000)
            elif b2 + b5 + b8 == 6:#central collumn = 6 which means only x's in this area which means that player 2 won
                gameWindow.fill(WHITE)
                graphics = font2.render("X/Player 2 Won", 0, BLACK) #define what to display
                gameWindow.blit(graphics, (0, 120) ) # display in centre of window
                graphics2 = font2.render("Press P to Play again", 0, BLACK) #define what to display
                gameWindow.blit(graphics2, (0, 170) )
                graphics3 = font3.render("Press x at top right to leave", 0, BLACK) #define what to display
                gameWindow.blit(graphics3, (0, 270 ) )
                pygame.display.update()
                pygame.time.delay(2000)
            elif b3 + b6 + b9 == 6:#right collumn = 6 which means only x's in this area which means that player 2 won
                gameWindow.fill(WHITE)
                graphics = font2.render("X/Player 2 Won", 0, BLACK) #define what to display
                gameWindow.blit(graphics, (0, 120) ) # display in centre of window
                graphics2 = font2.render("Press P to Play again", 0, BLACK) #define what to display
                gameWindow.blit(graphics2, (0, 170) )
                graphics3 = font3.render("Press x at top right to leave", 0, BLACK) #define what to display
                gameWindow.blit(graphics3, (0, 270 ) )
                pygame.display.update()
                pygame.time.delay(2000)
            elif b1+b5+b9 == 6:#left to right diagonal = 6 which means only x's in this area which means that player 2 won
                gameWindow.fill(WHITE)
                graphics = font2.render("X/Player 2 Won", 0, BLACK) #define what to display
                gameWindow.blit(graphics, (0, 120) ) # display in centre of window
                graphics2 = font2.render("Press P to Play again", 0, BLACK) #define what to display
                gameWindow.blit(graphics2, (0, 170) )
                graphics3 = font3.render("Press x at top right to leave", 0, BLACK) #define what to display
                gameWindow.blit(graphics3, (0, 270 ) )
                pygame.display.update()
                pygame.time.delay(2000)
            elif b3+b5+b7 ==6:#right to left diagonal = 6 which means only x's in this area which means that player 2 won
                gameWindow.fill(WHITE)
                graphics = font2.render("X/Player 2 Won", 0, BLACK) #define what to display
                gameWindow.blit(graphics, (0, 120) ) # display in centre of window
                graphics2 = font2.render("Press P to Play again", 0, BLACK) #define what to display
                gameWindow.blit(graphics2, (0, 170) )
                graphics3 = font3.render("Press x at top right to leave", 0, BLACK) #define what to display
                gameWindow.blit(graphics3, (0, 270 ) )
                pygame.display.update()
                pygame.time.delay(2000)
            
            #check if player 1 has won each box of player 1 is worth 5 so that means that if he has three in a row they are worth 15 and that is what we are checking for
            elif b1+b2+b3 == 15: #O/player 1 winning messages # top row = 15 which means only o's in this area and player one won
                gameWindow.fill(WHITE)
                graphics = font2.render("O/Player 1 Won", 0, BLACK) #define what to display
                gameWindow.blit(graphics, (0, 120) ) # display in centre of window
                graphics2 = font2.render("Press P to Play again", 0, BLACK) #define what to display
                gameWindow.blit(graphics2, (0, 170) )
                graphics3 = font3.render("Press x at top right to leave", 0, BLACK) #define what to display
                gameWindow.blit(graphics3, (0, 270 ) )
                pygame.display.update()
                pygame.time.delay(2000)
            elif b4+b5+b6 == 15:# middle row = 15 which means only o's in this area and player one won
                gameWindow.fill(WHITE)
                graphics = font2.render("O/Player 1 Won", 0, BLACK) #define what to display
                gameWindow.blit(graphics, (0, 120) ) # display in centre of window
                graphics2 = font2.render("Press P to Play again", 0, BLACK) #define what to display
                gameWindow.blit(graphics2, (0, 170) )
                graphics3 = font3.render("Press x at top right to leave", 0, BLACK) #define what to display
                gameWindow.blit(graphics3, (0, 270 ) )
                pygame.display.update()
                pygame.time.delay(2000)
            elif b7+b8+b9 == 15:#bottom row = 15 which means only o's in this area and player one won
                gameWindow.fill(WHITE)
                graphics = font2.render("O/Player 1 Won", 0, BLACK) #define what to display
                gameWindow.blit(graphics, (0, 120) ) # display in centre of window
                graphics2 = font2.render("Press P to Play again", 0, BLACK) #define what to display
                gameWindow.blit(graphics2, (0, 170) )
                graphics3 = font3.render("Press x at top right to leave", 0, BLACK) #define what to display
                gameWindow.blit(graphics3, (0, 270 ) )
                pygame.display.update()
                pygame.time.delay(2000)
            elif b1+b4+b7 == 15:#left collumn = 15 which means only o's in this area and player one won
                gameWindow.fill(WHITE)
                graphics = font2.render("O/Player 1 Won", 0, BLACK) #define what to display
                gameWindow.blit(graphics, (0, 120) ) # display in centre of window
                graphics2 = font2.render("Press P to Play again", 0, BLACK) #define what to display
                gameWindow.blit(graphics2, (0, 170) )
                graphics3 = font3.render("Press x at top right to leave", 0, BLACK) #define what to display
                gameWindow.blit(graphics3, (0, 270 ) )
                pygame.display.update()
                pygame.time.delay(2000)
            elif b2 + b5 + b8 == 15:#middle collumn = 15 which means only o's in this area and player one won
                gameWindow.fill(WHITE)
                graphics = font2.render("O/Player 1 Won", 0, BLACK) #define what to display
                gameWindow.blit(graphics, (0, 120) ) # display in centre of window
                graphics2 = font2.render("Press P to Play again", 0, BLACK) #define what to display
                gameWindow.blit(graphics2, (0, 170) )
                graphics3 = font3.render("Press x at top right to leave", 0, BLACK) #define what to display
                gameWindow.blit(graphics3, (0, 270 ) )
                pygame.display.update()
                pygame.time.delay(2000)
            elif b3 + b6 + b9 == 15:#right collumn = 15 which means only o's in this area and player one won
                gameWindow.fill(WHITE)
                graphics = font2.render("O/Player 1 Won", 0, BLACK) #define what to display
                gameWindow.blit(graphics, (0, 120) ) # display in centre of window
                graphics2 = font2.render("Press P to Play again", 0, BLACK) #define what to display
                gameWindow.blit(graphics2, (0, 170) )
                graphics3 = font3.render("Press x at top right to leave", 0, BLACK) #define what to display
                gameWindow.blit(graphics3, (0, 270 ) )
                pygame.display.update()
                pygame.time.delay(2000)
            elif b1+b5+b9 == 15:#left to right collumn = 15 which means only o's in this area and player one won
                gameWindow.fill(WHITE)
                graphics = font2.render("O/Player 1 Won", 0, BLACK) #define what to display
                gameWindow.blit(graphics, (0, 120) ) # display in centre of window
                graphics2 = font2.render("Press P to Play again", 0, BLACK) #define what to display
                gameWindow.blit(graphics2, (0, 170) )
                graphics3 = font3.render("Press x at top right to leave", 0, BLACK) #define what to display
                gameWindow.blit(graphics3, (0, 270 ) )
                pygame.display.update()
                pygame.time.delay(2000)
            elif b3+b5+b7 == 15:#right to left collumn = 15 which means only o's in this area and player one won
                gameWindow.fill(WHITE)
                graphics = font2.render("O/Player 1 Won", 0, BLACK) #define what to display
                gameWindow.blit(graphics, (0, 120) ) # display in centre of window
                graphics2 = font2.render("Press P to Play again", 0, BLACK) #define what to display
                gameWindow.blit(graphics2, (0, 170) )
                graphics3 = font3.render("Press x at top right to leave", 0, BLACK) #define what to display
                gameWindow.blit(graphics3, (0, 270 ) )
                pygame.display.update()
                pygame.time.delay(2000)
            elif b1 != 0 and b2 != 0 and b3 !=0 and b4!=0 and b5!=0 and b6!=0 and b7!=0 and b8!=0 and b9!=0:
                gameWindow.fill(WHITE)
                graphics = font2.render("It was a Tie", 0, BLACK) #define what to display
                gameWindow.blit(graphics, (0, 120) ) # display in centre of window
                graphics2 = font2.render("Press P to Play again", 0, BLACK) #define what to display
                gameWindow.blit(graphics2, (0, 170) )
                graphics3 = font3.render("Press x at top right to leave", 0, BLACK) #define what to display
                gameWindow.blit(graphics3, (0, 270 ) )
                pygame.display.update()
                pygame.time.delay(2000)
            #end if
    #end for
#end while
            
