import tkinter 
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class get_window :
    #function to provide a message
    @staticmethod 
    def show(s,t):
        window=Tk()
        window.withdraw()   # Tk widow is been hidden 
        messagebox.showinfo(s,t)  # then this message is shown 

    # getting the path of the file
    @staticmethod 
    def path():
        root=Tk()
        root.withdraw()   # same hiding the Tkwindow()
        file_path=filedialog.askopenfilename()  # getting path of the file 
        return file_path  # returning the path of the file 

