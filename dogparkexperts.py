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

import random

def mainPage(shift):
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
             command = lambda:mainPage(shift))
    tagBtn.pack(padx=10, pady = 10, anchor=NW)

    favoritesLabel = Label(window, 
              text ="Here are our favorites:")
    favoritesLabel.pack(pady=10)

    parks=[]
    file=open("txts/park-service.txt", 'w', encoding="utf-8")
    file.write("r,")
    file.close()
    
    while len(parks)<=0:
        file = open("txts/park-service.txt", 'r', encoding="utf-8")
        input=file.readline()
        check=input.split(",")
        if check[0]=="RR":
            for line in file:
                if line=="RR" or "":
                    continue
                else:
                    parks.append(line.split(","))
            file.close()
            file = open("txts/park-service.txt", 'w', encoding="utf-8")
            file.close()

    parkLeftArrow = Button(window, 
             text ="<-", 
             command = lambda: shiftDown(shift, len(parks)))
    parkLeftArrow.pack(pady = 10, side=LEFT, padx= 50)

    parkBtnOne = Button(window, 
             text = parks[shift][0], 
             command = lambda: parkPage(parks[shift], 0))
    parkBtnOne.pack(pady = 10, side=LEFT)
    parkBtnTwo = Button(window, 
             text = parks[(shift+1)%len(parks)][0], 
             command = lambda: parkPage(parks[(shift+1)%len(parks)], 0))
    parkBtnTwo.pack(pady = 10, side=LEFT)
    parkBtnThree = Button(window, 
             text = parks[(shift+2)%len(parks)][0], 
             command = lambda: parkPage(parks[(shift+2)%len(parks)], 0))
    parkBtnThree.pack(pady = 10, side=LEFT)

    parkRightArrow = Button(window, 
             text ="->", 
             command = lambda: shiftUp(shift, len(parks)))
    parkRightArrow.pack(pady = 10, side=LEFT, padx=50)

    addParkBtn = Button(window, 
             text ="Add a Park", 
             command = addParkPage)
    addParkBtn.pack(pady = 0, side=BOTTOM, anchor=SE)

def shiftUp(shift, parkNum):
    if shift < parkNum-1:
        shift+=1
    else:
        shift=0
    mainPage(shift)
    
def shiftDown(shift, parkNum):
    if shift >=1:
        shift-=1
    else:
        shift=parkNum-1
    mainPage(shift)

def parkPage(park, shift):
    clear()
    backBtn = Button(window, 
             text ="Back", 
             command = lambda:mainPage(0))
    backBtn.pack(pady = 0, anchor=NE)

    reviews=[]
    file=open("txts/review-service.txt", 'w', encoding="utf-8")
    file.write("r;"+park[0])
    file.close()

    while len(reviews)<=0:
        file = open("txts/review-service.txt", 'r', encoding="utf-8")
        input=file.readline()
        check=input.split(";")
        if check[0]=="RR":
            for line in file:
                if line=="RR" or "":
                    continue
                else:
                    reviews.append(line.split(";"))
            file.close()
            file = open("txts/review-service.txt", 'w', encoding="utf-8")
            file.close()

    ratings=0
    tags=[]
    pictures=[]
    for review in reviews:
        ratings+=float(review[0])
        tag=review[2].split(',')
        for t in tag:
            if t not in tags:
                tags.append(t)
        pics=review[3].split(',')
        for pic in pics:
            if pic not in pics:
                pictures.append(pic)
    
    ratings=ratings/len(reviews)

    tagString="Tags: "
    for tag in tags:
        tagString+=tag+", "

    nameLabel = Label(window, 
              text =park[0])
    nameLabel.pack(pady=10)
    locationLabel = Label(window, 
              text =park[1])
    locationLabel.pack(pady=10)

    ratingLabel = Label(window, text= str(ratings))
    ratingLabel.pack(pady=10)

    tagsLabel = Label(window, 
              text = tagString)
    tagsLabel.pack(pady = 10)


    reviewsLabel = Label(window, 
              text = reviews[random.randint(0,len(reviews)-1)][1])
    reviewsLabel.pack(pady = 10)

    reviewBtn = Button(window, 
             text ="Add a Review", 
             command = lambda:reviewPage(park))
    reviewBtn.pack(pady = 0, side=BOTTOM, anchor=SE)

def reviewPage(park):
    clear()
    backBtn = Button(window, 
             text ="Back/Cancel", 
             command = lambda:parkPage(park, 0))
    backBtn.pack(pady = 0, anchor=NE)

    thankYouLabel = Label(window, 
              text ="Thank you for Reviewing "+park[0]+"! You may add as much or as little information as you would like")
    thankYouLabel.pack(pady=10)

    ratingLabel = Label(window, 
              text ="Rating out of 5:")
    ratingLabel.pack(pady = 10)
    ratingText= Text(window, height=1, width=20)
    ratingText.pack()

    reviewLabel = Label(window, 
              text ="Review:")
    reviewLabel.pack(pady = 10)
    reviewText= Text(window, height=1, width=20)
    reviewText.pack()

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

    deleteLabel = Label(window, 
              text ="Your review can be deleted from the user info page.")

    submitBtn = Button(window, 
             text ="Submit", 
             command = lambda:submitReview(park, ratingText.get("1.0", "end-1c"), reviewText.get("1.0", "end-1c"), 
                                           tagsText.get("1.0", "end-1c"), picText.get("1.0", "end-1c")))
    submitBtn.pack(pady = 0, side=BOTTOM, anchor=S)
    deleteLabel.pack(pady = 10, side=BOTTOM, anchor=SW)

def submitReview(park, rating, review, tags, picURL):
    file = open("txts/review-service.txt", 'w', encoding="utf-8")
    file.write("w;"+park[0]+";"+rating+";"+review+";"+tags+";"+picURL)
    file.close()
    parkPage(park, 0)

def userPage():
    clear()
    backBtn = Button(window, 
             text ="Back", 
             command = lambda:mainPage(0))
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
             text ="Back/Cancel", 
             command = lambda:mainPage(0))
    backBtn.pack(pady = 0, anchor=NE)

    thankYouLabel = Label(window, 
              text ="Thank you for Adding a Park!")
    thankYouLabel.pack(pady=10)

    nameLabel = Label(window, 
              text ="Park Name:")
    nameLabel.pack(pady = 10)
    nameText= Text(window, height=1, width=20)
    nameText.pack()

    locationLabel = Label(window, 
              text ="Location:")
    locationLabel.pack(pady = 10)
    locationText= Text(window, height=1, width=20)
    locationText.pack()

    picLabel = Label(window, 
              text ="Picture URL:")
    picLabel.pack(pady = 10)
    picText= Text(window, height=1, width=20)
    picText.pack()

    submitBtn = Button(window, 
             text ="Add Park", 
             command = lambda:submitPark(nameText.get("1.0", "end-1c"), locationText.get("1.0", "end-1c"), picText.get("1.0", "end-1c")))
    submitBtn.pack(pady = 0,side=BOTTOM, anchor=S)

    deleteLabel = Label(window, 
              text ="Your Park can be deleted from the user info page.")
    deleteLabel.pack(pady=10, side=BOTTOM, anchor=SW)

def submitPark(nameText, locationText, picText):
    file = open("txts/park-service.txt", 'w', encoding="utf-8")
    file.write("w,"+nameText+","+locationText+","+picText)
    file.close()
    mainPage(0)
    

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
             command = lambda:mainPage(0))
    loginBtn.pack(pady = 10)
    createAccountBtn = Button(window, 
             text ="Create an Account", 
             command = lambda:mainPage(0))
    createAccountBtn.pack(pady = 10)

    
    accountFeatureLabel = Label(window, 
              text ="Create an account to track your visited parks or review and add new ones!")
    accountFeatureLabel.pack(pady=10)
    guestBtn = Button(window, 
             text ="Continue as Guest", 
             command = lambda:mainPage(0))
    guestBtn.pack(pady = 90)
    
 
# mainloop, runs infinitely
loginPage()
mainloop()