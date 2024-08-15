import time

while True:
    file = open("txts/park-service.txt", 'r', encoding="utf-8")
    input = file.readline()
    check = input.split(",")
    if check[0] != '' and check[0] != 'RR,':
        file.close
        if check[0] == 'w':
            print("wrote park")
            file = open("txts/parks.txt", 'a', encoding="utf-8")
            file.write("\n"+check[1]+","+check[2]+","+check[3])
            file.close()
            file = open("txts/park-service.txt", 'w', encoding="utf-8")
        if check[0] == 'r':
            file = open("txts/parks.txt", 'r', encoding="utf-8")
            parks = []
            for line in file:
                parks.append(line.split(","))
            file.close()
            file = open("txts/park-service.txt", 'w', encoding="utf-8")
            output = "RR,\n"
            file.write(output)
            for park in parks:
                park[2]=park[2].split("\n")[0]
                nextLine=(park[0]+","+park[1]+","+park[2]+"\n")
                file.write(nextLine)
                output+=nextLine
            if output == "RR,\n":
                file.write(",,\n")
            print("Read parks")
    file.flush()
    time.sleep(0.2)
    file.close