class Hero:
    def __init__(self, name, health, attackpower):
        self.__Name = name
        self.__Health = health
        self.__Damage = attackpower

    #getter called private
    def getName(self):
        return self.__Name
    def getHealth(self):
        return self.__Health
    def getDamage(self):
        return self.__Damage

    #setter (like same up)
    def attacking(self, value):
        self.__Health -= value
    def charging(self, newDamage):
        self.__Damage = newDamage

    #var instance private
    #self.__private = 'This is Private'
    #var instance protect
    #self._protected = 'This is Protected'

#====================================================output

#avatar = Hero("Yoru", 20000)
#print(avatar.__dict__)

yoru = Hero('Yoru', 100, 9)

print(yoru.__dict__)
print(yoru.getName())
print(yoru.getHealth())

yoru.attacking(5)
print(yoru.getHealth())
print(yoru.__dict__)

yoru.charging(10)
print(yoru.__dict__)

#print(avatar._protected)