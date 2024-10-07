
import time
import random

class color:
    WHITE   = '\033[37m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[35m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


print ("Hello! Welcome to the Cinibi World online booking system!")
time.sleep(0.5)
print ("")
time.sleep(0.5)
print ("This cinema is open 24 hours a day, 7 days a week!")
print ("")
time.sleep(1)
print ("Therefore, you can watch absolutely ANY movie you want at ANY day and time!")
time.sleep(1)
print("")
print ("****************************************************")
print ('\033[1;4m'    +'         PRICES LIST FOR CINIBI CINEMA 2024         ' + '\033[0m')
print ("")

a = color.BOLD + color.UNDERLINE + color.GREEN + "Adults" + color.END + color.GREEN
c  = color.BOLD + color.UNDERLINE + color.PURPLE + "Children" + color.END + color.PURPLE
st = color.BOLD + color.UNDERLINE + color.BLUE + "Students" + color.END + color.BLUE
s = color.BOLD + color.UNDERLINE + color.DARKCYAN + "Seniors" + color.END + color.DARKCYAN
f = color.BOLD + color.UNDERLINE + color.MAGENTA + "Family" + color.END + color.MAGENTA
gap = color.BOLD + color.UNDERLINE + color.WHITE + "-------------" + color.END + color.WHITE
to = color.BOLD + color.UNDERLINE + color.YELLOW + "Tuesday Offer" + color.END + color.YELLOW

priceList = [
    [a, "£7.40", "£8.90"],
    [c, "£5.40", "£6.40"],
    [st, "£5.90", "£6.90"],
    [s, "£5.90", "£6.90"],
    [f, "£22.60", "£27.60"],
    [gap, "---------", "--------"],
    [to, "£5.40", "£5.40"]
]

# Column widths
col1_width = 35
col2_width = 11  # Adjusted width for prices
col3_width = 11  # Adjusted width for prices

# Header
print(color.BOLD, color.UNDERLINE, " " * 13, "|", "Before 5PM".center(col2_width), "|", "After 5PM".center(col3_width), "|", color.END)

# Centered content
for item in priceList:
    col1_text = item[0].center(col1_width)
    col2_text = item[1].center(col2_width)
    col3_text = item[2].center(col3_width)
    
    print("|", col1_text, "|", col2_text, "|", col3_text, "|")

print(color.END)


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

movie = input ("What movie would you like to watch? ")
movie = movie.title()

days = ["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday"]

day = ""

while day not in days:
    day = input("What day would you like to watch the movie?")
    day = day.lower()
    day = day.title()
    if day not in days:
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


adults = int(input("How many adult tickets?  "))
children = int(input("How many children tickets?  "))
students = int(input("How many student tickets? "))
seniors = int(input("How many senior tickets? "))
family = int(input("How many family tickets? "))

if day == "tuesday":
    offer = 5.40
    adult_price = round((adults * offer),2)
    child_price = round ((children * offer),2)
    student_price = round ((students * offer),2)
    senior_price = round ((seniors * offer),2)
    family_price = round ((family * offer),2)

if chosen_time == "morning" or "afternoon":
    adult_price = round((adults * apb5),2)
    child_price = round ((children * cpb5),2)
    student_price = round ((students * stpb5),2)
    senior_price = round ((seniors * spb5),2)
    family_price = round ((family * fpb5),2)

elif chosen_time == "evening" or "nightowl":
    adult_price = round ((adults * apb5),2)
    child_price = round ((children * cpb5),2)
    student_price = round ((students * stpb5),2)
    senior_price = round ((seniors * spb5),2)
    family_price = round ((family * fpb5),2)

print ("")
print ("Would you like parking?")
print ("It costs £2 extra...")
parking = input()
while parking != "yes" or "no":
    if parking == "yes":
      park_price = 2
      break
    elif parking == "no":
      park_price = 0
      break
    else:
      print ("That is not a valid answer! Type 'yes' or 'no'...")
      parking = input()

total_price = adult_price + child_price + student_price + senior_price + family_price + park_price
park_price = str(park_price)

total_price = round(total_price,2)
print ("Your total is: £", total_price)


hour = str(hour)
minute = str(minute)
timing = hour+":"+minute

prices = [child_price, adult_price, student_price, senior_price, family_price,total_price]
index = 0
while index < 6:
    prices[index] = str(prices[index])
    index = index + 1


people = [children, adults, students, seniors, family]
index2 = 0
while index2 < 5:
    people[index2] = str(people[index2])
    index2 = index2 + 1

screen = random.randint(1,10)
screen = str(screen)

gate = ["north", "west", "east", "south"]
entrance = random.choice(gate)
entrance = entrance.title()

movie_final = color.BOLD + color.UNDERLINE + color.YELLOW + "Chosen Movie" + color.END +color.YELLOW
day_final = color.BOLD + color.UNDERLINE + color.RED +"Chosen Day" + color.END + color.RED
time_final = color.BOLD + color.UNDERLINE + color.CYAN + "Chosen Time" + color.END + color.CYAN
blank1_final = color.BOLD + color.UNDERLINE + color.WHITE + "____________________" + color.END + color.WHITE
child_final = color.BOLD + color.UNDERLINE + color.PURPLE + "Child Total Price" + color.END + color.PURPLE
adult_final = color.BOLD + color.UNDERLINE + color.GREEN +"Adult Total Price" + color.END + color.GREEN
student_final = color.BOLD + color.UNDERLINE + color.BLUE + "Student Total Price" + color.END + color.BLUE
senior_final = color.BOLD + color.UNDERLINE + color.DARKCYAN + "Senior Total Price" + color.END + color.DARKCYAN
family_final = color.BOLD + color.UNDERLINE + color.MAGENTA + "Family Total Price" + color.END + color.MAGENTA
parking_final = color.BOLD + color.UNDERLINE + color.RED + "Parking Price" + color.END + color.RED
blank_final = color.BOLD + color.WHITE + color.WHITE + "--------------------" + color.END + color.WHITE
total_final = color.BOLD + color.UNDERLINE + color.WHITE +  "Total Price" + color.END + color.WHITE

column_width = 30
column_width2 = 10
column_width3 = 22
end = color.END

summary = [[movie_final.center(column_width), movie.center(column_width2), ("Screen " + screen).center(column_width3),color.END],
           [day_final.center(column_width), day.center(column_width2), " ".center(column_width3),color.END],
           [time_final.center(column_width), timing.center(column_width2), " ".center(column_width3),color.END],
           [blank1_final.center(column_width), "________".center(column_width2), "_____________________".center(column_width3)],
           [child_final.center(column_width), ("£" + prices[0]).center(column_width2), (people[0] + " x child(ren)").center(column_width3),color.END],
           [adult_final.center(column_width), ("£" + prices[1]).center(column_width2), (people[1] + " x adult(s)").center(column_width3),color.END],
           [student_final.center(column_width), ("£" + prices[2]).center(column_width2), (people[2] + " x student(s)").center(column_width3),color.END],
           [senior_final.center(column_width), ("£" + prices[3]).center(column_width2), (people[3] + " x senior(s)").center(column_width3),color.END],
           [family_final.center(column_width), ("£" + prices[4]).center(column_width2), (people[4] + " x family").center(column_width3),color.END],
           [blank1_final.center(column_width), "________".center(column_width2), "_____________________".center(column_width3)],
           [parking_final.center(column_width), ("£" + park_price).center(column_width2), ("Entry: " + entrance + " Entrance").center(column_width3),color.END],
           [blank_final.center(column_width), "------- ".center(column_width2), "---------------------".center(column_width3)],
           [total_final.center(column_width), ("£" + prices[5]).center(column_width2), " ".center(column_width3)]]

print ("*************************"+color.BOLD,color.UNDERLINE+"RECEIPT" + color.END +"************************")
print (color.UNDERLINE,"                                                          ",color.END)
for item in summary:
    print ("|", item[0]," "*(42-len(item[0])),"|",
           item[1]," "*(8-len(item[1])),"|",
           item[2]," "*(20-len(str(item[2]))),"|",)