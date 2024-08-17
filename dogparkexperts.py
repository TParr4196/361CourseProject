# Citation for creation of a window and button in python:
# Date: 7/29/2024
# Adapted from:
# https://www.geeksforgeeks.org/open-a-new-window-with-a-button-in-python-tkinter/
from tkinter import *
from tkinter.ttk import *
import time

# creates a Tk() object
window = Tk()
 
# sets the geometry of main 
# root window
window.geometry("750x500")
window.title("Dog Park Experts")

import random

def mainPage(shift, user):
    clear()
    userInfoBtn = Button(window, 
             text ="Track your User Info", 
             command = lambda: userPage(user))
    
    # citation for the follow anchor syntax:
    # Date: 08/01/24
    # Adapted from:
    # https://stackoverflow.com/questions/58016467/how-to-make-tkinterpack-place-label-on-top-left-corner-in-below-program
    userInfoBtn.pack(pady=0, anchor=NE)

    logoutBtn = Button(window, 
             text ="Log out", 
             command = loginPage)
    logoutBtn.pack(pady = 0,anchor=NE)

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
             command = lambda: shiftDown(shift, len(parks), user))
    parkLeftArrow.pack(pady = 10, side=LEFT, padx= 50)

    parkBtnOne = Button(window, 
             text = parks[shift][0], 
             command = lambda: parkPage(parks[shift], 0, user))
    parkBtnOne.pack(pady = 10, side=LEFT)
    parkBtnTwo = Button(window, 
             text = parks[(shift+1)%len(parks)][0], 
             command = lambda: parkPage(parks[(shift+1)%len(parks)], 0, user))
    parkBtnTwo.pack(pady = 10, side=LEFT)
    parkBtnThree = Button(window, 
             text = parks[(shift+2)%len(parks)][0], 
             command = lambda: parkPage(parks[(shift+2)%len(parks)], 0, user))
    parkBtnThree.pack(pady = 10, side=LEFT)

    parkRightArrow = Button(window, 
             text ="->", 
             command = lambda: shiftUp(shift, len(parks), user))
    parkRightArrow.pack(pady = 10, side=LEFT, padx=50)

    addParkBtn = Button(window, 
             text ="Add a Park", 
             command = lambda: addParkPage(user))
    addParkBtn.pack(pady = 0, side=BOTTOM, anchor=SE)

def shiftUp(shift, parkNum, user):
    if shift < parkNum-1:
        shift+=1
    else:
        shift=0
    mainPage(shift, user)
    
def shiftDown(shift, parkNum, user):
    if shift >=1:
        shift-=1
    else:
        shift=parkNum-1
    mainPage(shift, user)

def parkPage(park, shift, user):
    clear()
    backBtn = Button(window, 
             text ="Back", 
             command = lambda:mainPage(0, user))
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
             command = lambda:reviewPage(park, user))
    reviewBtn.pack(pady = 0, side=BOTTOM, anchor=SE)

def reviewPage(park, user):
    clear()
    backBtn = Button(window, 
             text ="Back/Cancel", 
             command = lambda:parkPage(park, 0, user))
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
                                           tagsText.get("1.0", "end-1c"), picText.get("1.0", "end-1c"), user))
    submitBtn.pack(pady = 0, side=BOTTOM, anchor=S)
    deleteLabel.pack(pady = 10, side=BOTTOM, anchor=SW)

def submitReviewFinal(park, rating, review, tags, picURL, user):
    file = open("txts/review-service.txt", 'w', encoding="utf-8")
    file.write("w;"+park[0]+";"+rating+";"+review+";"+tags+";"+picURL)
    file.flush()
    time.sleep(0.5)
    file.close()
    file = open("txts/users-service.txt", 'w', encoding="utf-8")
    file.flush()
    time.sleep(0.5)
    file.write("a|"+user+"|"+"review:"+park[0]+";"+rating+";"+review+";"+tags+";"+picURL)
    file.close()
    parkPage(park, 0, user)

def submitReview(park, rating, review, tags, picURL, user):
    clear()
    message=Label(window, text ="Are you sure you wish to submit your review?").pack(side=TOP)
    yesBtn = Button(window, text="Yes", command=lambda:submitReviewFinal(park, rating, review, tags, picURL, user)).pack(padx=200,side=LEFT)
    noBtn = Button(window, text="No", command=lambda:reviewPage(park, user)).pack(side=LEFT)

def userPage(user):
    clear()
    backBtn = Button(window, 
             text ="Back", 
             command = lambda:mainPage(0, user))
    backBtn.pack(pady = 0, anchor=NE)

    usernameLabel = Label(window, 
              text ="Welcome "+user+"! Click a review or park to delete it.")
    usernameLabel.pack(pady=10)

    file=open("txts/servicea.txt", 'r', encoding="utf-8")
    reminder=file.readline()
    file.close()
    print(reminder)
    if reminder == '' or reminder=='\n':
        serviceaBtn= Button(window, 
             text ="Click here to set a vaccination reminder!", 
             command = lambda:service(user))
        serviceaBtn.pack(pady = 10)
    else:
        serviceaBtn= Button(window, 
             text = reminder, 
             command = lambda:service(user))
        serviceaBtn.pack(pady = 10)

    file = open("txts/users-service.txt", 'w', encoding="utf-8")
    file.write("l|"+user+"|inforequest")
    userInfo = ["empty"]
    file.flush()
    time.sleep(0.5)
    while userInfo[0]=="empty":
        file = open("txts/users-service.txt", 'r', encoding="utf-8")
        userInfo=file.readline().split("|")
        if userInfo[0]=='RR':
            print(userInfo)

    parks=[]
    reviews=[]
    if len(userInfo)>5:
        for i in range(5, len(userInfo)):
            split = userInfo[i].split(":")
            if split[0]=="park":
                parks.append(split[1])
            if split[0]=="review":
                reviews.append(split[1])
    yourParksLabel = Label(window, 
              text ="Your Parks:")
    yourParksLabel.pack(pady=10)

    if len(parks)>0:
        for i in range(len(parks)):
            parkButton = Button(window,
                text=parks[i].split(",")[0],
                
                # Citation for the following lambda tkinter syntax:
                # Date 08/16/24
                # Adapted from:
                # https://stackoverflow.com/questions/4236182/generate-tkinter-buttons-dynamically
                command=lambda j=i:deleteParkOrReview(parks[j], user, True))
            parkButton.pack(pady=0)

    reviewLabel = Label(window, 
              text ="Your Reviews:")
    reviewLabel.pack(pady=10)

    if len(reviews)>0:
        for i in range(len(reviews)):
            reviewButton = Button(window,
                text=reviews[i].split(",")[0],
                
                # Citation for the following lambda tkinter syntax:
                # Date 08/16/24
                # Adapted from:
                # https://stackoverflow.com/questions/4236182/generate-tkinter-buttons-dynamically
                command=lambda j=i:deleteParkOrReview(reviews[j], user, False))
            reviewButton.pack(pady=0)

    accountInfoLabel = Label(window, 
              text ="This information will be saved even after you log out!")
    accountInfoLabel.pack(pady=10)

    deleteAccountBtn = Button(window, 
             text ="Delete Account", 
             command = lambda: deleteAccount(user, parks, reviews))
    deleteAccountBtn.pack(pady = 0, side=BOTTOM, anchor=SE)

def service(user):
    file=open("txts/servicea.txt", 'w', encoding="utf-8")
    file.write(user)
    file.flush()
    time.sleep(0.2)
    file.close()
    readresponse=user
    while readresponse==user:
        file=open("txts/servicea.txt", 'r', encoding="utf-8")
        print(readresponse)
        readresponse=file.readline()
    userPage(user)

def deleteParkOrReview(info, user, bool):
    clear()
    message=Label(window, text ="Are you sure you wish to delete?").pack(side=TOP)
    yesBtn = Button(window, text="Yes", command=lambda:deleteFinal(info, user, bool)).pack(padx=200,side=LEFT)
    noBtn = Button(window, text="No", command=lambda:userPage(user)).pack(side=LEFT)

def deleteFinal(info, user, bool):
    file = open("txts/users-service.txt", 'w', encoding="utf-8")
    if bool:
        file.write("d|"+user+"|"+"park:"+info)
        file.flush()
        time.sleep(0.2)
        file.close()
        file=open("txts/park-service.txt", 'w', encoding="utf-8")
        file.write("dd,"+info)
    else:
        file.write("d|"+user+"|"+"review:"+info)
        file.flush()
        time.sleep(0.2)
        file.close()
        file=open("txts/review-service.txt", 'w', encoding="utf-8")
        file.write("dd;"+info)
    file.flush()
    time.sleep(0.2)
    file.close()
    userPage(user)  

def deleteAccount(user, parks, reviews):
    clear()
    message=Label(window, text ="Are you sure you wish to delete your account?").pack(side=TOP)
    yesBtn = Button(window, text="Yes", command=lambda:deleteAccFinal(user, parks, reviews)).pack(padx=200,side=LEFT)
    noBtn = Button(window, text="No", command=lambda:userPage(user)).pack(side=LEFT)
    
def deleteAccFinal(user, parks, reviews):
    for park in parks:
        file=open("txts/park-service.txt", 'w', encoding="utf-8")
        file.write("dd,"+park)
        file.flush()
        time.sleep(0.2)
        file.close()

    for review in reviews:
        file=open("txts/review-service.txt", 'w', encoding="utf-8")
        file.write("dd;"+review)
        file.flush()
        time.sleep(0.2)
        file.close()

    file = open("txts/users-service.txt", 'w', encoding="utf-8")
    file.write("dd|"+user)
    file.flush()
    time.sleep(0.2)

    loginPage()

def addParkPage(user):
    clear()
    backBtn = Button(window, 
             text ="Back/Cancel", 
             command = lambda:mainPage(0, user))
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
             command = lambda:submitPark(nameText.get("1.0", "end-1c"), locationText.get("1.0", "end-1c"), picText.get("1.0", "end-1c"), user))
    submitBtn.pack(pady = 0,side=BOTTOM, anchor=S)

    deleteLabel = Label(window, 
              text ="Your Park can be deleted from the user info page.")
    deleteLabel.pack(pady=10, side=BOTTOM, anchor=SW)

def submitParkFinal(nameText, locationText, picText, user):
    file = open("txts/park-service.txt", 'w', encoding="utf-8")
    file.write("w,"+nameText+","+locationText+","+picText)
    file.flush()
    time.sleep(1)
    file.close()
    file = open("txts/users-service.txt", 'w', encoding="utf-8")
    file.write("a|"+user+"|"+"park:"+nameText+","+locationText+","+picText)
    file.flush()
    time.sleep(0.2)
    file.close()
    mainPage(0, user)

def submitPark(nameText, locationText, picText, user):
    clear()
    message=Label(window, text ="Are you sure you wish to submit your park?").pack(side=TOP)
    yesBtn = Button(window, text="Yes", command=lambda:submitParkFinal(nameText, locationText, picText, user)).pack(padx=200,side=LEFT)
    noBtn = Button(window, text="No", command=lambda:mainPage(0, user)).pack(side=LEFT)

# citation for the following function:
# Date: 07/31/24
# copied from:
# https://stackoverflow.com/questions/15781802/python-tkinter-clearing-a-frame
def clear():
    for widget in window.winfo_children():
        widget.destroy()
 
def loginPage():
    clear()
    # Citation for the following global python syntax:
    # Date: 08/16/24
    # Copied from:
    # https://www.w3schools.com/python/python_variables_global.asp

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
             command = lambda:login(userText.get("1.0", "end-1c"), passText.get("1.0", "end-1c")))
    loginBtn.pack(pady = 10)
    createAccountBtn = Button(window, 
             text ="Create an Account", 
             command = lambda:createAccount(userText.get("1.0", "end-1c"), passText.get("1.0", "end-1c")))
    createAccountBtn.pack(pady = 10)

    
    accountFeatureLabel = Label(window, 
              text ="Create an account to track your visited parks or review and add new ones!")
    accountFeatureLabel.pack(pady=10)
    guestBtn = Button(window, 
             text ="Continue as Guest", 
             command = lambda:mainPage(0, "Guest"))
    guestBtn.pack(pady = 90)

def login(usern, password):
    file = open("txts/users-service.txt", 'w', encoding="utf-8")
    file.write("l|"+usern+"|"+password)
    file.close()
    user = "Guest"
    while user=="Guest":
        file = open("txts/users-service.txt", 'r', encoding="utf-8")
        input=file.readline()
        time.sleep(0.5)
        check=input.split("|")
        if check[0]=="RR":
            if check[2]=="Verified":
                user=usern
            file.close()
            file = open("txts/users-service.txt", 'w', encoding="utf-8")
            file.close()
    mainPage(0, user)

def createAccount(usern, password):
    file = open("txts/users-service.txt", 'w', encoding="utf-8")
    file.write("w|"+usern+"|"+password)
    file.close()
    user = "Guest"
    while user=="Guest":
        file = open("txts/users-service.txt", 'r', encoding="utf-8")
        input=file.readline()
        time.sleep(0.5)
        check=input.split("|")
        if check[0]=="RR":
            if check[1]=="wrote":
                user=usern
            file.close()
            file = open("txts/users-service.txt", 'w', encoding="utf-8")
            file.close()
    mainPage(0, usern)
 
# mainloop, runs infinitely
loginPage()
mainloop()