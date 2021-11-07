import sys
from tabulate import tabulate

inUrl = None
apexUrl = "App:Page:Session:Request:Debug:ClearCache:itemNames:itemValues:PrinterFriendly"

print("Formato de una url en Apex:")
print("f?p={}".format(apexUrl))
if(not inUrl):
    if (len(sys.argv) > 1):
        inUrl = sys.argv[1]
    else:
        inUrl = input("\nIngrese la url Apex:\n")

print("Url ingresada:", inUrl)
inUrlArr = inUrl[inUrl.find("f?p=") + 4 :].split(":")
apexUrlArr = apexUrl.split(":")

print()
printArr = []

for i in range(len(apexUrlArr)):
    printArr.append([apexUrlArr[i], inUrlArr[i]])

print(tabulate(printArr,["Identificadores", "Valores"], tablefmt="psql"))

itemNamesIndex = apexUrlArr.index("itemNames")
itemValuesIndex = apexUrlArr.index("itemValues")
itemNamesArr = inUrlArr[itemNamesIndex].split(",")
itemValuesArr = inUrlArr[itemValuesIndex].split(",")

print()
printArr = []
for i in range(len(itemNamesArr)):
    printArr.append([itemNamesArr[i], itemValuesArr[i]])

print(tabulate(printArr,["itemNames", "itemValues"], tablefmt="psql"))


#f?p=App:Page:Session:Request:Debug:ClearCache:itemNames:itemValues:PrinterFriendly
#http://192.168.0.218:8080/ords/f?p=101:318:9496897411448:::318:P318_PAGEID,P318_IDPACIENTE,P318_IDENCO:296,8253741,1400:
