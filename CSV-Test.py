import csv

d= []
with open(r"C:\tgw\visualproject\tia exporter\UDTKonverter\UDTKonverter\UDTKonverter\bin\Debug\net8.0-windows\Buffer.csv") as csvfile:
    allezeilen = csv.reader(csvfile,delimiter=';',quotechar='"')
    for row in allezeilen:
        tempstring = row[0]
        split = tempstring.split("_")
        modtyp = split[1]
        if int(modtyp) > 1399:
            print(modtyp)

