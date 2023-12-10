def add_time(currentTime, timeToAdd, currentDayName=None):
    resultString=""
    
    def convertHoursMinutesToMinutes(timeString):
        pass
    def convertMinutesToDaysHoursMinutes(minsNumber):
        pass
    def describeDaysPassed(daysPassedNumber):
        pass
    def calculateWeekDayName(startingDayName, daysAddedNumber):
        pass
    def formatResultString(hours, minutes, resultDayName=None):
        pass
    
    currentTimeInMinutes=convertHoursMinutesToMinutes(currentTime)
    timeToAddInMinutes=convertHoursMinutesToMinutes(timeToAdd)
    finalTimeInMinutes=currentTimeInMinutes+timeToAddInMinutes
    
    finalTimeArray=convertMinutesToDaysHoursMinutes
    if(currentDayName is not None):
        resultDayName=calculateWeekDayName(currentDayName, finalTimeArray[0])

    resultString=formatResultString(finalTimeArray[1], finalTimeArray[2], resultDayName)
    return resultString