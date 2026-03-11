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


    
