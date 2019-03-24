#!/usr/bin/env python
# coding: utf-8

# In[11]:


from tkinter import *
from random import randint
from PIL import ImageTk, Image,ImageDraw
import cv2
from tkinter import filedialog

def exit():
    global top
    top.destroy()

def clear_label_image():
    global l,counter,list_point,width,height
    l.config(image='')
    counter = 1
    list_point = []
    width = None
    height = None

    l = None

def getorigin(eventorigin):
      global list_point
      global counter
      global e1
      if counter <= int(e1.get()):
          list_point.append((eventorigin.x,eventorigin.y))
          counter = counter +1

def drawpolygon():
    global list_point
    global width,height
    global e1
    global index
    im = Image.new("RGB", (width,height), "black")
    draw = ImageDraw.Draw(im)
    draw.line(list_point[:int(int(e1.get())/2)],fill='green',width=5)
    draw.line(list_point[int(int(e1.get())/2):int(e1.get())],fill='green',width=5)
    filename = "y"+str(index)+".jpg"
    index+=1
    im.save(filename)

def open_img():
    global top
    global width , height ,l
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    # Load an image using OpenCV
    #cv_img = cv2.cvtColor(cv2.imread(filename,1),cv2.COLOR_BGR2RGB)
    width = 960
    height = 540
    # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
    img = Image.open(filename)
    photo = ImageTk.PhotoImage(img.resize((width,height),Image.ANTIALIAS))
    label = Label(image=photo)
    label.image = photo # keep a reference!
    l = label
    label.pack()
    label.place(x=0,y=0)

    label.bind("<Button 1>",getorigin)
    import_button = Button(top,text='clear',command= clear_label_image)
    import_button.place(x=650, y=650)
index=0
list_point = []
width = None
height = None
l = None
counter = 1
top = Tk()
top.title('segmentation tool')
top.geometry("1280x1280")
import_button = Button(top,text='import',command=open_img)
import_button.place(x=200, y=650)
import_button = Button(top,text='draw',command=drawpolygon)
import_button.place(x=450, y=650)
import_button = Button(top,text='exit',command=exit)
import_button.place(x=900, y=650)
l = Label(top, text="Enter no of points")
l.place(x=200,y=680)
e1 = Entry(top)
e1.place(x=400,y=680)
top.mainloop()
