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
TreeGap = 180
TreeSpeed = 3
FishGravity = 0.5
FishJump = -17.5
WaterHight = 50
LevelWinScore = 5
Level = 1
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
        global FishJump 
        if Level >= 4:
            FishJump = -6.5
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
        if Level == 5:
            self.speed = random.randint(1,4)
            pos = random.randint(0,1)
            if pos == 0:
                self.speed = self.speed * -1
            self.height = random.randint (100, 270)
        self.x = WindowWidth
        if Level != 5:
            self.height = random.randint (200, 270)
        self.top = self.height
        self.bottom = self.top + TreeGap
    def TreeMove (self):
        if Level == 5:
            self.height += self.speed
            self.top = self.height
            self.bottom = self.top + TreeGap
            if (self.bottom >= WindowHeight - WaterHight) or (self.top <= WaterHight):
                self.speed = -1 * self.speed
        self.x = self.x - TreeSpeed
    def TreeDraw (self):
        pygame.draw.rect (Window, TreeColor, (self.x, 0, TreeWidth, self.height))
        pygame.draw.rect (Window, TreeColor, (self.x, self.bottom, TreeWidth, WindowHeight - self.bottom))

def main ():
    global Level
    global FishGravity
    global LevelWinScore
    global TreeGap
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
        if LevelWinScore == Score:
            Level+=1
            Score = 0
            Window.fill (BackroundColor)
            if Level < 6:
                TitleText = font.render ("!You Won!", True, ScoreColor)
                Window.blit (TitleText, (WindowWidth / 2 - TitleText.get_width() / 2, 200))
                StartText = font.render ("Press a button to continue", True, FishColor)
                Window.blit (StartText, (WindowWidth/ 2 - StartText.get_width() / 2, 300))
            else:
                TitleText = font.render ("!You have ofishally Won!", True, ScoreColor)
                Window.blit (TitleText, (WindowWidth / 2 - TitleText.get_width() / 2, 200))
                StartText = font.render ("Press a button to touch grass", True, FishColor)
                Window.blit (StartText, (WindowWidth/ 2 - StartText.get_width() / 2, 300))
            ButtonPressed = False
            if Level == 2:
                TitleText = font.render ("This water is salty, and you dont like salty water", True, ScoreColor)
                Window.blit (TitleText, (WindowWidth / 2 - TitleText.get_width() / 2, 250))
            if Level == 3:
                TreeGap = 100
                TitleText = font.render ("You start to believe you can fly", True, ScoreColor)
                Window.blit (TitleText, (WindowWidth / 2 - TitleText.get_width() / 2, 250))
            else:
                TreeGap = 180
            if Level == 4:
                TreeGap = 150
                TitleText = font.render ("You feel like a flapy fish", True, ScoreColor)
                Window.blit (TitleText, (WindowWidth / 2 - TitleText.get_width() / 2, 250))
            if Level == 5:
                TreeGap = 150
                TitleText = font.render ("The trees start celebrating!", True, ScoreColor)
                Window.blit (TitleText, (WindowWidth / 2 - TitleText.get_width() / 2, 250))
            pygame.display.update()
            while not ButtonPressed:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        ButtonPressed = True
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
        if Level == 6:
            pygame.quit()
            return
        Window.fill (BackroundColor)
        pygame.draw.rect (Window, WaterColor, (0, WindowHeight - WaterHight, WindowWidth, WaterHight))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if (Level != 4) and (Level != 5):
                        if Player.y == (WindowHeight - FishHeight):
                            Player.Jump()
                        else:
                            Player.speed = 0
                            if Level != 3:
                                FishGravity = 0.05
                            else:
                                FishGravity = 0
                    else:
                        Player.Jump()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    FishGravity = 0.5
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        if Level == 2:
            if Player.y + FishHeight >= WindowHeight - WaterHight:
                Player.Jump()

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