
class favoriteAnimal:

    def __init__(self, lenArms, lenLegs, numEyes, boolTail, boolFurry) -> None:
        self.lenArms = lenArms
        self.lenLegs = lenLegs
        self.numEyes = numEyes
        self.boolTail = boolTail
        self.boolFurry = boolFurry

    def printAttributes(self):
        print("Length of Arms:",self.lenArms)
        print("Length of Legs:", self.lenLegs)
        print("Number of Eyes:", self.numEyes)
        print("Tail?:", self.boolTail)
        print("Furry?:", self.boolFurry)

if __name__ == "__main__":
    spider = favoriteAnimal(2, 2, 8, False, False)
    spider.printAttributes()