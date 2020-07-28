import glob
import numpy as np
from tkinter import *
from PIL import Image, ImageTk

def getImages():
    #images = [12, 11, 13, 5, 6, 7, 99, 2]
    #create array of images
    images = []
    for f in glob.iglob("pics/*"):
        images.append(np.asarray(Image.open(f)))

    np.random.shuffle(images)
    #images = np.array(images)
    return images
    
def saveOrder(a):
    for ind,image in enumerate(a):
        Image.fromarray(image).save('newOrder/'+str(ind)+'.png','PNG')


def mergeSort(a): 
	if len(a) > 1: 
		mid = len(a) // 2
		L = a[:mid] 
		R = a[mid:] 
		mergeSort(L) 
		mergeSort(R) 
		
		a.clear() 
		while len(L) > 0 and len(R) > 0:
			if compImages(L[0], R[0]): 
				a.append(L[0]) 
				L.pop(0) 
			else: 
				a.append(R[0]) 
				R.pop(0) 

		for i in L: 
			a.append(i) 
		for i in R: 
			a.append(i) 

def compImages(l,r):
    #create user ui for choosing between two images
    decision = None
    
    root = Tk()

    pilImage = Image.fromarray(np.array(l))
    pilImage2 = Image.fromarray(np.array(r))
    image = ImageTk.PhotoImage(pilImage)
    image2 = ImageTk.PhotoImage(pilImage2)
    
    def choseLeft():
        nonlocal decision
        decision = False
        root.destroy()
        
    def choseRight():
        nonlocal decision
        decision = True
        root.destroy()
        
    l_display = Button(root, image=image, command=choseLeft)
    r_display = Button(root, image=image2, command=choseRight)
    
    l_display.pack()
    r_display.pack()

    root.mainloop()
    return decision

# Input list 
a = getImages()

mergeSort(a) 

saveOrder(a)

