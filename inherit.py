#parent class
class dad:
    def __init__(self, eyes, kindness, hair_color):
        self.eyes = eyes
        self.kindness = kindness
        self.hair_color = hair_color
    
    def display_traits(self):
        print(f"Your traits - Eyes: {self.eyes}, Kindness: {self.kindness}, Hair Color: {self.hair_color}")

#child class
class Giwa(dad):
    def __init__(self, eyes, kindness, hair_color, talent, name, age):
        self.talent = talent
        self.name = name
        self.age = age

        #calling parent class constructor to access its attributes
        dad.__init__(self, eyes, kindness, hair_color)
#object creation
ob = Giwa("Brown", "High", "Black", "Piano", "Giwa", 14)
#calling the display method
ob.display_traits()
