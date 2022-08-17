class Flight():
    #Method to create a new flight with a given capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    #Method to add passenger to the flight
    def add_passenger(self, name):
        self.passengers.append(name)
        