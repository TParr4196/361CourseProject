# Citation for creation of a window and button in python:
# Date: 7/29/2024
# Adapted from:
# https://www.geeksforgeeks.org/open-a-new-window-with-a-button-in-python-tkinter/
from tkinter import *
from tkinter.ttk import *

# creates a Tk() object
window = Tk()
 
# sets the geometry of main 
# root window
window.geometry("750x500")
 
# function to open a new window 
# on a button clic8
def mainPage():
    clear()
    welcomeLabel = Label(window, 
              text ="Here are our favorites:")
    welcomeLabel.pack(pady=10)
    

# citation for the following function:
# Date: 07/31/24
# copied from:
# https://stackoverflow.com/questions/15781802/python-tkinter-clearing-a-frame
def clear():
    for widget in window.winfo_children():
        widget.destroy()

 
def login():
    guestLabel = Label(window, 
              text ="Welcome to Dog Park Experts")
 
    guestLabel.pack(pady = 10)
 
# a button widget which will open a 
# new window on button click
    btn = Button(window, 
             text ="Continue as Guest", 
             command = mainPage)
    btn.pack(pady = 10)
 
# mainloop, runs infinitely
login()
mainloop()