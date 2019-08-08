def stopwords():
    stop = []
    with open("../datapreprocessing/stopwords-bn.txt", "r") as ins:
        for line in ins:
            stop.append(line.strip('\n'))
    #print(stop)
    return stop