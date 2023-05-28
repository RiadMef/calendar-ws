#There are 24 hours in a day, 60 minutes in an hour, 
#so there are 4 15-minute slots in an hour. 
#there are 96 slots in a day (24 hours * 4 slots per hour(15min)), and 672 slots in a week (96 slots per day * 7 days)



# AN empty schedule is a 2D array of 672 slots, each slot is a 2D array of 2 elements,


class Schedule:

    def __init__(self, schedule):
        self.schedule = schedule

    
    def getSchedule(self):
        return self.schedule
    
    def getMonday(self):
        return self.schedule[0:96]
    
    def getTuesday(self):
        return self.schedule[96:192]
    

    def getWednesday(self):
        return self.schedule[192:288]

    def getThursday(self):
        return self.schedule[288:384]
    
    def getFriday(self):
        return self.schedule[384:480]
    
    def getSaturday(self):
        return self.schedule[480:576]
    
    def getSunday(self):
        return self.schedule[576:672]
    


        


    
    


