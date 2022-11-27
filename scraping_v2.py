import csv

source = 'C:/Users/amndr/Desktop/Prova/phone_reviews.csv'
dest = 'C:/Users/amndr/Desktop/Prova/Doc/'
with open (source, newline="", encoding="ISO-8859-1") as filecsv:
    while (csv.reader(filecsv, delimiter=",")) :
        letto = csv.reader(filecsv, delimiter=",")
        header = next(letto)
        fd = open(dest+"sm_"+header[0]+".txt", 'w')
        fd.write(header[1])
        fd.write(header[3])
        fd.write(header[4]+"\n")
        fd.write(header[5])
