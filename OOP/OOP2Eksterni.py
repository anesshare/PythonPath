class Car:
    def __init__(self,model,year,color,forSale):         #Ovako se definise construcotr
        self.model = model
        self.year = year
        self.color = color
        self.forSale = forSale
    def drive(self):
        print(f"You drive the {self.model}, your car is from {self.year} year ")
    def stop(self):
          print(f"You stop the {self.model} your car is from {self.year} year ")
