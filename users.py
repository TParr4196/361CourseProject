import time

while True:
    file = open("txts/users-service.txt", 'r', encoding="utf-8")
    input = file.readline()
    check = input.split("|")
    if check[0] != '' and check[0] != 'RR':
        file.close
        if check[0] == 'w':
            print("wrote new user")
            file = open("txts/users.txt", 'a', encoding="utf-8")
            file.write(check[1]+"|"+check[2]+"\n")
            file.close()
            file = open("txts/users-service.txt", 'w', encoding="utf-8")
            file.write("RR|wrote")
        if check[0] == 'n':
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
                        output="RR|Found|Verified"
                        break
                    else:
                        print("user not verified")
                        output="RR|Found|NotVerified"
                        break
            if output=="RR|NotFound":
                print("user not found")
            file.write(output)
    file.flush()
    time.sleep(0.2)
    file.close()