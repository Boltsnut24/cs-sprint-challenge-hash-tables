#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}
    route = ['']
    next_source = None

    #add all tickets into cache key: source, value: destination
    for i in tickets:
        if i.source not in cache:
            cache[i.source] = i.destination

    #walk through cache for first flight
    for i in cache:
        if i == 'NONE':
            next_source = cache[i]

    #build route construction
    while route[-1] != 'NONE':
        #first flight only
        if route[0] == '':
            route[0] = next_source
        else:
            next_source = cache[next_source]
            route.append(next_source)



    return route
