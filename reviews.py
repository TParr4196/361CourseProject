while True:
    file = open("txts/review-service.txt", 'r', encoding="utf-8")
    input = file.readline()
    check = input.split(";")
    if check[0] != '' and check[0] != 'RR,':
        file.close
        if check[0] == 'w':
            print("wrote review")
            file = open("txts/reviews.txt", 'a', encoding="utf-8")
            file.write("\n"+check[1]+";"+check[2]+";"+check[3]+";"+check[4]+";"+check[5])
            file.close()
            file = open("txts/review-service.txt", 'w', encoding="utf-8")
        if check[0] == 'r':
            file = open("txts/reviews.txt", 'r', encoding="utf-8")
            reviews = []
            for line in file:
                reviews.append(line.split(";"))
            file.close()
            file = open("txts/review-service.txt", 'w', encoding="utf-8")
            output = "RR;\n"
            file.write(output)
            for review in reviews:
                if review[0]==check[1]:
                    review[4]=review[4].split("\n")[0]
                    nextLine=(review[1]+";"+review[2]+";"+review[3]+";"+review[4]+"\n")
                    file.write(nextLine)
                    output+=nextLine
            if output == "RR;\n":
                output+="0;No Reviews yet;none;nonpic\n"
                file.write("0;No Reviews yet;none;nonpic\n")
            print("Read parks: \n"+output)

    file.close