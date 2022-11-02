#image processing
import cv2
import glob
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import os
from tkinter import filedialog
class Annotation:

    def __init__(self,root):
        self.root=root
        self.label_file_explorer = Label(root,
                            text = "chechking images",
                            width = 100, height = 4,
                            fg = "blue")
        self.button_explore = Button(root,
                        text = "Browse Files",
                        command = self.browseFiles)
        self.label_file_explorer.place(relx=0.2,rely=0.2,anchor=CENTER)
        self.button_explore.place(relx=0.2,rely=0.4,anchor=CENTER)



    def browseFiles(self):
        filename = filedialog.askdirectory()
        self.label_file_explorer.configure(text="File Opened: "+filename)
        print(filename)
        self.check(filename)
    
      
    def check(img1,img2):

        img1 = cv2.imread("C:/Users/haarv\OneDrive/Desktop/AMS-INDIA/testimg1.jpg")
        x = width1 = img1.shape[1]
        y = height1 = img1.shape[0]
        img2=glob.glob(f"{img2}/*.jpg")
        x2 = width2 = img2.shape[1]
        y2 = height2 = img2.shape[0]

        
        if x == x2 and x2 == y2:

            messagebox.showinfo(title='THE END RESULT',
                         message='THE IMAGE DIMENSIONS MATCHED  PERFECT')
            
        else:
            messagebox.showinfo(title='THE END RESULT '
                        , message='DIMENSIONS NOT MATCHING')
                        
if __name__=="__main__":

    root=Tk()
    root.title("CHECK WINDOW")
    root.geometry("400x150")
    root.config(background='white')


    obj=Annotation(root)
    root.mainloop()
                       
                       
        
        
        

        
        
