import time
import random

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
           item[2]," "*(7-len(str(item[2]))),"|",)
print (color.END)


apb5 = 7.40
cpb5 = 5.40
stpb5 = 5.90
spb5 = 5.90
fpb5 = 22.60

apa5 = 8.90
cpa5 = 6.40
stpa5 = 6.90
spa5 = 6.90
fpa5 = 27.60

tuesday_p = 5.40

days = ["monday", "tuesday", "wednesday","thursday","friday","saturday","sunday"]

day = ""

while day not in days:
    day = input("What day would you like to watch the movie?")
    day = day.lower()
    print ("Invalid Input!")

print ("")
print ("At what time do you want to watch the movie?")
print ("")
print ("You have the options of:")
print ("- Morning")
print ("- Afternoon")
print ("- Evening")
print ("- Nightowl")
print ("")
print ("PLEASE INPUT YOUR ANSWER ALL IN LOWERCASE LETTERS OTHERWISE THE SYSTEM WOULD NOT WORK PROPERLY!")

chosen_time = input()
global hour
global minute
  
while chosen_time != "morning" or "afternoon" or "evening" or "nightowl":
    
    if chosen_time == "morning":
        hour = random.randrange(6,11)
        minute = random.randrange(0,55, 5)
        break
    elif chosen_time == "afternoon":
        hour = random.randrange(12,16)
        minute = random.randrange(0,55, 5)
        break
    elif chosen_time =="evening":
        hour = random.randrange(17,22)
        minute = random.randrange(0,55, 5) 
        break
    elif chosen_time == "nightowl":
        hour = random.randrange(0,5) or 23
        minute = random.randrange(0,55, 5)
        break
    else:
        print ("Invalid Input! Type it again!")
        chosen_time = input()


