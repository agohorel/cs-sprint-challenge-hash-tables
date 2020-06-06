#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __repr__(self):
        return f"source: {self.source}, destination: {self.destination}"


def reconstruct_trip(tickets, length):
    trip = {}
    route = []
    
    for ticket in tickets:
        trip[ticket.source] = ticket.destination

    nxt = trip['NONE']

    while nxt != "NONE":
        route.append(nxt)
        nxt = trip[nxt] 

    route.append("NONE")

    return route
