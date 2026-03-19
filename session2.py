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
1) Imagine you are working on a wildlife conservation database. Write a function named most_endangered() that returns the species with 
the highest conservation priority based on its population.

The function should take in a list of dictionaries named species_list as a parameter. 
Each dictionary represents data associated with a species, including its name, habitat, and wild population. 
The function should return the name of the species with the lowest population.

If there are multiple species with the lowest population, return the species with the lowest index.
"""


def most_endangered(species_list):
    min_temp = species_list[0]
    for specie in species_list:
        if specie["population"] < min_temp["population"]:
            min_temp = specie
    return min_temp["name"]


species_list = [
    {"name": "Amur Leopard", "habitat": "Temperate forests", "population": 84},
    {"name": "Javan Rhino", "habitat": "Tropical forests", "population": 72},
    {"name": "Vaquita", "habitat": "Marine", "population": 10},
]


# print(most_endangered(species_list))
"""
2)As part of conservation efforts, certain species are considered endangered and are represented by the string endangered_species. 
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


## O(n)
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

print(count_endangered_species(endangered_species1, observed_species1))
print(count_endangered_species(endangered_species2, observed_species2))
"""
3)
"""


def remove_low_rated_destinations(destinations, rating_threshold):
    result = {}
    for destination, rating in destinations.items():
        if rating >= rating_threshold:
            result[destination] = rating
    return result


destinations = {"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}
destinations2 = {"Bogotá": 4.8, "Kansas City": 3.9, "Tokyo": 4.5, "Sydney": 3.0}

# print(remove_low_rated_destinations(destinations, 4.0))
# print(remove_low_rated_destinations(destinations2, 4.9))


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
