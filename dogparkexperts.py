# Citation for creation of a window and button in python:
# Date: 7/29/2024
# Adapted from:
# https://www.geeksforgeeks.org/open-a-new-window-with-a-button-in-python-tkinter/
from tkinter import *
from tkinter.ttk import *

# creates a Tk() object
master = Tk()
 
# sets the geometry of main 
# root window
master.geometry("600x400")
 
# function to open a new window 
# on a button click
def openNewWindow():
     
    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel(master)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    Label(newWindow, 
          text ="This is a new window").pack()
 
 
label = Label(master, 
              text ="Welcome to Dog Park Experts")
 
label.pack(pady = 10)
 
# a button widget which will open a 
# new window on button click
btn = Button(master, 
             text ="Continue as Guest", 
             command = openNewWindow)
btn.pack(pady = 10)
 
# mainloop, runs infinitely
mainloop()