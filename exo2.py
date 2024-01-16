from Robot import Robot


class Human():   
	# Human class content here
    __sex=['Male','Female']
    __stomach=[]
    __digest = False
    __vision = True

    def __init__(self,sex:int) -> None:
        if sex == 1:
            print(self.sex[1])
        elif sex == 0:
            print(self.sex[0])
        else:
            print("Veuillez mettre une valeur: 0 = Male , 1 = Female")
        
        
        pass

    def digest_food(self,digest:bool):
        self.digest = digest
        if digest == False:
            print("Sick")
            for i in self.stomach:
                self.stomach.clear()

        else:
            print("Fine!")
    
    def eat(self,food):
        self.stomach.append(food)
        print("L'aliment à été mangé",food)

    def day_time(self,night):
        if night ==True:
            self.vision = False
        else:
            self.vision = True

    @property
    def sex(self):
        return self.__sex
    @sex.setter
    def sex(self,s):
        self.__sex = s

    @property
    def stomach(self):
        return self.__stomach
    @stomach.setter
    def stomach(self,s):
        self.__stomach = s

    @property
    def digest(self):
        return self.__digest
    @digest.setter
    def digest(self,s):
        self.__digest = s

    @property
    def vision(self):
        return self.__vision
    @vision.setter
    def vision(self,s):
        self.__vision = s


    pass
	
 
	
class Cyborg(Robot, Human):   
	
 
	
    def __init__(self, name, sex):   
	
        # initiate Robot parent class
	
        Robot.__init__(self, name)
	
        # initiate Human parent class
	
        Human.__init__(self, sex)

        pass

	
 
	
 
	
cyborg = Cyborg('Deux Ex Machina', 1)
	
 
	
print(cyborg.name, 'sexe', cyborg.sex)
	
print('Charging battery...')
	
cyborg.charge_battery()
	
cyborg.status()
	
cyborg.eat('banana')
	
cyborg.eat(['coca', 'chips'])
	
cyborg.digest_food(False)

print(cyborg.stomach)