class Car :
    name = " "
    model = " "
    weight = 0
    color = " "

    def __init__(self, name, model, weight, color):
        self.name = name
        self.model = model
        self.weight = weight
        self.color = color
    def start(self) :
        pass
    def dive(self) :
        pass
    def stop(self) :
        pass
    def brake(self) :
        pass
    def toString(self) :
        pass

i = Car("Honda" , "CR-V", 2000, "Brow")