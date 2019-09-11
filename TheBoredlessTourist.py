destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'So Paulo, Brazil', 'Cairo, Egypt']
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
test_traveler2 = ['Seppo Hovi', 'Cairo, Egypt', ['monument', 'historical site', 'museum']]
attractions = [[] for i in range(len(destinations))]


def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index


def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index]
        attractions_for_destination.append(attraction)
    except ValueError:
        return


def find_attractions(destination, interests):
    attractions_with_interest = []
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    for attraction in attractions_in_city:
        for interest in interests:
            if interest in attraction[1]:
                if attraction[0] in attractions_with_interest:
                    continue
                else:
                    attractions_with_interest.append(attraction[0])

    return attractions_with_interest

def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = "Hi " + str(traveler[0]) + ", we think you'll like these places around "
    for attraction in traveler_attractions:
        interests_string += attraction
    return interests_string





add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("So Paulo, Brazil", ["So Paulo Zoo", ["zoo"]])
add_attraction("So Paulo, Brazil", ["Ptio do Colgio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(get_attractions_for_traveler(test_traveler))
print(get_attractions_for_traveler(test_traveler2))