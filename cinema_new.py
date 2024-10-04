import time

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    colors = [PURPLE,CYAN,DARKCYAN,BLUE,GREEN,YELLOW,RED]


print ("Hello! Welcome to the Cinebi World online booking system!")
time.sleep(0.5)
print ("")
time.sleep(0.5)
print ("This is a simple and easy system where you will recieve your virtual ticket in just under 2 minutes where you simply scan at the venue!")
print ("")
time.sleep(1)
print ("This cinema is open 24 hours a day, 7 days a week!")
print ("")
time.sleep(1)
print ("Therefore, you can watch absolutely ANY movie you want at ANY day and time!!")
time.sleep(1)
print("")
print ("****************************************************")
print ('\033[1;4m'    +'         PRICES LIST FOR CINIBI CINEMA 2024         ' + '\033[0m')
print ("")

priceList = [["Adults","£7.40","£8.90   "],
             ["Children","£5.40","£6.40   "],
             ["Students","£5.90","£6.90   "],
             ["Seniors","£5.90","£6.90   "],
             ["Family","£22.60","£27.60  "],
             ["","","  "],
             ["Tuesday Offer","£5.40","£5.40   "],]

print (color.BOLD,color.UNDERLINE,"                 |","Before 5PM | After 5PM |")
for item in priceList:
    print ("|", item[0]," "*(15-len(item[0])),"|",
           item[1]," "*(9-len(item[1])),"|",
           item[2]," "*(7-len(str(item[2]))),"|")
    
    