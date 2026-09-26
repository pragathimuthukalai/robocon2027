class SensorValidation:
    def __init__(self, front,left, right,rear,battery):
        self.__f= front
        self.__l = left
        self.__r= right
        self.__re = rear
        self.__b = battery
    
    def SensorValidation(self):
        if(self.__f<0 or self.__f>400):
            print("Invalid")
        else:
            print("Valid")
        
        if(self.__l<0 or self.__l>400):
            print("Invalid")
        else:
            print("Valid")
        
            
        if(self.__r<0 or self.__r>400):
            print("Invalid")
        else:
            print("Valid")
        
        if(self.__re<0 or self.__re>400):
            print("Invalid")
        else:
            print("Valid")
        
class BatterySensor:
    def __init__(self, battery):
        self.__b = battery
    def BatteryDecision(self):
        if(self.__b>0.50):
            print("Normal Operation")
        if(0.20<self.__b<0.50):
            print("low battery")
        else:
            print("Return to Charger")

class DecisionSensor:

    def EmergencyStop(self):
        if (self.__f <= 10 or self.__b <= 0.05):
            print("EmergencyStop")
        else:
            print("Continue")
class NavigationDecision:
    def __init__(self, front, left, right, rear):
        self.__f = front
        self.__l = left
        self.__r = right
        self.__re = rear

    def NavigationDecision(self):
        if (self.__f > 50):
            print("Move Forward")
        elif (self.__f <= 50 ) :
            if (self.__l > self.__r and self.__l > 20):
                print("Turn Left")
            elif (self.__r > self.__l and self.__r > 20):
                print("Turn Right")
            elif (self.__l == self.__r and( self.__l > 20 and self.__r > 20)):
                print("Choose Left")
            elif (self.__l <= 20 and self.__r <= 20):
                if(self.__re > 50):
                    print("Move Backward")
            else:
                print("Stop")

front=int(input("Enter the value of sensor:"))
left=float(input("Enter the battery life:"))
right=int(input("Enter the value of sensor:"))
rear=int(input("Enter the value of sensor:"))
battery=int(input("Enter the value of sensor:"))
result=SensorValidation(front,left,right,rear,battery)
result.SensorValidation()
battery=BatterySensor(battery)
battery.BatteryDecision()
navigation=NavigationDecision(front,left,right,rear)
navigation.NavigationDecision()