import tkinter as tk
from tkinter import filedialog
import sys
import cv2
import numpy as np
import math
from PIL import Image, ImageTk
import os
selection_vector, selections, m = [], [], []

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

def linearSolve(x, y, a, b):
	A=np.array([[m[0][0]*x,m[1][0]*y,-150*m[2][0]],[m[0][1]*x,m[1][1]*y,-150*m[2][1]],[x, y, -150]])
	B = np.array([[a], [b], [1]])
	return np.linalg.solve(A, B)


def vanishP(selections):
	x=selections[-1]+[1]
	y=selections[-2]+[1]

	crs_pdt1=crs(x,y)
	print("Line1 = " + str(crs_pdt1))
	a=selections[-3]+[1]
	b=selections[-4]+[1]
	crs_pdt2=crs(a,b)
	print("Line2 = " + str(crs_pdt2))
	crs_pdt = crs(crs_pdt1,crs_pdt2)
	print("Line1xLine2 = " + str(crs_pdt))
	crs_pdt[0]=(float(crs_pdt[0])/crs_pdt[2])
	crs_pdt[1]=(float(crs_pdt[1])/crs_pdt[2])
	m.append(crs_pdt[:2] + [1])
	print("Vanishing point = "+str(crs_pdt[:2]))

def crs(a, b):
	c = [a[1]*b[2] - a[2]*b[1],
	a[2]*b[0] - a[0]*b[2],
	a[0]*b[1] - a[1]*b[0]]
	return c

def distance(p0, p1):
	return (math.sqrt((int(p0[0]) - int(p1[0]))**2 + (int(p0[1]) - int(p1[1]))**2))

def click(event):

	imagecv = cv2.imread("resize.jpg")
	print ("Clicked Pixel : (%s, %s)" %(str(event.x), str(event.y)))

	selection_vector = [int(event.x), int(event.y)]
	selections.append(selection_vector)
	if(len(selections)%2==0):
		print("length in pixels between two image points = " + str(distance(selections[len(selections)-1],selections[len(selections)-2])))
	if(len(selections)%4==0 and len(selections) <= 12):
		vanishP(selections)
	if(len(selections) == 12):
		print("Select two pairs of wheels to calculate px/meter")
	if(len(selections) == 14):
		#ppi = distance(selections[12],selections[13])/(28.660344)
		print("Assuming World Origin and Center at (0,0,0) which last column of Projection Matrix")
		print("\nSelect middle point on the nearest Airplane.")

	if(len(selections) > 14):
		ppi = distance(selections[12],selections[13])/(28.660344)
		x,y=float(selections[14][0])/ppi,float(selections[14][1])/ppi
		z = -150
		ans = linearSolve(x, y, selections[14][0], selections[14][1])
		print("\n\n##Projection Matrix##\n")
		pro = [[m[i][j]*ans[i][0] for j in range(3)] for i in range(3)]
		pro = [[pro[j][i] for j in range(3)] for i in range(3)]

		pro[0].append(0)
		pro[1].append(0)
		pro[2].append(0)
		for t in range(3):
			print(pro[t])


#The Pack geometry manager packs widgets in rows or columns.
panel.bind("<Button-1>", click)

panel.pack(side = "bottom", fill = "both", expand = "yes")

print("Please select 2 sets of two points in X, Y and Z axes of World Co-ordinate")
#Start the GUI
window.mainloop()