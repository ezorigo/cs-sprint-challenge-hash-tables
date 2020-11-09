#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):\

    cache = {}
    route = [None] * length

    for i in tickets:
        if i.source == "NONE":
            route[0] = i.destination
        cache[i.source] = i.destination
    
    for ticket in range(1, length):
        route[ticket] = cache[route[ticket - 1]]

    return route
