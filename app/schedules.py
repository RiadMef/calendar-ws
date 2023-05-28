from app.schedule import Schedule
import numpy as np

class Schedules :
    def __init__(self, schedules):
        self.schedules = self.formatSchedules(schedules)
    


    def formatSchedules(self, schedules):
        scheduleObjects = []

        for schedule in schedules:
            scheduleObjects.append(Schedule(schedule))
        scheduleObjects[1].schedule[2] = False
        return scheduleObjects

    

    def compareMonday(self):

        return np.logical_or(self.schedules[0].getMonday(), self.schedules[1].getMonday()).tolist()
    