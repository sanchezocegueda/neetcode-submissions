class SuperHero:
    def __init__(self, name: str, health: int, power_level: int):
        self.__name = name
        self.__health = health
        self.__power_level = power_level
        # TODO: Add the private attributes
    
    # TODO: Add the getter and setter methods

    def get_health(self) -> int:
        return self.__health
    
    def set_health(self, health: int) -> None:
        if 0 <= health and health <= 100:
            self.__health = health
        elif health > 100:
            print("You can't set the health to more than 100")
        else:
            print("You can't set the health to less than 0")
    

    def get_name(self) -> str:
        return self.__name


    def set_name(self, name: str) -> None:
        self.__name = name

    def get_power_level(self) -> int:
        return self.__power_level

    def set_power_level(self, power_level: int) -> None:
        if power_level > 10:
            print("You can't set the power level to more than 10")
        elif power_level < 1:
            print("You can't set the power level to less than 1")
        else:
            self.__power_level = power_level

super_hero = SuperHero("Batman", 80, 9)

print(super_hero.get_health()) # this should print 80
super_hero.set_health(110) # this should print You can't set the health to more than 100
super_hero.set_health(-10) # this should print You can't set the health to less than 100
super_hero.set_health(70)

print(super_hero.get_power_level()) # this should print 9
super_hero.set_power_level(11) # this should print You can't set the power level to more than 10
super_hero.set_power_level(0) # this should print You can't set the power level to less than 1
super_hero.set_power_level(7)



# TODO: print the hero's attributes
print(f"{super_hero.get_name()} has {super_hero.get_health()} health and {super_hero.get_power_level()} power level")
