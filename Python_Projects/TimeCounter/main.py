import time

class Clock:
    def __init__(self):
        self.currTime = None
        
    def time_split(self, clockTime):
        return clockTime[0], clockTime[1], clockTime[2]

    def update_time(self):
        self.currTime = time.ctime(time.time())
        timeBreakdown = self.currTime.split()
        clockTime = timeBreakdown[3].split(':')
        timeHours, timeMinutes, timeSeconds = self.time_split(clockTime) 
        print(f'Time - {timeHours}:{timeMinutes}:{timeSeconds}')
        #print(self.currTime)

    def start_clock(self):
        while(True):
            self.update_time()
            time.sleep(1)

if __name__ == "__main__":
    '''
    Create an object called clock1 of class Clock and run the function 
    called start_clock in class Clock on clock1.
    '''
    clock1 = Clock()
    clock1.start_clock()
