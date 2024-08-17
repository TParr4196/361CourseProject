import time

while True:
    file = open("txts/users-service.txt", 'r', encoding="utf-8")
    input = file.readline()
    check = input.split("|")
    if check[0] != '' and check[0] != 'RR':
        file.close
        #write a new user
        if check[0] == 'w':
            print("wrote new user")
            file = open("txts/users.txt", 'a', encoding="utf-8")
            file.write(check[1]+"|"+check[2]+"\n")
            file.close()
            file = open("txts/users-service.txt", 'w', encoding="utf-8")
            file.write("RR|wrote")

        #login a user
        if check[0] == 'l':
            file = open("txts/users.txt", 'r', encoding="utf-8")
            users = []
            for line in file:
                users.append(line.split("|"))
            file.close()
            file = open("txts/users-service.txt", 'w', encoding="utf-8")
            output="RR|NotFound"
            for user in users:
                user[1]=user[1].split("\n")[0]
                if user[0]==check[1]:
                    if user[1]==check[2]:
                        print("user verified")
                        # Citation for the following join() syntax:
                    # Date: 08/16/24
                    # Copied from:
                    # https://www.digitalocean.com/community/tutorials/python-join-list
                        output="RR|Found|Verified|"+"|".join(user)
                        break
                    else:
                        print("user not verified")
                        output="RR|Found|NotVerified|"+"|".join(user)
                        break
            if output=="RR|NotFound":
                print("user not found")
            file.write(output)

        #add information to a user
        if check[0]=='a':
            file = open("txts/users.txt", 'r', encoding="utf-8")
            users = []
            for line in file:
                users.append(line.split("|"))
            file.close()
            file = open("txts/users.txt", 'w', encoding="utf-8")
            userStrings=[]
            found = False
            for user in users:
                if user[0]==check[1]:
                    user.append(check[2]+"\n")
                    found = True
                    user[len(user)-2]=user[len(user)-2].split("\n")[0]
                # Citation for the following join() syntax:
                # Date: 08/16/24
                # Copied from:
                # https://www.digitalocean.com/community/tutorials/python-join-list
                userStrings.append("|".join(user))
            # Citation for the following writelines() function:
            # Date: 08/16/24
            file.writelines(userStrings)
            file.close()

            file = open("txts/users-service.txt", 'w', encoding="utf-8")
            if not found:
                print("user not found")
                file.write("RR|NotFound")
            else:
                print("appended "+check[2]+" to user "+check[1])
                file.write("RR|Appended|"+check[1]+"|"+check[2])

        #delete information from a user
        if check[0]=='d':
            file = open("txts/users.txt", 'r', encoding="utf-8")
            users = []
            for line in file:
                users.append(line.split("|"))
            file.close()
            file = open("txts/users.txt", 'w', encoding="utf-8")
            userStrings=[]
            found = False
            for user in users:
                if user[0]==check[1]:
                    for s in user:
                        if s==check[2]:
                            user.remove(s)
                            found = True
                            
                    user[len(user)-1]=user[len(user)-1].split("\n")[0]+"\n"
                    user[len(user)-2]=user[len(user)-2].split("\n")[0]
                # Citation for the following join() syntax:
                # Date: 08/16/24
                # Copied from:
                # https://www.digitalocean.com/community/tutorials/python-join-list
                userStrings.append("|".join(user))
            # Citation for the following writelines() function:
            # Date: 08/16/24
            file.writelines(userStrings)
            file.close()

            file = open("txts/users-service.txt", 'w', encoding="utf-8")
            if not found:
                print("information to delete not found")
                file.write("RR|NotFound")
            else:
                print("deleted "+check[2]+" from user "+check[1])
                file.write("RR|Deleted|"+check[1]+"|"+check[2])

        #delete a user
        if check[0]=='dd':
            file = open("txts/users.txt", 'r', encoding="utf-8")
            users = []
            for line in file:
                users.append(line.split("|"))
            file.close()

            file = open("txts/users.txt", 'w', encoding="utf-8")
            found = False
            for user in users:
                if user[0]==check[1]:
                    users.remove(user)
                    print("Deleted user")
                    found = True
                    break
            
            userStrings = []
            for user in users:
                # Citation for the following join() syntax:
                # Date: 08/16/24
                # Copied from:
                # https://www.digitalocean.com/community/tutorials/python-join-list
                userStrings.append("|".join(user))

            # Citation for the following writelines() function:
            # Date: 08/16/24
            # adapted from:
            # https://www.w3schools.com/python/ref_file_writelines.asp
            file.writelines(userStrings)
            file.close()
            
            file = open("txts/users-service.txt", 'w', encoding="utf-8")

            if not found:
                print("user not found")
                file.write("RR|NotFound")
            else:
                print("deleted user "+check[1])
                file.write("RR|Deleted|"+check[1])

    # Citation for the following flush() function:
    # Date: 08/15/24
    # Copied from:
    # https://www.geeksforgeeks.org/file-flush-method-in-python/
    file.flush()
    time.sleep(0.2)
    file.close()