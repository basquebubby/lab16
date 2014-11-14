# Lab 16
# 70pt -  Add in movement buttons for up, down, left and right using WASD
# 80pt -  Make sure the player can't go out of bounds to the left, right or down.
# 90pt -  When you hit space, fire a missile straight up! 
#         Subtract from how many missiles you have left
# 100pt - Destroy the target if a missile hits it! 
# Hints: use drawpad.delete(enemy) in the collision detect function, which you can trigger
# from the key press event... maybe a loop to keep checking until the rocket goes out of bounds?
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
background = drawpad.create_rectangle(0,0,800,400, fill="black")
rocket1 = drawpad.create_rectangle(400,585,405,590, fill="white", outline="blue")
player = drawpad.create_oval(390,580,410,600, fill="blue")
enemy = drawpad.create_rectangle(50,50,100,60, fill="red")
rocket1Fired = False
width = 600
height = 800
direction = 5


class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        global rocket1Fired
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        # Enter my text
        self.prompt = "Rockets left :"
        
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='green')
        self.label1.pack()

        self.rockets = 3
        
        self.rocketsTxt = Label(root, text=str(self.rockets), width=len(str(self.rockets)), bg='green')
        self.rocketsTxt.pack()
        
        self.rocket1Fired = False
        # Adding the drawpad, adding the key listener, starting animation
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
    
    def animate(self):
        global drawpad
        global enemy
        global direction
        global rocket1
        global rocket1Fired
        x1,y1,x2,y2 = drawpad.coords(enemy)
        px1,py1,px2,py2 = drawpad.coords(player)
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket1)
        if x2 > 800:
            direction = - 5
        elif x1 < 0:
            direction = 5
        if rocket1Fired == True:
            drawpad.move(rocket1,0,-15)
        if ry2 < 0:
            drawpad.move(rocket1,px1-rx1+7.5,py1+30)
            rocket1Fired = False
        if self.rockets == 0:
            direction = 0
        didWeHit = self.collisionDetect(rocket1)
        if didWeHit == True:
            drawpad.delete(enemy)
            drawpad.move(rocket1,px1-rx1+7.5,py1-ry1+15)
        if didWeHit == False:
            drawpad.move(enemy,direction,0)
            drawpad.after(5,self.animate)

    def key(self,event):
        global width
        global height
        global player
        global rocket1
        global rocket1Fired
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket1)
        px1,py1,px2,py2 = drawpad.coords(player)
        if event.char == " ":
            rocket1Fired = True
            self.rockets = self.rockets - 1
            self.rocketsTxt.configure(text=self.rockets)
        if event.char == "w":        #Up Key
            drawpad.move(player,0,-4)
            drawpad.move(rocket1,0,-4)
            if py1 <= 400:
                drawpad.move(player,0,4)
                drawpad.move(rocket1,0,4)
        if event.char == "a":        #Left Key
            drawpad.move(player,-4,0)
            drawpad.move(rocket1,-4,0)
            if px1 <= 0:
                drawpad.move(player,4,0)
                drawpad.move(rocket1,4,0)
        if event.char == "s":        #Down Key
            drawpad.move(player,0,4)
            drawpad.move(rocket1,0,4)
            if py2 >= 600:
                drawpad.move(player,0,-4)
                drawpad.move(rocket1,0,-4)
        if event.char == "d":        #Right Key
            drawpad.move(player,4,0)
            drawpad.move(rocket1,4,0)
            if px2 >= 800:
                drawpad.move(player,-4,0)
                drawpad.move(rocket1,-4,0)
    
    def collisionDetect(self, rocket1):
        global enemy
	global drawpad
        global rocket1Fired
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket1)
        ex1,ey1,ex2,ey2 = drawpad.coords(enemy)
        if ((rx1+5 >= (ex1-5)) and (rx2+5 <= (ex2+5))) and ((ry1+5 >= (ey1-5)) and (ry2+5 <= (ey2+5))):
            return True
        else:
            return False

app = myApp(root)
root.mainloop()