import time
class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutdown','running']


    def __init__(self,name='',power=False,battery=100):
        self.name=name
        self.power=power
        self.battery_level=battery

        pass
    
    def turn_on (self,power=True):
        self.power=power
        print(self.__states[1])
        pass

    def turn_off(self,power=False):
        self.power=power
        print(self.__states[0])
        pass

    def charge_battery(self):
        if self.battery_level < 100 and self.power == False:
            while self.battery_level<100:
                self.battery_level+=1
                print(self.battery_level)
                time.sleep(0.2)

    def show_speed(self):
        print(self.__current_speed)

    def set_speed(self,avance,vitesse):
        if avance==True:
            self.current_speed=vitesse
            print(self.current_speed)
        else:
            self.current_speed=-vitesse
            print(self.current_speed)


    def stop_speed(self):
        self.__current_speed = 0  

    def status(self):
        print("")


    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,n):
        self.__name = n


    @property
    def power(self):
        return self.__power
    @power.setter
    def power (self,p):
        self.__power = p


    @property
    def current_speed (self):
        return self.__current_speed
    @current_speed.setter
    def current_speed(self,c):
        self.__current_speed = c
    
    @property
    def battery_level(self):
        return self.__battery_level
    @battery_level.setter
    def battery_level(self,b):
        self.__battery_level = b

    @property
    def states(self):
        return self.__states
    @states.setter
    def states(self,b):
        self.states.append(b)
