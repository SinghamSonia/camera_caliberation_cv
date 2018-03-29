import tkinter as tk
from tkinter import filedialog
import sys
import cv2
import numpy as np
import math
from PIL import Image, ImageTk
import os
selection_vector, selections, p_vector = [], [], []

dir_path = os.path.dirname(os.path.realpath(__file__))

#This creates the main window of an application
window = tk.Tk()
window.title("Image_GUI")
window.geometry("1366x768")
window.configure(background='grey')

path =  filedialog.askopenfilename(initialdir = dir_path,title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

menubar = tk.Menu(window)
window.config(menu = menubar)

filemenu = tk.Menu(menubar)
#Create a menu button labeled "File" that brings up a menu
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Quit', command=sys.exit)

# path = "ThreePanel4.jpg"
resized = Image.open(path).resize((1366, 768), Image.ANTIALIAS)
resized.save("resize.jpg")
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(resized)

imagecv = cv2.imread("resize.jpg")

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#Returns the value of lambda
def myFun(world_point, image_point, axis):
	return (image_point[0]-p_vector[3][0])/(world_point*p_vector[axis][0])

def crs(a, b):
	c = [a[1]*b[2] - a[2]*b[1],
	a[2]*b[0] - a[0]*b[2],
	a[0]*b[1] - a[1]*b[0]]
	return c
	
def distance(t, u):
	return (math.sqrt((int(t[0]) - int(u[0]))**2 + (int(t[1]) - int(u[1]))**2))

def click(event):
	
	print ("Clicked Pixel : (%s, %s)" %(str(event.x), str(event.y)))

	selection_vector = [int(event.x), int(event.y)]
	selections.append(selection_vector)
	if(len(selections)%2==0 and len(selections) <= 6):
		print("length in pixels between two image points = " + str(distance(selections[len(selections)-1],selections[len(selections)-2])))
		x=selections[-1]+[1]
		y=selections[-2]+[1]
		cross = crs(x,y)
		print("Line: " + str(cross))
		p_vector.append([cross[1],-1*(cross[0]),0])
	if(len(selections) == 6): print("Select corner point where two walls meet with the attic which will be image of World Origin")
	
	if(len(selections) == 7):
		p_vector.append([selections[6][0], 768-selections[6][1] , 1])
		print("Select 2 points across width of windows on left wall from left to right to calculate px/meter")
	
	if(len(selections) >= 9):
		ppi = distance(selections[8],selections[7])/(0.6)
		#Corresponding point on Z-Axis for selections[7]
		corresponding_point = crs(crs(selections[8]+[1],selections[7]+[1]),crs(selections[4]+[1],selections[5]+[1]))
		corresponding_point[0]=(float(corresponding_point[0])/corresponding_point[2])
		corresponding_point[1]=(float(corresponding_point[1])/corresponding_point[2])
		corresponding_point = corresponding_point[:2]
		
		#Corresponding point on Z-Axis for selections[2]
		corresponding_pointy = crs(crs(selections[4]+[1],selections[5]+[1]), crs(selections[2]+[1],selections[3]+[1]))
		corresponding_pointy[0]=(float(corresponding_pointy[0])/corresponding_pointy[2])
		corresponding_pointy[1]=(float(corresponding_pointy[1])/corresponding_pointy[2])
		corresponding_pointy = corresponding_pointy[:2]


		totx = distance(corresponding_point,selections[7])/ppi
		totz = distance(selections[6],corresponding_point)/ppi
		toty = distance(selections[2]+[1],corresponding_pointy)/ppi
		lam1 = myFun(totx,selections[7],0)
		lam2 = myFun(toty,selections[2],1)
		lam3 = myFun(totz,corresponding_point,2)

		ans = [lam1, lam2, lam3]
		print("\n\n##Projection Matrix##\n")
		pro = [[ans[i]*p_vector[i][j] for j in range(3)] for i in range(3)]

		pro = [[pro[j][i] for j in range(3)] for i in range(3)]
		pro[0].append(selections[6][0])
		pro[1].append(selections[6][1])
		pro[2].append(1)
		for t in range(3):
			print(pro[t])



#The Pack geometry manager packs widgets in rows or columns.
panel.bind("<Button-1>", click)

panel.pack(side = "bottom", fill = "both", expand = "yes")

print("Select 2 points in each direction x, y and z")
#Start the GUI
window.mainloop()