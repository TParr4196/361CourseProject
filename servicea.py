import tkinter as tk
from tkinter import simpledialog
import time

user_alert = []
while True:
    file = open("txts/servicea.txt", 'r')
    users = file.readline()
    if users is not None and users!='' and users!="\n" and users.split(":")[0]!="Do Not Forget to Schedule your Pets vaccination by the following date":
        file.close()
        root = tk.Tk()
        root.withdraw()

        user_input = simpledialog.askstring("Input", "When is your pet due for their next vaccines?")
        file = open("txts/servicea.txt", 'w')
        file.write("Do Not Forget to Schedule your Pets vaccination by the following date:")
        file.write(user_input)
        file.close()
        print("Reminder schedule your pet for their next vaccinations before:", user_input)

        root.quit()
    else:
        file.close()
        time.sleep(0.5)
        #print("There are no registered users yet, please register before setting your alert")