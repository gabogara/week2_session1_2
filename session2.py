"""UPI TEMPLATE

--- UNDERSTAND ---

    I - Inputs: destinations (dictionary),  ating_threshold (number)
    O - Outputs: dictionary
    C - Constraints: rating < threshold : Delete
                    rating >= threshold : keep
    E - Edge Cases (and examples): {} return {}

--- PLAN --- we neet to check every element in the dicctionary (rating)
    you look thougt every destination dictionary and check rating,
    and then if rating < threshold : Delete.
    At the end return the dictionary.

--- IMPLEMENT ---

"""

"""
1) Imagine you are working on a wildlife conservation database. Write a function named most_endangered() that 
returns the species with the highest conservation priority based on its population.

The function should take in a list of dictionaries named species_list as a parameter. 
Each dictionary represents data associated with a species, including its name, habitat, and wild population. 
The function should return the name of the species with the lowest population.

If there are multiple species with the lowest population, return the species with the lowest index.
"""


def most_endangered(species_list):
    # min_temp = species_list[0]
    # for specie in species_list:
    #     if specie["population"] < min_temp["population"]:
    #         min_temp = specie
    # return min_temp["name"]
    min_population = species_list[0]["population"]
    key_min = species_list[0]["name"]
    for specie in species_list:
        if specie["population"] < min_population:
            min_population = specie["population"]
            key_min = specie["name"]

    return key_min


species_list = [
    {"name": "Amur Leopard", "habitat": "Temperate forests", "population": 84},
    {"name": "Javan Rhino", "habitat": "Tropical forests", "population": 72},
    {"name": "Vaquita", "habitat": "Marine", "population": 10},
]


# print(most_endangered(species_list))
"""
2) As part of conservation efforts, certain species are considered endangered and are represented by the string 
endangered_species. 
Each character in this string denotes a different endangered species. 
You also have a record of all observed species in a particular region, represented by the string observed_species. 
Each character in observed_species denotes a species observed in the region.

Your task is to determine how many instances of the observed species are also considered endangered.
Note: Species are case-sensitive, so "a" is considered a different species from "A".
Write a function to count the number of endangered species observed.
"""
## O(n * m)

# def count_endangered_species(endangered_species, observed_species):
#     counter = 0
#     for i in range(len(endangered_species)):
#         for j in range(len(observed_species)):
#             if endangered_species[i] == observed_species[j]:
#                 counter += 1
#     return counter


# ## O(n)
def count_endangered_species(endangered_species, observed_species):
    my_set = set(endangered_species)
    counter = 0

    for specie in observed_species:
        if specie in my_set:
            counter += 1
    return counter


endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"


# print(count_endangered_species(endangered_species1, observed_species1))
# print(count_endangered_species(endangered_species2, observed_species2))

"""
3)In a wildlife research station, each letter of the alphabet represents a different observation point laid out in a single row. 
Given a string station_layout of length 26 indicating the layout of these observation points (indexed from 0 to 25), 
you start your journey at the first observation point (index 0). To make observations in a specific order represented by a string observations, 
you need to move from one point to another.

The time taken to move from one observation point to another is the absolute difference between their indices, |i - j|.

Write a function that returns the total time it takes to visit all the required observation points in the given order with one movement.

"""


def navigate_research_station(station_layout, observations):
    counter_dict = {}

    for i, val in enumerate(station_layout):
        counter_dict[val] = i

    current_pos = 0
    total_time = 0

    for char in observations:
        next_pos = counter_dict[char]
        total_time += abs(current_pos - next_pos)
        current_pos = next_pos

    return total_time


station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

# print(navigate_research_station(station_layout1, observations1))
# print(navigate_research_station(station_layout2, observations2))

"""
4) In your work with a wildlife conservation database, you have two lists: observed_species and priority_species. 
The elements of priority_species are distinct, and all elements in priority_species are also in observed_species.

Write a function prioritize_observations() that sorts the elements of observed_species such that the 
relative ordering of items in observed_species matches that of priority_species. 
Species that do not appear in priority_species should be placed at the end of observed_species in ascending order.
"""


def prioritize_observations(observed_species, priority_species):
    counter = {}
    solution = []
    for observed in observed_species:
        if observed in counter:
            counter[observed] += 1
        else:
            counter[observed] = 1

    for specie in priority_species:
        if specie in counter:
            solution.extend([specie] * counter[specie])
            del counter[specie]

    remaining = []

    for specie in counter:
        remaining.extend([specie] * counter[specie])

    remaining.sort()
    solution.extend(remaining)

    return solution


observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

# print(prioritize_observations(observed_species1, priority_species1))
# print(prioritize_observations(observed_species2, priority_species2))


"""
5) You are given a 0-indexed integer array species_populations of even length, 
where each element represents the population of a particular species in a wildlife reserve.

As long as species_populations is not empty, you must repetitively:

Find the species with the minimum population and remove it.
Find the species with the maximum population and remove it.
Calculate the average population of the two removed species.
The average of two numbers a and b is (a+b)/2.

For example, the average of 200 and 300 is (200+300)/2=250.

Return the number of distinct averages calculated using the above process.

Note that when there is a tie for a minimum or maximum population, any can be removed.
"""


def distinct_averages(species_populations):
    pass


species_populations1 = [4, 1, 4, 0, 3, 5]
species_populations2 = [1, 100]

# print(distinct_averages(species_populations1))
# print(distinct_averages(species_populations2))


"""

"""


"""UPI TEMPLATE

--- UNDERSTAND ---

    I - Inputs: destinations (dictionary),  ating_threshold (number)
    O - Outputs: dictionary
    C - Constraints: rating < threshold : Delete
                    rating >= threshold : keep
    E - Edge Cases (and examples): {} return {}

--- PLAN --- we neet to check every element in the dicctionary (rating)
    you look thougt every destination dictionary and check rating,
    and then if rating < threshold : Delete.
    At the end return the dictionary.

--- IMPLEMENT ---

"""


""" UPI TEMPLATE

--- UNDERSTAND ---

    I - Inputs: key
                message
    O - Outputs: string
    C - Constraints: 
        only 
    E - Edge Cases (and examples)

--- PLAN ---
    1 Create a subtitucion table (dictionary)
    2 Build the mapping using the alphabet order
    3 Decode the message
    4 Construct the decoded string



--- IMPLEMENT ---


"""
"""
   -----------------------    SET VERSION 2   --------------------------------------
"""


"""
1)You're planning an epic trip and have a dictionary of destinations mapped to their respective rating scores. 
Your goal is to visit only the best-rated destinations. Write a function that takes in a dictionary 
destinations and a rating_threshold as parameters. 
The function should iterate through the dictionary and remove all destinations that have a rating 
strictly below the rating_threshold. Return the updated dictionary.

"""


def remove_low_rated_destinations(destinations, rating_threshold):

    result = {}
    for key, value in destinations.items():
        if value >= rating_threshold:
            result[key] = value
    return result


destinations = {"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}
destinations2 = {"Bogotá": 4.8, "Kansas City": 3.9, "Tokyo": 4.5, "Sydney": 3.0}

# print(remove_low_rated_destinations(destinations, 4.0))
# print(remove_low_rated_destinations(destinations2, 4.9))


"""
2) As a seasoned traveler, you've collected a variety of souvenirs from different destinations. 
You have an array of string souvenirs, where each string represents a type of souvenir. 
You want to know if the number of occurrences of each type of souvenir in your collection is unique.

Write a function that takes in an array souvenirs and returns True if the number of 
occurrences of each value in the array is unique, or False otherwise.
"""


def unique_souvenir_counts(souvenirs):
    frecuency = {}

    for souvenir in souvenirs:
        if souvenir in frecuency:
            frecuency[souvenir] += 1
        else:
            frecuency[souvenir] = 1

    return len(frecuency.values()) == len(set(frecuency.values()))


souvenirs1 = ["keychain", "hat", "hat", "keychain", "keychain", "postcard"]
souvenirs2 = ["postcard", "postcard", "postcard", "postcard"]
souvenirs3 = ["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"]

# print(unique_souvenir_counts(souvenirs1))
# print(unique_souvenir_counts(souvenirs2))
# print(unique_souvenir_counts(souvenirs3))


"""
two_sum
"""


def two_sum(arr, target):
    vistos = {}

    for i, num in enumerate(arr):
        faltante = target - num
        if faltante in vistos:
            return [vistos[faltante], i]
        vistos[num] = i


print(two_sum([2, 7, 11, 15], 9))
