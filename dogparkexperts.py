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
    userInfoBtn = Button(window, 
             text ="Track your parks: User Info", 
             command = userPage)
    
    # citation for the follow anchor syntax:
    # Date: 08/01/24
    # Adapted from:
    # https://stackoverflow.com/questions/58016467/how-to-make-tkinterpack-place-label-on-top-left-corner-in-below-program
    userInfoBtn.pack(pady=0, anchor=NE)

    logoutBtn = Button(window, 
             text ="Log out", 
             command = loginPage)
    logoutBtn.pack(pady = 0,anchor=NE)

    tagsLabel = Label(window, 
              text ="Sort by Tags:")
    tagsLabel.pack(padx=10, pady=10, anchor=NW)

    tagsText= Text(window, height=1, width=20)
    tagsText.pack(padx=10, pady=10, anchor=NW)

    tagBtn = Button(window, 
             text ="Suggested tags here", 
             command = mainPage)
    tagBtn.pack(padx=10, pady = 10, anchor=NW)

    favoritesLabel = Label(window, 
              text ="Here are our favorites:")
    favoritesLabel.pack(pady=10)

    parkLeftArrow = Button(window, 
             text ="<-", 
             command = parkPage)
    parkLeftArrow.pack(pady = 10, side=LEFT, padx= 95)

    parkBtnOne = Button(window, 
             text ="Park", 
             command = parkPage)
    parkBtnOne.pack(pady = 10, side=LEFT)
    parkBtnTwo = Button(window, 
             text ="Park", 
             command = parkPage)
    parkBtnTwo.pack(pady = 10, side=LEFT)
    parkBtnThree = Button(window, 
             text ="Park", 
             command = parkPage)
    parkBtnThree.pack(pady = 10, side=LEFT)

    parkRightArrow = Button(window, 
             text ="->", 
             command = parkPage)
    parkRightArrow.pack(pady = 10, side=LEFT, padx=55)

    addParkBtn = Button(window, 
             text ="Add a Park", 
             command = addParkPage)
    addParkBtn.pack(pady = 0, side=BOTTOM, anchor=SE)

def parkPage():
    clear()
    backBtn = Button(window, 
             text ="Back", 
             command = mainPage)
    backBtn.pack(pady = 0, anchor=NE)

    tagsLabel = Label(window, 
              text ="Tags:")
    tagsLabel.pack(pady = 10)

    reviewsLabel = Label(window, 
              text ="Reviews:")
    reviewsLabel.pack(pady = 10)

    reviewBtn = Button(window, 
             text ="Add a Review", 
             command = reviewPage)
    nameLabel = Label(window, 
              text ="Park Name")
    nameLabel.pack(pady=10)
    reviewBtn.pack(pady = 0, side=BOTTOM, anchor=SE)

def reviewPage():
    clear()
    backBtn = Button(window, 
             text ="Back/Cancel", 
             command = parkPage)
    backBtn.pack(pady = 0, anchor=NE)

    thankYouLabel = Label(window, 
              text ="Thank you for Reviewing Park Name!")
    thankYouLabel.pack(pady=10)

    ratingLabel = Label(window, 
              text ="Rating out of 5:")
    ratingLabel.pack(pady = 10)
    ratingText= Text(window, height=1, width=20)
    ratingText.pack()

    tagsLabel = Label(window, 
              text ="Tags (please separate by a comma):")
    tagsLabel.pack(pady = 10)
    tagsText= Text(window, height=1, width=20)
    tagsText.pack()

    picLabel = Label(window, 
              text ="Picture:")
    picLabel.pack(pady = 10)
    picText= Text(window, height=1, width=20)
    picText.pack()

    submitBtn = Button(window, 
             text ="Submit", 
             command = parkPage)
    submitBtn.pack(pady = 0, side=BOTTOM, anchor=S)

def userPage():
    clear()
    backBtn = Button(window, 
             text ="Back", 
             command = mainPage)
    backBtn.pack(pady = 0, anchor=NE)

    usernameLabel = Label(window, 
              text ="Welcome Username!")
    usernameLabel.pack(pady=10)

    favoriteLabel = Label(window, 
              text ="Favorite Parks:")
    favoriteLabel.pack(pady=10)

    visitedLabel = Label(window, 
              text ="Visited Parks:")
    visitedLabel.pack(pady=10)

    yourParksLabel = Label(window, 
              text ="Your Parks:")
    yourParksLabel.pack(pady=10)

    yourPicturesLabel = Label(window, 
              text ="Your Pictures:")
    yourPicturesLabel.pack(pady=10)

    reviewLabel = Label(window, 
              text ="Your Reviews:")
    reviewLabel.pack(pady=10)

    accountInfoLabel = Label(window, 
              text ="This information will be saved even after you log out!")
    accountInfoLabel.pack(pady=10)

    deleteAccountBtn = Button(window, 
             text ="Delete Account", 
             command = userPage)
    deleteAccountBtn.pack(pady = 0, side=BOTTOM, anchor=SE)

def addParkPage():
    clear()
    backBtn = Button(window, 
             text ="Back", 
             command = mainPage)
    backBtn.pack(pady = 0, anchor=NE)

    thankYouLabel = Label(window, 
              text ="Thank you for Adding a Park!")
    thankYouLabel.pack(pady=10)

    nameLabel = Label(window, 
              text ="Park Name:")
    nameLabel.pack(pady = 10)
    nameText= Text(window, height=1, width=20)
    nameText.pack()

    passLabel = Label(window, 
              text ="Location:")
    passLabel.pack(pady = 10)
    passText= Text(window, height=1, width=20)
    passText.pack()

    picLabel = Label(window, 
              text ="Picture:")
    picLabel.pack(pady = 10)
    picText= Text(window, height=1, width=20)
    picText.pack()

    submitBtn = Button(window, 
             text ="Add Park", 
             command = mainPage)
    submitBtn.pack(pady = 0,side=BOTTOM, anchor=S)

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
    createAccountBtn = Button(window, 
             text ="Create an Account", 
             command = mainPage)
    createAccountBtn.pack(pady = 10)

    
    accountFeatureLabel = Label(window, 
              text ="Create an account to track your visited parks or review and add new ones!")
    accountFeatureLabel.pack(pady=10)
    guestBtn = Button(window, 
             text ="Continue as Guest", 
             command = mainPage)
    guestBtn.pack(pady = 90)
    
 
# mainloop, runs infinitely
loginPage()
mainloop()