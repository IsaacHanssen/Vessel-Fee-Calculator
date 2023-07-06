# Functions
from JettyFees import Spacer
import math
from datetime import datetime
from dateutil import relativedelta


def timeBetweenDates(date1,date2): # dates in format dd/mm/yy
    start_date = datetime.strptime(date1, "%d/%m/%Y")
    end_date = datetime.strptime(date2, "%d/%m/%Y")
    delta = relativedelta.relativedelta(end_date, start_date)
    return (delta.days, delta.months, delta.years)

def round_nearest(x, a):
    max_frac_digits = 100
    for i in range(max_frac_digits):
        if round(a, -int(math.floor(math.log10(a)))+ i) == a:
            frac_digits = -int(math.floor(math.log10(a))) + i
            break
    return round(round(x / a) * a, frac_digits)

def areaList():
    return ["Albany (Emu Pont)","Albany Waterfront Marina","Augusta Boat Harbour"]

def areaAsk():
    Spacer()
    arealist = areaList()
    print("Pick the location of your desired vessel accommodation:")
    for i in range(len(arealist)):
        print(f"{i+1}) {arealist[i]}")
    area = int(input("What area are you looking to accommodate in? (Type 1, 2...) "))
    Spacer()
    print(f"You picked {arealist[area-1]}")
    Spacer()
    return arealist[area-1]

def timeAsk():
    Spacer()
    date1 = input("What date do you want to accommodate your vessel? (dd/mm/yyyy) ")
    date2 = input("What date do you want to leave the accommodation? (dd/mm/yyyy) ")
    Spacer()
    timedifference = timeBetweenDates(date1, date2)
    x, y, z = timeBetweenDates(date1, date2)
    print(f"That will be {x} days, {y} months and {z} years.")
    return timedifference

def priceCalculation2(week, month, threeMonth, year, days, months, years, length, overwidthMultiplier, penType):
    if years > 0:
        return year[penType]*length*overwidthMultiplier
    elif months > 2:
        return threeMonth[penType]*(months + days / 30)*length*overwidthMultiplier
    elif months > 0:
        return month[penType]*(months + days / 30)*length*overwidthMultiplier
    elif days > 0:
        return week[penType]*(days/7)*length*overwidthMultiplier



def lengthVessel():
    return int(input("How long is your vessel? (meters) "))

def overWidth():
    a = input("Is your vessel over width? y/n ")
    Spacer()
    if a == "y":
        print("1) Using a specified CAT pen")
        print("2) Vessel requires two standard pens")
        print("3) Still fits into a single pen")
        b = int(input("What scenario does your vessel fit into? "))
        Spacer()
        if b == 1:
            return 1.5
        if b == 2:
            return 2
        if b == 3:
            return 1
    else:
        return 1

def priceCalculation(week, month, threeMonth, year, length, time, type, overwidthMultiplier, penType):
    if type == 0:
        return week[penType]*time*length*overwidthMultiplier
    elif type == 1 and time < 3:
        return month[penType]*time*length*overwidthMultiplier
    elif type == 1 and time >= 3 and time < 12:
        return threeMonth[penType]*time*length*overwidthMultiplier     
    elif type == 1 and time == 12:
        return year[penType]*length*overwidthMultiplier

# Sites
def albanyEmuPoint(length, days, months, years): # Fixed Pen Without Walkway, Fixed Alongside Berth
    week = [17.75,21.40]
    month = [59.2, 71.3]
    threeMonth = [36,43.35]
    year = [394.55,475.2]
    Spacer()
    print("1) Fixed Pen Without Walkway")
    print("2) Fixed Pen Alongside Berth")
    penType = int(input("Which is your pen type? (1, 2... etc) "))-1
    Spacer()
    overwidthMultiplier = overWidth()
    return priceCalculation2(week, month, threeMonth, year, days, months, years, length, overwidthMultiplier, penType)      

def albanyWaterFront(length, days, months, years): # Fixed Pen Without Walkway, Fixed Alongside Berth
    week = [31.3,31.3,25.05]
    month = [104.4,104.4,83.5]
    threeMonth = [63.5,63.5,50.8]
    year = [696,696,556.8]
    Spacer() 
    print("1) Floating Pen with Walkway")
    print("2) Floating Alongside Berth")
    print("3) Fixed Alongside Berth")
    penType = int(input("Which is your pen type? (1, 2... etc) "))-1
    Spacer()
    overwidthMultiplier = overWidth()
    return priceCalculation2(week, month, threeMonth, year, days, months, years, length, overwidthMultiplier, penType) 

def augustaBoatHarbour(length, days, months, years): # Fixed Pen Without Walkway, Fixed Alongside Berth
    week = [31.3,31.3]
    month = [104.4, 104.4]
    threeMonth = [63.5,63.5]
    year = [696,696]
    Spacer()
    print("1) Fixed Pen With Walkway")
    print("2) Floating Alongside Berth")
    penType = int(input("Which is your pen type? (1, 2... etc) "))-1
    Spacer()
    overwidthMultiplier = overWidth()
    return priceCalculation2(week, month, threeMonth, year, days, months, years, length, overwidthMultiplier, penType)

def VesselAccomodationFee():
    # Find main variables
    area = areaAsk()
    length = lengthVessel()
    days, months, years = timeAsk()

    areas = areaList()
    if area == areas[0]:
        a = albanyEmuPoint(length, days, months, years)
    if area == areas[1]:
        a = albanyWaterFront(length, days, months, years)
    if area == areas[2]:
        a = augustaBoatHarbour(length, days, months, years)
        
    print(f"That will cost you ${round_nearest(a,0.05)} to accommodate your vessel.")
    return a