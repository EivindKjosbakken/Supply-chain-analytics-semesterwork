import numpy as np

totDowntime = 0
hoursInDay = 8
numberOfDays = 100000000

for i in range(numberOfDays):
    timeOfFail = np.random.exponential(200)
    timeForRepair = np.random.exponential(8)
    if (timeOfFail >8): # fail doesnt happen within day
        continue
    if (timeForRepair > 8-timeOfFail): #if it fails, and we dont repair within the day
        totDowntime+= (8-timeOfFail)
        continue
        
    #if those statements doesnt return anything, we repaired the machine, and we need to calculate further for the next interval
    totDowntime+=(timeForRepair)
    timeLeft = 8-timeOfFail-timeForRepair
    while True:
        if (timeLeft <0):
            break
        newTimeOfFail = np.random.exponential(200)
        newTimeOfRepair = np.random.exponential(8)
        if (newTimeOfFail < timeLeft): # if we fail again within the time
            if (newTimeOfRepair < timeLeft-newTimeOfFail):
                totDowntime+= (newTimeOfRepair)
                timeLeft -= (newTimeOfFail+newTimeOfRepair)
                break
            else: #if we cant repair again
                totDowntime+=(timeLeft-newTimeOfFail)
                break
        else: #if machine doesnt fail again
            break

print("TotDowntime is: ", totDowntime)
print("prosentage of time down: ", totDowntime/(numberOfDays*8), "with ", numberOfDays, " days")
print("Hours of downtime: ", 8*totDowntime/(numberOfDays*8))


