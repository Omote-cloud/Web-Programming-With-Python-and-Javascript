class Flight():
    #Method to create a new flight with a given capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    #Method to add passenger to the flight
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    #Method to return number of open seats
    def open_seats(self):
        return self.capacity - len(self.passengers)
        