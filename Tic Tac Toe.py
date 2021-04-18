import pygame
import time

(width, height) = (400, 400)
background_color = (255, 198, 26)
white_color = (255, 255, 255)
black_color =(0, 0, 0)
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Tic Tac Toe")
screen.fill(background_color)
pygame.display.flip()

o_round = False

def round_switch():
    global o_round
    o_round = not o_round

def draw_o(x, y):
    pygame.draw.circle(screen, white_color, (x, y), 40)
    pygame.draw.circle(screen, background_color, (x, y), 30)

def draw_x(x, y):
    pygame.draw.line(screen, white_color, (x-(100/2-15), y-(100/2-15)), (x+(100/2-15), y+(100/2-15)), 15)
    pygame.draw.line(screen, white_color, (x-(100/2-15), y+(100/2-15)), (x+(100/2-15), y-(100/2-15)), 15)

def check_end():
    s = True
    for row in range(3):
        for col in range(3):
            if board[row][col]==0:
                s=False
                break
    if s == True:
        global done
        myimage = pygame.Surface((width, height), pygame.SRCALPHA)
        myimage.fill((0,0,0,200))
        screen.blit(myimage, (0, 0))
        pygame.display.update()
        pygame.font.init()
        myfont=pygame.font.SysFont('Times New Roman', 42)
        textsurface = myfont.render('DRAW', False, (255, 255, 255))
        text_width = myfont.size("DRAW")[0]
        etext_width = myfont.size("The game will restart")[0]
        etextsurface = myfont.render("The game will restart", False, (255, 255, 255))
        screen.blit(etextsurface,(200-(etext_width/2), (height)/2))
        screen.blit(textsurface,(200-(text_width/2), (height)/2-text_width/2))
        pygame.display.update()
        time.sleep(3)
        done=True



def check_for_win():
    if board[0][0]==board[0][1]==board[0][2]!=0:
        return True
    elif board[1][0]==board[1][1]==board[1][2]!=0:
        return True
    elif board[2][0]==board[2][1]==board[2][2]!=0:
        return True
    elif board[0][0]==board[1][0]==board[2][0]!=0:
        return True
    elif board[0][1]==board[1][1]==board[2][1]!=0:
        return True
    elif board[0][2]==board[1][2]==board[2][2]!=0:
        return True
    elif board[0][0]==board[1][1]==board[2][2]!=0:
        return True
    elif board[0][2]==board[1][1]==board[2][0]!=0:
        return True
    else:
        return False

board=[]

def start_game():
    board.clear()
    screen.fill(background_color)
    for x in range(2):
        for y in range(2):
            pygame.draw.line(screen, white_color,((((y+1)*100)*x+50), (((y+1)*100)*abs(x-1)+50)),((400+((y-2)*100)*x-50), (400+((y-2)*100)*abs(x-1)-50)), 5)
    for row in range(3):
        board.append([])
        for col in range(3):
            board[row].append(0)
    pygame.display.update()

def end_game():
    global done
    myimage = pygame.Surface((width, height), pygame.SRCALPHA)
    myimage.fill((0,0,0,200))
    screen.blit(myimage, (0, 0))
    pygame.display.update()
    pygame.font.init()
    myfont=pygame.font.SysFont('Times New Roman', 42)
    if o_round==False:
        textsurface = myfont.render('O WON', False, (255, 255, 255))
        text_width = myfont.size("O won")[0]
    else:
        textsurface = myfont.render('X WON', False, (255, 255, 255))
        text_width = myfont.size("X won")[0]
    
    etext_width = myfont.size("The game will restart")[0]
    etextsurface = myfont.render("The game will restart", False, (255, 255, 255))
    screen.blit(etextsurface,(200-(etext_width/2), (height)/2))
    screen.blit(textsurface,(200-(text_width/2), (height)/2-text_width/2))
    pygame.display.update()
    time.sleep(3)
    done=True
    
    
done=True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif done:
            start_game()
            done=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            col=int((position[0]-50)/(105))
            row=int((position[1]-50)/(105))
            if row>=0 and row<=2 and col>=0 and col<=2:
                if o_round and board[row][col]==0:
                    round_switch()
                    draw_o((col+1)*100, (row+1)*100)
                    board[row][col] = 2
                elif o_round==False and board[row][col]==0:
                    round_switch()
                    draw_x((col+1)*100, (row+1)*100)
                    board[row][col] = 1
                if check_for_win():
                    end_game()
                else:
                    check_end()
                pygame.display.update()
                print("Click ", position, "Grid coordinates: ", row, col, " - ", board[row][col])

