# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 17:53:20 2019

@author: Chris
"""
import cv2
import PIL
import tkinter
from PIL import ImageTk


class Window(object):
    def __init__(self, name=None):
        self.window = tkinter.Tk()
        self.window.title(name)
        
    def start(self):
        self.window.mainloop()
        
class MainWindow(Window):
    def __init__(self, name=None):
        super().__init__(name=name)
    
class ImageWindow(Window):
    def __init__(self, name=None, imageArrays=None, images=None):
        super().__init__(name=name)
        if not isinstance(images, list):
            self.images = [images]
        else:
            self.images = image.copy()
        if not isinstance(imageArrays, list):
            self.imageArrays = [imageArrays]
        else:
            self.imageArrays = imageArray
        if self.imageArray is not None:
            height, width, _ = self.imageArray.shape
            self.canvas = tkinter.Canvas(self.window,
                                         width=1.1*width,
                                         height=1.1*height)
        else:
            self.canvas = tkinter.Canvas(self.window,
                                         width=300,
                                         height=300)
        
    def convertCV2ToPIL(self):
        dims = self.imageArray.shape
        if len(dims) == 2:
            self.imageArray = cv2.cvtColor(self.imageArray,cv2.COLOR_GRAY2RGB)
        elif len(dims) == 3:
            self.imageArray = cv2.cvtColor(self.imageArray,cv2.COLOR_BGR2RGB)
        else:
            raise IOError("Can only accept 2D and 3D image arrays")
        convertedImage = PIL.Image.fromarray(self.imageArray)
        self.image = ImageTk.PhotoImage(image=convertedImage,master=self.window)
        
    def loadImages(self):
        
    
    def loadImage(self,rowIndex=0,columnIndex=0):
        self.canvas.grid(row=rowIndex,column=columnIndex)
        self.canvas.create_image(20,20, anchor="nw", image=self.image)
        
    def main(self):
        self.convertCV2ToPIL()
        self.loadImage()
        self.start()
                   
image = cv2.imread(r"C:\Users\Chris\Pictures\Annotation 2019-10-29 223318.png")
window = ImageWindow(imageArray=image)
window.imageArray = image
window.main()