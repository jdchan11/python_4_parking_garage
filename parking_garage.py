class ParkingGarage():
    def __init__(self, time = 0, currentTicket = {}, tickets = 10, spaces_available = 10):
        self.tickets = tickets
        self.spaces_available = spaces_available
        self.time = time
        self.currentTicket = currentTicket
    
    def takeTicket(self):
        self.tickets -= 1
        self.spaces_available -= 1
    
    def payForParking(self):
        self.currentTicket = {
            'paid' : False,
            'amt_paid' : 0,
        }
        self.time = input("How long were you here (in hours)? ")
        if self.time == '0':
            self.currentTicket['paid'] = False
        else:
            if float(self.time) > 0 and float(self.time) < 5:
                self.currentTicket['amt_paid'] = 15
                print(f"You owe ${self.currentTicket['amt_paid']}.")
            elif float(self.time) >= 5:
                self.currentTicket['amt_paid'] = 30
                print(f"You owe ${self.currentTicket['amt_paid']}.")
            self.currentTicket['paid'] = True
        if self.currentTicket['paid'] == True:
            print("You have 15 minutes to exit the garage.")
    
    def leaveGarage(self):
        if self.currentTicket['paid'] == True:
            print("Thank you, have a nice day!")
            self.tickets += 1
            self.spaces_available += 1


nyc = ParkingGarage()
def run():
    nyc.takeTicket()
    nyc.payForParking()
    nyc.leaveGarage()
    if nyc.currentTicket['paid'] == False:
        print("You must pay before you leave.")
        nyc.payForParking()
        nyc.leaveGarage()

run()





