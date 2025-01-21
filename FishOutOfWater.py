import pygame
import random


FishColor = (226, 127, 128)
TreeColor = (71, 48, 11)
BackroundColor = (0, 51, 89)
ScoreColor = (255, 255, 255)
WaterColor = (73, 173, 255)

WindowWidth = 1000
WindowHeight = 500
FishWidth = 35
FishHeight = 25
TreeWidth = 30
TreeGap = 150
TreeSpeed = 3
FishGravity = 0.5
FishJump = -17.5
WaterHight = 50
FPS = 60

pygame.init()
Window = pygame.display.set_mode((WindowWidth, WindowHeight))
pygame.display.set_caption("Fish Out Of Water!")
font = pygame.font.SysFont ("Comic Sans MS", 35)

class fish:
    def __init__ (self):
        self.x = 100
        self.y = WindowHeight / 2
        self.speed = 0
    def Jump (self):
        self.speed = (FishJump)
    def Move (self):
        self.speed = self.speed+FishGravity
        self.y = self.y + self.speed
        if self.y < 0 :
            self.y = 0
        if self.y > WindowHeight - FishHeight:
            self.y = WindowHeight -FishHeight
    def draw (self):
        pygame.draw.rect (Window, FishColor, (self.x, self.y, FishWidth, FishHeight))
class trees:
    def __init__ (self):
        self.x = WindowWidth
        self.height = random.randint (200, 270)
        self.top = self.height
        self.bottom = self.top + TreeGap
    def TreeMove (self):
        self.x = self.x - TreeSpeed
    def TreeDraw (self):
        pygame.draw.rect (Window, TreeColor, (self.x, 0, TreeWidth, self.height))
        pygame.draw.rect (Window, TreeColor, (self.x, self.bottom, TreeWidth, WindowHeight - self.bottom))

def main ():
    global FishGravity
    Window.fill (BackroundColor)
    TitleText = font.render ("Fish Out Of Water!", True, ScoreColor)
    Window.blit (TitleText, (WindowWidth / 2 - TitleText.get_width() / 2, 200))
    StartText = font.render ("Press a button to start", True, FishColor)
    Window.blit (StartText, (WindowWidth/ 2 - StartText.get_width() / 2, 300))
    ButtonPressed = False
    pygame.display.update()
    while not ButtonPressed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                ButtonPressed = True
            if event.type == pygame.QUIT:
                pygame.quit()
                return
    Player = fish()
    TreeList = [trees()]
    Score = 0
    Clock = pygame.time.Clock()

    while ButtonPressed:

        Window.fill (BackroundColor)
        pygame.draw.rect (Window, WaterColor, (0, WindowHeight - WaterHight, WindowWidth, WaterHight))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if Player.y == (WindowHeight - FishHeight):
                        Player.Jump()
                    else:
                        Player.speed = 0
                        FishGravity = 0.1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    FishGravity = 0.5
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        Player.Move()
        for Tree in TreeList: 
            Tree.TreeMove()
            if Tree.x + TreeWidth < 0:
                Score += 1
                TreeList.remove(Tree)
                TreeList.append(trees())
            if Player.x + FishWidth > Tree.x and Player.x < Tree.x + TreeWidth:
                if Player.y < Tree.top or Player.y + FishHeight > Tree.bottom:
                    ButtonPressed = False
        Player.draw ()
        for Tree in TreeList:
            Tree.TreeDraw ()
        ScoreText = font.render(f"{Score}", True, ScoreColor)
        Window.blit(ScoreText, (10, 10))
        pygame.display.update()
        Clock.tick(FPS)
        if (ButtonPressed == False):
            Window.fill (BackroundColor)

            TitleText = font.render ("Game Over!", True, ScoreColor)
            Window.blit (TitleText, (WindowWidth / 2 - TitleText.get_width() / 2, 200))
            StartText = font.render ("Press a button to start", True, FishColor)
            Window.blit (StartText, (WindowWidth/ 2 - StartText.get_width() / 2, 300))
            ButtonPressed = False
            pygame.display.update()
            while not ButtonPressed:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        ButtonPressed = True
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
            Player = fish()
            TreeList = [trees()]
            Score = 0
            Clock = pygame.time.Clock()
main()