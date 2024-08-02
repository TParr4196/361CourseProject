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
window.title("Dog Park Experts")

def mainPage():
    clear()
    favoritesLabel = Label(window, 
              text ="Here are our favorites:")
    favoritesLabel.pack(pady=10)
    userInfoBtn = Button(window, 
             text ="User Info", 
             command = userPage)
    userInfoBtn.pack(pady = 10)

    logoutBtn = Button(window, 
             text ="Log out", 
             command = loginPage)
    logoutBtn.pack(pady = 10)

    addParkBtn = Button(window, 
             text ="Add a Park", 
             command = addParkPage)
    addParkBtn.pack(pady = 10)
    parkBtn = Button(window, 
             text ="Park", 
             command = parkPage)
    parkBtn.pack(pady = 10)

def parkPage():
    clear()
    backBtn = Button(window, 
             text ="Back", 
             command = mainPage)
    backBtn.pack(pady = 10)
    reviewBtn = Button(window, 
             text ="Add a Review", 
             command = reviewPage)
    reviewBtn.pack(pady = 10)

def reviewPage():
    clear()
    backBtn = Button(window, 
             text ="Back/Cancel", 
             command = parkPage)
    backBtn.pack(pady = 10)
    submitBtn = Button(window, 
             text ="Submit", 
             command = parkPage)
    submitBtn.pack(pady = 10)


def userPage():
    clear()
    backBtn = Button(window, 
             text ="Back", 
             command = mainPage)
    backBtn.pack(pady = 10)

def addParkPage():
    clear()
    backBtn = Button(window, 
             text ="Back", 
             command = mainPage)
    backBtn.pack(pady = 10)
    submitBtn = Button(window, 
             text ="Submit", 
             command = mainPage)
    submitBtn.pack(pady = 10)

# citation for the following function:
# Date: 07/31/24
# copied from:
# https://stackoverflow.com/questions/15781802/python-tkinter-clearing-a-frame
def clear():
    for widget in window.winfo_children():
        widget.destroy()

 
def loginPage():
    clear()
    welcomeLabel = Label(window, 
              text ="Welcome to Dog Park Experts!")
    welcomeLabel.pack(pady = 10)

    userLabel = Label(window, 
              text ="username:")
    userLabel.pack(pady = 10)

    # citation for the following widget:
    # Date: 08/01/24
    # adapted from:
    # https://www.geeksforgeeks.org/python-tkinter-text-widget/ 
    userText= Text(window, height=1, width=20)
    userText.pack()

    passLabel = Label(window, 
              text ="password:")
    passLabel.pack(pady = 10)
    passText= Text(window, height=1, width=20)
    passText.pack()
 
# a button widget which will open a 
# new window on button click
    loginBtn = Button(window, 
             text ="Log in", 
             command = mainPage)
    loginBtn.pack(pady = 10)

    
    accountFeatureLabel = Label(window, 
              text ="Create an account to track your visited parks or review and add new ones!")
    accountFeatureLabel.pack(pady=100)
    guestBtn = Button(window, 
             text ="Continue as Guest", 
             command = mainPage)
    guestBtn.pack(pady = 10)
    
 
# mainloop, runs infinitely
loginPage()
mainloop()