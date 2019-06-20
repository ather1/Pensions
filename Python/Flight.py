class Flight:
    def __init__(self, origin,destination,duration):
        self.origin = origin
        self.destination = destination
        self.duration  = duration
        self.Passengers = []

    def  Print_info(self):
        print(f"The origin is: {self.origin}" )
        print(f"The destination is: {self.destination}" )
        print(f"The duration is: {self.duration} ")

        for passenger in self.Passengers:
            print(f"Passenger {passenger.name}")
        else:
            print("No passengers")

    def delay(self,delay):
        self.duration += delay

    def add_passenger(self,newpassenger):
        self.Passengers.append(newpassenger)

class Passenger:
    def __init__(self, name):
        self.name = name 

def main():
    f = Flight(origin="New York", destination= "Paris", duration=540)
    
    p1= Passenger(name="Bod Jones")
    p2= Passenger(name="Dave Smith")

    f.duration  += 10

    f = Flight(origin="London", destination= "Paris", duration=60)
    f.delay(100)
    
    
    f.add_passenger(p1)
    f.add_passenger(p2)
    f.Print_info()



if __name__ == "__main__":
    main()

