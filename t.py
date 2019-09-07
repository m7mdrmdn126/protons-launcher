from tkinter import *
import pygame
import random
import math
import tkinter as tk
from tkinter import messagebox
import turtle
import os
import random as r
import time as tm


        

root=Tk()

def about():

    tk = Tk()
    tk.title("About us")
    tk.geometry("500x500")
     tk.configure(background="#A9C6D9")


    lbl= Label(tk, text="\n Protons launcher \n \n" ,  bg = "#A9C6D9", fg="white", font=("Calibri (Body)", 25))
    lbl.grid(row=0, column = 0)



    lbl2= Label(tk, text="Protons Launcher Is a Program that run Games",  bg = "#A9C6D9", fg="black", font=("Andalus", 10))
    lbl2.grid(row=1, column = 0)

    lbl3= Label(tk, text="1-Zombie:  It’s a Game Which You Try To Fight the Zombies and Kill them" ,  bg = "#A9C6D9", fg="black", font=("Andalus", 10))
    lbl3.grid(row=2, column = 0)

    lbl4= Label(tk, text="2-Tic-tac-toe:…….U already know it " ,  bg = "#A9C6D9", fg="black", font=("Andalus", 10))
    lbl4.grid(row=3, column = 0)

    lbl5= Label(tk, text="3-pong:It’s a multi-player pong game" ,  bg = "#A9C6D9", fg="black", font=("Andalus", 10))
    lbl5.grid(row=4, column = 0)

    lbl6= Label(tk, text="4-Snake:It’s…….Snake" ,  bg = "#A9C6D9", fg="black", font=("Andalus", 10))
    lbl6.grid(row=5, column = 0)

    lbl7= Label(tk, text="WE Hope U Love Our Project That we Made With A lot of Passion And Truly Hardwork " ,  bg = "#A9C6D9", fg="black", font=("Andalus", 10))
    lbl7.grid(row=6, column = 0)




    tk.mainloop ()


def click():
    win = Tk()
    win.title("final project")
    win.geometry('500x500')
    win.configure(background="#A9C6D9")
    
    
    

    
    
    def pong2():
    
        wn = turtle.Screen()
        wn.title("Pong")
        wn.bgcolor("black")
        wn.setup(width=800, height=600)
        wn.tracer(0)

        # Score
        score_a = 0
        score_b = 0

        # Paddle A
        paddle_a = turtle.Turtle()
        paddle_a.speed(0)
        paddle_a.shape("square")
        paddle_a.color("white")
        paddle_a.shapesize(stretch_wid=5,stretch_len=1)
        paddle_a.penup()
        paddle_a.goto(-350, 0)

        # Paddle B
        paddle_b = turtle.Turtle()
        paddle_b.speed(0)
        paddle_b.shape("square")
        paddle_b.color("white")
        paddle_b.shapesize(stretch_wid=5,stretch_len=1)
        paddle_b.penup()
        paddle_b.goto(350, 0)

        # Ball
        ball = turtle.Turtle()
        ball.speed('slow')
        ball.shape("circle")
        ball.color("white")
        ball.penup()
        ball.goto(0, 0)
        ball.dx = 2
        ball.dy = 2

        # Pen
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


        # Functions
        def paddle_a_up():
            y = paddle_a.ycor()
            y += 20
            paddle_a.sety(y)

        def paddle_a_down():
            y = paddle_a.ycor()
            y -= 20
            paddle_a.sety(y)

        def paddle_b_up():
            y = paddle_b.ycor()
            y += 20
            paddle_b.sety(y)

        def paddle_b_down():
            y = paddle_b.ycor()
            y -= 20
            paddle_b.sety(y)

        # Keyboard bindings
        wn.listen()
        wn.onkeypress(paddle_a_up, "w")
        wn.onkeypress(paddle_a_down, "s")
        wn.onkeypress(paddle_b_up, "Up")
        wn.onkeypress(paddle_b_down, "Down")

        # Main game loop
        while True:
            wn.update()
            
            # Move the ball
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            # Border checking

            # Top and bottom
            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy *= -1
        #        os.system("afplay bounce.wav&")
            
            elif ball.ycor() < -290:
                ball.sety(-290)
                ball.dy *= -1
        #        os.system("afplay bounce.wav&")

            # Left and right
            if ball.xcor() > 350:
                score_a += 1
                pen.clear()
                pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                ball.goto(0, 0)
                ball.dx *= -1
            elif score_b == 10:
                tk = Tk()
                tk.title("score")
                tk.geometry("100x100")
                lbl= Label(tk, text="Player B win" , fg="red", font=("Jokerman", 10))
                lbl.grid(row=0, column = 1)
                btn=Button(tk, text= "Exit", fg="red" ,font=("Niagara Engraved", 15))
                btn.grid(row=1, column = 0)
                btn=Button(tk, text= "Try again", fg="black" ,font=("Niagara Engraved", 15))
                btn.grid(row=1, column = 1)
                tk.mainloop ()
                
            elif ball.xcor() < -350:
                score_b += 1
                pen.clear()
                pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                ball.goto(0, 0)
                ball.dx *= -1
                
            elif score_a == 10 :
                tk = Tk()
                tk.title("score")
                tk.geometry("100x100")
                lbl= Label(tk, text="Player A win" , fg="red", font=("Jokerman", 10))
                lbl.grid(row=0, column = 1)
                btn=Button(tk, text= "Exit", fg="red" ,font=("Niagara Engraved", 15))
                btn.grid(row=1, column = 0)
                btn=Button(tk, text= "Try again", fg="black" ,font=("Niagara Engraved", 15))
                btn.grid(row=1, column = 1) 
                tk.mainloop ()

            # Paddle and ball collisions
            if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
                ball.dx *= -1 
        #        os.system("afplay bounce.wav&")
            
            elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:                 
                ball.dx *= -1
        #        os.system("afplay bounce.wav&")

    
    
    
    
    
    
    
    
        
    def zombie():
        # - ieee protons'19 -
        # -- zombies -- 

        # - importing pygame library -
        import pygame

        pygame.init()
        pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
            

        # -- creating pygame window --
        win = pygame.display.set_mode((500,480))
        pygame.display.set_caption("first game")


        # --- global varibles ---


          # ---man charactar images---

        walkRight = [pygame.image.load('p/R1.png'), pygame.image.load('p/R2.png'), pygame.image.load('p/R3.png'), pygame.image.load('p/R4.png'), pygame.image.load('p/R5.png'), pygame.image.load('p/R6.png'), pygame.image.load('p/R7.png'), pygame.image.load('p/R8.png'), pygame.image.load('p/R9.png')]
        walkLeft = [pygame.image.load('p/L1.png'), pygame.image.load('p/L2.png'), pygame.image.load('p/L3.png'), pygame.image.load('p/L4.png'), pygame.image.load('p/L5.png'), pygame.image.load('p/L6.png'), pygame.image.load('p/L7.png'), pygame.image.load('p/L8.png'), pygame.image.load('p/L9.png')]
        char = pygame.image.load('p/standing.png')


          # -- game background --
        bg = pygame.image.load('p/bg.jpg')


        clock =pygame.time.Clock() #  that' atime clock for frame rate of the vedio game


         # -- game sounds --
        bulletsound = pygame.mixer.Sound('s/bullet.wav')
        hitsound = pygame.mixer.Sound('s/hit.wav')

         # -- back ground music
        music = pygame.mixer.music.load('s/music.mp3')
        pygame.mixer.music.play(-1)

         # -- score --
        score = 0

        #   the player class for our charcter 
        class player(object):
            def __init__(self, x, y, width,height): 
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.vel = 5
                self.isjump = False
                self.jcount = 10
                self.left= False
                self.right= False
                self.walkc = 0
                self.standing = True
                self.hitbox = (self.x + 17, self.y + 11, 29, 52)
            
            def draw(self,win):  
                if self.walkc +1 >= 27:
                    self.walkc= 0
                if not(self.standing):
                    if self.left:
                        win.blit(walkLeft[self.walkc//3], (self.x,self.y))
                        self.walkc+=1
                    elif man.right:
                        win.blit(walkRight[self.walkc//3], (self.x,self.y))
                        self.walkc+=1
                else:
                    if self.right:
                        win.blit(walkRight[0], (self.x, self.y))
                    else:
                        win.blit(walkLeft[0], (self.x, self.y))
                self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)         we don't want that more 


            def hit (self):
                self.isjump = False
                self.jcount = 10
                self.x = 60
                self.y = 410
                self.walkc = 0
                font1 = pygame.font.SysFont("comicsans", 100)
                text = font1.render("-5", 1 ,(255,0,0))
                win.blit(text, (250 - (text.get_width()/2), 200))
                pygame.display.update()
                i = 0
                while i < 300:
                    pygame.time.delay(10)
                    i += 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT :
                            i = 301
                            pygame.quit()

         # projectiles class
        class projectile(object):
            def __init__(self, x, y, redius, color, facing):
                self.x = x
                self.y = y
                self.redius = redius
                self.color = color
                self.facing = facing
                self.vel = 8 * facing
                
                
            def draw(self,win):
                pygame.draw.circle(win, self.color, (self.x, self.y), self.redius)
                
            
                            
        #  enemy character class

        class enemy(object): 
            walkRight = [pygame.image.load('p/R1E.png'), pygame.image.load('p/R2E.png'), pygame.image.load('p/R3E.png'), pygame.image.load('p\R4E.png'), pygame.image.load('p/R5E.png'), pygame.image.load('p/R6E.png'), pygame.image.load('p/R7E.png'), pygame.image.load('p/R8E.png'), pygame.image.load('p/R9E.png'), pygame.image.load('p/R10E.png'), pygame.image.load('p/R11E.png')]
            walkLeft = [pygame.image.load('p/L1E.png'), pygame.image.load('p/L2E.png'), pygame.image.load('p/L3E.png'), pygame.image.load('p\L4E.png'), pygame.image.load('p/L5E.png'), pygame.image.load('p/L6E.png'), pygame.image.load('p/L7E.png'), pygame.image.load('p/L8E.png'), pygame.image.load('p/L9E.png'), pygame.image.load('p/L10E.png'), pygame.image.load('p/L11E.png')]
            
            def __init__(self, x, y, width, height, end):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.end = end
                self.path = [self.x, self.end]
                self.walkcount = 0
                self.vel = 3
                self.hitbox = (self.x + 17, self.y + 2, 31, 57)
                self.score = 0
                self.health = 10
                self.visible = True
            
            def draw(self, win):
                self.move()
                if self.visible :
                    if self.walkcount +1 >= 33 :
                        self.walkcount = 0
                    
                    if self.vel > 0:
                        win.blit(self.walkRight[self.walkcount//3], (self.x, self.y))
                        self.walkcount+=1
                    else:
                        win.blit(self.walkLeft[self.walkcount//3], (self.x, self.y))
                        self.walkcount+=1
                    
                    pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
                    pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
                    self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)


            def move(self):
                if self.vel > 0:
                    if self.x + self.vel < self.path[1]:
                        self.x += self.vel
                    else:
                        self.vel = self.vel * -1
                        self.walkcount = 0
                    
                else:
                    if self.x - self.vel > self.path[0]:
                        self.x += self.vel
                    else:
                        self.vel = self.vel * -1
                        self.walkcount = 0
                        
                        
            def hit(self): 
                if self.health > 0:
                    self.health -= 1
                else:
                    self.visible = False
                print("hit")
                

                         
            
        # window  drawing 
        def redrawgamewindow():
            win.blit(bg, (0,0))
            text = font.render("score: " + str(score), 1, (0,0,0))
            win.blit(text, (350, 10))
            man.draw(win)
            valian.draw(win)
            goblin.draw(win)
            for bullet in bullets :
                bullet.draw(win)
                
                
            if not(goblin.visible) and not(valian.visible) :
                winfont = font.render(" you win ", 1, (0,0,0))
            pygame.display.update()
                    
        # varibles for main loop
        font =  pygame.font.SysFont("comicsans", 30, True, True)
        man = player(300, 410, 64, 64)
        valian = enemy(90, 415, 64, 64, 450)
        goblin = enemy(10, 415, 64, 64, 460)
        shootloop = 0
        bullets = []
        run = True
        #mainloop
        while run:
            clock.tick(27) # rate of -fps-
            
            
            
            # 1st zombie
            if valian.visible == True:
                if man.hitbox[1] < valian.hitbox[1] + valian.hitbox[3] and man.hitbox[1] + man.hitbox[3] > valian.hitbox[1]:
                    if  man.hitbox[0] + man.hitbox[2] > valian.hitbox[0] and man.hitbox[0] < valian.hitbox[0] + valian.hitbox[2]:
                        man.hit()
                        score -= 5



            # 2nd zombie
            if goblin.visible == True:
                if man.hitbox[1] < valian.hitbox[1] + valian.hitbox[3] and man.hitbox[1] + man.hitbox[3] > valian.hitbox[1]:
                    if  man.hitbox[0] + man.hitbox[2] > valian.hitbox[0] and man.hitbox[0] < valian.hitbox[0] + valian.hitbox[2]:
                        man.hit()
                        score -= 5



            
            if shootloop > 0:
                shootloop += 1
            if shootloop > 3:
                shootloop = 0
            
                        #for closing
            
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                    run= False
                    
                    
                        # for shooting bullets lon 1st zombie
                    
            for bullet in bullets:
                if bullet.y - bullet.redius < valian.hitbox[1] + valian.hitbox[3] and bullet.y + bullet.redius > valian.hitbox[1]:
                    if  bullet.x + bullet.redius > valian.hitbox[0] and bullet.x - bullet.redius < valian.hitbox[0] + valian.hitbox[2]:
                        hitsound.play()
                        valian.hit()
                        score += 1
                        bullets.pop(bullets.index(bullet))
            
                if bullet.x < 500 and bullet.x >0:
                    bullet.x += bullet.vel
                else:
                    bullets.pop(bullets.index(bullet))
                    
                    
            
            
                    
            # for shooting bullets on 2nd zombie         
            for bullet in bullets:
                if bullet.y - bullet.redius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.redius > goblin.hitbox[1]:
                    if  bullet.x + bullet.redius > goblin.hitbox[0] and bullet.x - bullet.redius < goblin.hitbox[0] + goblin.hitbox[2]:
                        hitsound.play()
                        goblin.hit()
                        score += 1
                        bullets.pop(bullets.index(bullet))
            
                if bullet.x < 500 and bullet.x >0:
                    bullet.x += bullet.vel
                else:
                    bullets.pop(bullets.index(bullet))
                    
                    
                    
            
            keys= pygame.key.get_pressed() # alist of pressed keys on key board
            
            if keys[pygame.K_SPACE] and shootloop == 0:
                bulletsound.play()
                if man.left:
                    facing=-1
                else:
                    facing = 1
                if len(bullets) < 10:
                    bullets.append(projectile(round(man.x + man.width//2), round(man.y + man.height//2), 6, (0,0,0), facing))
            
                shootloop+=1
                
            

                
            # right and left motion
            if keys[pygame.K_LEFT] and man.x > man.vel:
                man.x -= man.vel
                man.left=True
                man.right= False
                man.standing = False
            elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
                man.x += man.vel
                man.left=False
                man.right= True
                man.standing = False
            else:
                man.standing = True
                man.walkc = 0
            if not (man.isjump) :
                if keys[pygame.K_UP]: # jumping
                    man.isjump=True
                    man.left = False
                    man.right = False
                    man.walkc = 0
                    
            else:  #jumping mechanism
                if man.jcount >=-10:
                    neg = 1
                    if man.jcount < 0:
                        neg = -1
                    man.y -= (man.jcount**2)*0.5*neg
                    man.jcount-=1
                else:
                    man.isjump= False
                    man.jcount=10
                
            redrawgamewindow()
            
            
        pygame.quit()

    
    
    
    
    def hang():

        class menu:

            def __init__(self):

                self.game = Tk()

                self.game.geometry('600x600+50+50')

                self.game.title("Hang Man")

                self.canvas = Canvas(self.game,height=400,width=800,bg='light goldenrod yellow')  

                self.canvas.delete(ALL)

                self.canvas.create_line(100,50,100,500,tags="Line") #Vertical

                self.canvas.create_line(20,500,80,500,tags="Line") #Lower Horizontal

                self.canvas.create_line(100,50,150,50,tags="Line") #Horizontal Line

                self.canvas.pack() 

                self.play = Button(self.game,text="Play",command=self.playbt)

                self.play.pack(side=BOTTOM)

                self.game.mainloop() # Create an event loop

            def playagain(self):

                self.game.destroy()

                menu()

            def playbt(self):

              self.difs()



            def difs(self):

                self.play.destroy()

                self.easy = Button(self.game,text="Easy",command=self.easy)

                self.medium = Button(self.game,text="Medium",command=self.medium)

                self.hard = Button(self.game,text="Hard",command=self.hard)



                self.easy.pack(side=BOTTOM)

                self.medium.pack(side=BOTTOM)

                self.hard.pack(side=BOTTOM)



            def easy(self):

                ewords = r.choice(["TABLE","CHAIR","DESK","PHONE","LIGHT","MAN"])

                self.playP(ewords.lower())

            def medium(self):

                mwords = r.choice(["PYTHON","LAPTOP","JACKET","VIDEO","MODULE","LIBRARY"])

                self.playP(mwords.lower())

            def hard(self):

                hwords = r.choice(["PROGRAM","TOLEDO","UNIVERSITY","ENGINEER","FOOTBALL","LANGUAGE"])

                self.playP(hwords.lower())



            def playP(self,words):

                self.lwords = words

                for i in range(0, len(self.lwords)):

                    self.canvas.create_text(300+20*i,310,text="_",font="Times 16",tags="text")

                self.hm = 0

                self.easy.destroy()

                self.medium.destroy()

                self.hard.destroy()

                self.myscore = int(0)



                self.te = StringVar() #Text Entry TextVariable

                self.teb = Entry(self.game, textvariable = self.te) #Text Entry Box

                self.tebt = Button(self.game,text="Submit", command = self.checkAnswer)

                self.teb.pack(side=BOTTOM)

                self.tebt.pack(side=BOTTOM)





            def checkAnswer(self):

                temp= self.te.get()

                score=0 #trial set for each try

                score1=0

                x1=300


                for i in range(0,len(self.lwords)):



                    if temp==self.lwords[i]:

                        self.canvas.create_text(x1+20*i,300,text=self.lwords[i],font="Times 16",tags="text")

                        score1+=1

                        self.myscore += 1


                    if self.myscore == len(self.lwords):

                        self.win()


                if not (score1 > score):

                   self.draw()

                   score=0 

                   score1



            def win(self):

                self.canvas.delete(ALL)

                self.canvas.after(100)

                self.teb.destroy()

                self.tebt.destroy()

                self.canvas.create_text(400,200,text = 'YOU WIN!!',font='Times 36')

                self.pa = Button(self.game,text="Play Again?",command=self.playagain)

                self.pa.pack(side=BOTTOM)



            def draw(self):

                self.hm += 1

                if self.hm == 1:

                  self.canvas.create_oval(125,50,175,100, tags = "Line") #Head

                elif self.hm == 2:

                  self.canvas.create_line(150,100,150,150, tags = "Line") #Body

                elif self.hm == 3:

                  self.canvas.create_line(150,125,125,100, tags = "Line") #Left Arm

                elif self.hm == 4:

                  self.canvas.create_line(150, 125, 175, 100, tags = "Line") #Right Arm

                elif self.hm == 5:

                  self.canvas.create_line(150,150,125,175, tags = "Line") #Left Leg

                elif self.hm == 6:

                  self.canvas.create_line(150,150,175,175, tags = "Line") #Right Leg

                  self.canvas.update()

                  self.canvas.after(100)

                  self.canvas.delete(ALL)

                  self.canvas.create_text(200,200,text="HANG MAN!!",font="Times 36")

                  self.tebt.destroy()

                  self.teb.destroy()

                  self.pa = Button(self.game,text="Play Again?",command=self.playagain)

                  self.pa.pack(side=BOTTOM)







        menu()

        
    
    
    
    
    
    def tic():
        global player
        global cnt
        global bx1
        global bx2
        global bx3
        global bx4
        global bx5
        global bx6
        global bx7
        global bx8
        global bx9
        player = 1
        cnt = 0
        bx1 = "1"
        bx2 = "2"
        bx3 = "3"
        bx4 = "4"
        bx5 = "5"
        bx6 = "6"
        bx7 = "7"
        bx8 = "8"
        bx9 = "9"
        root= Tk()
        root.geometry("500x500")
        root.title("Tic Tac Toe")
        button1 = Button(root, text = "  ",command = lambda: activate(1))
        button1.grid(row='0',column="0",ipadx="75",ipady="70")


        button2 = Button(root, text = "  ",command = lambda: activate(2))
        button2.grid(row='0',column="1",ipadx="75",ipady="70")


        button3 = Button(root, text = "  ",command = lambda: activate(3))
        button3.grid(row='0',column="2",ipadx="75",ipady="70")


        button4 = Button(root, text = "  ",command = lambda: activate(4))
        button4.grid(row='1',column="0",ipadx="75",ipady="70")


        button5 = Button(root, text = "  ",command = lambda: activate(5))
        button5.grid(row='1',column="1",ipadx="75",ipady="70")


        button6 = Button(root, text = "  ",command = lambda: activate(6))
        button6.grid(row='1',column="2",ipadx="75",ipady="70")


        button7 = Button(root, text = "  ",command = lambda: activate(7))
        button7.grid(row='2',column="0",ipadx="75",ipady="70")


        button8 = Button(root, text = "  ",command = lambda: activate(8))
        button8.grid(row='2',column="1",ipadx="75",ipady="70")


        button9 = Button(root, text = "  ",command = lambda: activate(9))
        button9.grid(row='2',column="2",ipadx="75",ipady="70")


        def activate(box):
            global player 
            global cnt
            global bx1
            global bx2
            global bx3
            global bx4
            global bx5
            global bx6
            global bx7
            global bx8
            global bx9
            
            if box == 1 and player == 1:
               if  button1['text'] == "O" or button1['text'] == "X":
                    messagebox._show( 'value','Click another button')
               else:
                    button1.config(text="O")
                    cnt=cnt+1
                    player=2
                    bx1="O"
            elif box == 1 and player == 2:
                if  button1['text'] == "X" or button1['text'] == "O"  :
                    messagebox._show( 'value','Click another button')
                else:
                    button1.config(text="X")
                    cnt=cnt+1
                    player=1
                    bx1="X"
            elif box == 2 and player == 1:
               if  button2['text'] == "O" or button2['text'] == "X" :
                    messagebox._show( 'value','Click another button')
               else:
                    button2.config(text="O")
                    cnt=cnt+1
                    player=2
                    bx2="O"
            elif box == 2 and player == 2:
               if  button2['text'] == "O" or button2['text'] == "X" :
                    messagebox._show( 'value','Click another button')
               else:
                    button2.config(text="X")
                    cnt=cnt+1
                    player=1
                    bx2="X"
            elif box == 3 and player == 1:
               if  button3['text'] == "O" or button3['text'] == "X" :
                    messagebox._show( 'value','Click another button')
               else:
                    button3.config(text="O")
                    cnt=cnt+1
                    player=2
                    bx3="O"
            elif box == 3 and player == 2:
               if  button3['text'] == "O" or button1['text'] == "X" :
                    messagebox._show( 'value','Click another button')
               else:
                    button3.config(text="X")
                    cnt=cnt+1
                    player=1
                    bx3="X"
            elif box == 4 and player == 1:
               if  button4['text'] == "O" or button4['text'] == "X" :
                    messagebox._show( 'value','Click another button')
               else:
                    button4.config(text="O")
                    cnt=cnt+1
                    player=2
                    bx4="O"
            elif box == 4 and player == 2:
                if  button4['text'] == "O" or button4['text'] == "X" :
                    messagebox._show( 'value','Click another button')
                else:
                    button4.config(text="X")
                    cnt=cnt+1
                    player=1
                    bx4="X"
            elif box == 5 and player == 1:
                if  button5['text'] == "O" or button5['text'] == "X" :
                    messagebox._show( 'value','Click another button')
                else:
                    button5.config(text="O")
                    cnt=cnt+1
                    player=2
                    bx5="O"
            elif box == 5 and player == 2:
               if  button5['text'] == "O" or button5['text'] == "X" :
                    messagebox._show( 'value','Click another button')
               else:
                    button5.config(text="X")
                    cnt=cnt+1
                    player=1
                    bx5="X"
            elif box == 6 and player == 1:
               if  button6['text'] == "O" or button6['text'] == "X" :
                    messagebox._show( 'value','Click another button')
               else:
                    button6.config(text="O")
                    cnt=cnt+1
                    player=2
                    bx6="O"
            elif box == 6 and player == 2:
                if  button6['text'] == "O" or button6['text'] == "X" :
                    messagebox._show( 'value','Click another button')
                else:
                    button6.config(text="X")
                    cnt=cnt+1
                    player=1
                    bx6="X"
            elif box == 7 and player == 1:
                if  button7['text'] == "O" or button7['text'] == "X" :
                    messagebox._show( 'value','Click another button')
                else:
                    button7.config(text="O")
                    cnt=cnt+1
                    player = 2
                    bx7="O"
            elif box == 7 and player == 2:
                if  button7['text'] == "O" or button7['text'] == "X" :
                    messagebox._show( 'value','Click another button')
                else:
                    button7.config(text="X")
                    cnt=cnt+1
                    player=1
                    bx7="X"
            elif box == 8 and player == 1:
               if  button8['text'] == "O" or button8['text'] == "X" :
                    messagebox._show( 'value','Click another button')
               else:
                    button8.config(text="O")
                    cnt=cnt+1
                    player=2
                    bx8="O"
            elif box == 8 and player == 2:
                if  button8['text'] == "O" or button8['text'] == "X" :
                    messagebox._show( 'value','Click another button')
                else:
                    button8.config(text="X")
                    cnt=cnt+1
                    player=1
                    bx8="X"
            elif box == 9 and player == 1:
                if  button9['text'] == "O" or button9['text'] == "X" :
                    messagebox._show( 'value','Click another button')
                else:
                    button9.config(text="O")
                    cnt=cnt+1
                    player=2
                    bx9="O"
            elif box == 9 and player == 2:
               if  button9['text'] == "O" or button9['text'] == "X" :
                    messagebox._show( 'value','Click another button')
               else:
                    button9.config(text="X")
                    cnt=cnt+1
                    player=1
                    bx9="X"

            if bx1 == bx2 == bx3 =="O" or bx4 == bx5 == bx6 =="O" or bx7 == bx8 == bx9 =="O":
                player = "O"
                messagebox._show("Game end", "player: " + player + " wins")
                exit(0)
            elif bx1 == bx2 == bx3 =="X" or bx4 == bx5 == bx6 =="X" or bx7 == bx8 == bx9 =="X":
                player = "X"
                messagebox._show("Game end", "player: " + player + " wins")
                exit(0)
            elif bx1 == bx4 == bx7 =="O" or bx2 == bx5 == bx8 =="O" or bx3 == bx6 == bx9 =="O":
                player = "O"
                messagebox._show("Game end", "player: " + player + " wins")
                exit(0)
            elif bx1 == bx4 == bx7 =="X" or bx2 == bx5 == bx8 =="X" or bx3 == bx6 == bx9 =="X":
                player = "X"
                messagebox._show("Game end", "player: " + player + " wins")
                exit(0)
            elif bx1 == bx5 == bx9 =="O" or bx3 == bx5 == bx7 =="O":
                player = "O"
                messagebox._show("Game end", "player: " + player + " wins")
                exit(0)
            elif bx1 == bx5 == bx9 =="X" or bx3 == bx5 == bx7 =="X":
                player = "X"
                messagebox._show("Game end", "player: " + player + " wins")
                exit(0)
            elif cnt==9:
                messagebox._show("Game end", "Draw")
                exit(0)
                
                

        root.mainloop()





        
        
       
        
    def snake():
        

        pygame.init()


        class cube(object):
            w = 500
            rows = 20
            def __init__(self, start, dirx = 1, diry = 0, color = (255,0,0)):
                self.pos = start
                self.dirx = 1
                self.diry = 0
                self.color = color
                
            def move(self, dirx, diry):
                self.dirx = dirx
                self.diry = diry
                self.pos = (self.pos[0] + self.dirx , self.pos[1] + self.diry)
                
                
            def draw(self, surface, eyes = False):
                dis = self.w // self.rows
                i = self.pos[0]
                j = self.pos[1]
                
                pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))
                if eyes :
                    centre = dis//2
                    reduis = 3
                    eyecircle = (i*dis+centre-reduis, j*dis+8)
                    eyecircle2 = (i*dis+dis-reduis*2, j*dis+8)
                    pygame.draw.circle(surface, (0,0,0), eyecircle, reduis)
                    pygame.draw.circle(surface, (0,0,0), eyecircle2, reduis)



        class snake (object):
            body = []
            turns = {}
            
            
            def __init__(self, color, pos):
                self.color = color
                self.head = cube(pos)
                self.body.append(self.head)
                self.dirx = 0
                self.diry = 1
                
            def move(self):
                for evnt in pygame.event.get():  
                    if evnt.type == pygame.QUIT:
                        pygame.quit()
                
                
                        
                    
                    keys = pygame.key.get_pressed() #list of keyboard keys
                
            
                    for key in keys :
                
                        if keys[pygame.K_LEFT]  : # going left 
                            self.dirx = -1
                            self.diry = 0
                            self.turns[self.head.pos[:]] =[self.dirx , self.diry]
                            
                            
                            
                        elif keys[pygame.K_RIGHT]  : # going right
                            self.dirx = 1
                            self.diry = 0
                            self.turns[self.head.pos[:]] =[self.dirx , self.diry]
                         
                         
                         
                        elif keys[pygame.K_UP] : # going up 
                            self.dirx = 0
                            self.diry = -1
                            self.turns[self.head.pos[:]] =[self.dirx , self.diry]
                                
                                
                        elif keys[pygame.K_DOWN] : # going down
                            self.dirx = 0
                            self.diry = 1
                            self.turns[self.head.pos[:]] =[self.dirx , self.diry]

                for i, c in enumerate(self.body):
                    p = c.pos[:]
                    if p in self.turns :
                        turn = self.turns[p]
                        c.move(turn[0], turn[1])
                        if i == len (self.body) - 1 :
                             self.turns.pop(p)
                            
                    else :
                        if c.dirx == -1 and c.pos[0] <= 0:
                            c.pos = (c.rows-1, c.pos[1])
                        elif c.dirx == 1 and c.pos[0] >= c.rows-1:
                            c.pos = (0,c.pos[1])
                        elif c.diry == 1 and c.pos[1] >= c.rows-1:
                            c.pos = (c.pos[0], 0)
                        elif c.diry == -1 and c.pos[1] <= 0:
                            c.pos = (c.pos[0],c.rows-1)
                        else:
                            c.move(c.dirx,c.diry)
                                
                  
            

            def draw(self, surface):
                for i, c in enumerate(self.body):
                    if i == 0:
                        c.draw(surface, True)
                    else :
                        c.draw(surface)
            
            
            
            
            def reset(self, pos):
                self.head = cube(pos)
                self.body = []
                self.body.append(self.head)
                self.turns = {}
                self.dirx = 0
                self.diry = 1



            def addcube(self):
                tail = self.body[-1]
                dx, dy = tail.dirx, tail.diry
                
                if dx == 1 and dy == 0:
                    self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
                elif dx == -1 and dy == 0:
                    self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
                elif dx == 0 and dy == 1:
                    self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
                elif dx == 0 and dy == -1:
                    self.body.append(cube((tail.pos[0],tail.pos[1]+1)))
                

                self.body[-1].dirx = dx
                self.body[-1].diry = dy





        def griddraw(w, rows, surface):
            sizebtwn = w // rows
            
            
            x = 0
            y = 0
            
            for i in range(rows):
                x += sizebtwn
                y += sizebtwn
                
                pygame.draw.line(surface, (255, 255, 255), (x,0), (x,w))
                pygame.draw.line(surface, (255, 255, 255), (0,y), (w,y))



        def randomsnack(rows, item):
            positions = item.body
            while True :
                x = random.randrange(rows)
                y = random.randrange(rows)

                if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
                    continue
                else:
                    break

            return(x,y)


        def message_box(subject, content):
            root = tk.Tk()
            root.attributes("-topmost", True)
            root.withdraw()
            messagebox.showinfo(subject, content)
            try :
                root.destroy()
            except :
                pass




        def drawwindow(surface):
            global width ,rows ,s, snack
            surface.fill((0,0,0))
            s.draw(surface)
            snack.draw(surface)
            #griddraw(width, rows, surface)
            pygame.display.update()




        def main():
            #global variables
            global width , rows, s, snack
            width = 500
            run = True
            s = snake((255,0,0), (10, 10))
            rows = 20
            snack = cube(randomsnack(rows, s), color=(0,255,0))


            win = pygame.display.set_mode((width,width))
            pygame.display.set_caption("snake game")

            clock = pygame.time.Clock()

            
            


            #main loop
            while run :
                
                pygame.time.delay(100)
                clock.tick(10)
                s.move()
              
                
                if s.body[0].pos == snack.pos:
                    s.addcube()
                    snack = cube(randomsnack(rows, s), color=(0,255,0))
                
                for x in range(len(s.body)):
                    if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                        print('Score: ', len(s.body))
                        message_box("You Lost!", "Play again...")
                        s.reset((10,10))
                        break
                
                
                drawwindow(win)
            
                
            
         
        main()








    

    
    hangman = Button(win, text = "snake", command = snake, font=("comic sans ms", 14), width=10, bg="#12c2e9", relief= GROOVE)
    hangman.grid(row = 1, column = 0,padx = 0, pady=50, ipadx=10, ipady=10)


    
    pong=Button(win, text = "zombie", command = zombie, font=("comic sans ms", 14), width=10, bg="#12c2e9", relief= GROOVE)
    pong.grid(row = 1, column = 2,padx = 0, pady=50, ipadx=10, ipady=10)



    tic_tac_toe=Button(win, text = "tic-tac-toe",command = tic, font=("comic sans ms", 14), width=10, bg="#12c2e9", relief= GROOVE)
    tic_tac_toe.grid(row = 2, column = 0,padx = 0, pady=50, ipadx=10, ipady=10)

    
    
    metroites=Button(win, text = "pong",command = pong2, font=("comic sans ms", 14), width=10, bg="#12c2e9", relief= GROOVE)
    metroites.grid(row = 2, column = 2,padx = 0, pady=50, ipadx=10, ipady=10)



    h = Button(win, text ="hang man", command = hang, font=("comic sans ms", 14), width=10, bg="#12c2e9", relief= GROOVE )
    h.grid(row = 3, column = 1,padx = 25, pady=50, ipadx=10, ipady=10)
    
    win.mainloop()








root.geometry("500x500")
root.title("final project protons '19")
root.configure(background="#A9C6D9")


label = Label(root, text="protons game launcher", bg="#A9C6D9", fg="#000000", font=("verdana",25))
label.grid(row = 0, column = 0, padx = 50, pady=30, ipadx=10, ipady=10)



playbutton= Button(root, text="play", font=("comic sans ms", 14), width=14, bg="#12c2e9", relief= GROOVE, command = click)
playbutton.grid(row = 1, column = 0, padx = 50, pady=30, ipadx=10, ipady=10)


aboutusbutton= Button(root, text="about us", font=("comic sans ms", 14), width=14, bg="#12c2e9", relief= GROOVE, command= about)
aboutusbutton.grid(row = 2, column = 0, padx = 50, pady=30, ipadx=10, ipady=10)


exitbutton= Button(root, text="exit", font=("comic sans ms", 14), width=14 , bg="#12c2e9", relief= GROOVE, command = root.quit)
exitbutton.grid(row = 3, column = 0, padx = 50, pady=30, ipadx=10, ipady=10)





root.mainloop()
