filename = "Androsensor.csv"
filehandler =  open(filename,"r")
count = 0
bigstr = ""
for line in filehandler:
    if count>=0:
        sploot = line.split(",")
        temp = []
        for num in [22,23,27,29,32]:
                temp.append(sploot[num])
        tempstr = ""
        for num in temp:
            tempstr = tempstr + num + ","
        tempstr = tempstr[:-1]
        bigstr = bigstr + tempstr
    count += 1
#bigstr = "sep=;\n" + bigstr
filehandler.close()
filehandler = open("new.csv","w")
filehandler.write(bigstr)
filehandler.close()

