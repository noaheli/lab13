#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class
circle = drawpad.create_oval(10, 10, 50, 50, fill='green')
circle1 = drawpad.create_oval(600, 200, 640, 240, fill='green')
circle2 = drawpad.create_oval(300, 300, 340, 340, fill='green')

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=0)
       	    self.up.bind("<Button-1>", self.upClicked)
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "green")
       	    self.down.grid(row=1,column=1)
       	    self.down.bind("<Button-1>", self.downClicked)
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "green")
       	    self.left.grid(row=1,column=0)
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "green")
       	    self.right.grid(row=1,column=2)
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
	
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player, 20,0)
		

	
def animate1():
    global drawpad
    global player
    global circle
    # Remember to include your "enemies" with "global"
    x1, y1, x2, y2 = drawpad.coords(circle)
    if x2 > drawpad.winfo_width(): 
        drawpad.move(circle, -800, 0)
    drawpad.move(circle,8,0)
    drawpad.after(1, animate1)	
animate1()
	
def animate2():
    global drawpad

    global player
    global circle1
    # Remember to include your "enemies" with "global"
    x1, y1, x2, y2 = drawpad.coords(circle1)
    if x2 < 0: 
        drawpad.move(circle1, 800, 0)
    drawpad.move(circle1,-5,0)
    drawpad.after(1, animate2)	
animate2()
def animate3():
    global drawpad
    global player
    global circle2
    # Remember to include your "enemies" with "global"
    x1, y1, x2, y2 = drawpad.coords(circle2)
    if x2 > drawpad.winfo_width(): 
        drawpad.move(circle2, -800, 0)
    drawpad.move(circle2,2,0)
    drawpad.after(1, animate3)	
animate3()
app = MyApp(root)
root.mainloop()