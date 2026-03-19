"""
UPI TEMPLATE

--- UNDERSTAND ---

    I - Inputs
    O - Outputs
    C - Constraints
    time complexity = O(n) AKA linear time
    space complexity: O(n)
    E - Edge Cases (and examples)

--- PLAN ---
High-level approach (key idea): Iterate iver list, store/tally words in dictionary; then return.

steps (pseudocode):
initialize an empty dictionary word_counts
for each word in words
    if the word exist in word_count
        increment that word's value to 1
return word_counts

--- IMPLEMENT ---

"""

""" UPI TEMPLATE

--- UNDERSTAND ---

    I - Inputs
    O - Outputs
    C - Constraints
    E - Edge Cases (and examples)

--- PLAN ---

--- IMPLEMENT ---

"""

"""
1) Given two lists of strings artists and set_times of length n, write a function lineup() 
that maps each artist to their set time.

An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).
"""

# def lineup(artists, set_times):
#     result = {}
#     for i in range(len(artists)):
#         result[artists[i]] = set_times[i]
#     return result


artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []


# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))

# ----------------------------------------
"""
2) You are designing an app for your festival to help attendees have the best experience possible! 
As part of the application, users will be able to easily search their favorite artist and find out the day, 
time, and stage the artist is playing at. Write a function get_artist_info() that accepts a string artist 
and a dictionary festival_schedule mapping artist's names to dictionaries containing the day, 
time, and stage they are playing on. Return the dictionary containing the information about the given artist.

If the artist searched for does not exist in festival_schedule, 
return the dictionary {"message": "Artist not found"}.
"""


""" UPI TEMPLATE

--- UNDERSTAND ---

    I - Inputs: string of artist and the second one is a dictionary
    O - Outputs: A new dictionary
    C - Constraints: n / a
    E - Edge Cases (and examples)
        If artist in festival not found return "not found" in the value 
        of that dictionary

--- PLAN ---
take the artist as a parameters (string) and check if is exist in 
the festival schedule dictionary we got as a parameter  

--- IMPLEMENT ---

"""


festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"},
}


def get_artist_info(artist, festival_schedule):
    return festival_schedule.get(artist, {"message": "Artist not found"})


# print(get_artist_info("Blood Orange", festival_schedule))
# print(get_artist_info("Taylor Swift", festival_schedule))


"""
3) A dictionary ticket_sales is used to map ticket type to number of tickets sold. 
Return the total number of tickets of all types sold.
"""


def total_sales(ticket_sales):
    acumulator = 0
    for value in ticket_sales.values():
        acumulator += value
    return acumulator


ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

# print(total_sales(ticket_sales))


"""
4) Demand for your festival has exceeded expectations, so you're expanding the festival to 
span two different venues.
Some artists will perform both venues, while others will perform at just one. To ensure that there are no 
scheduling conflicts, implement a function identify_conflicts() that accepts two dictionaries 
venue1_schedule and venue2_schedule each mapping the artists playing at the venue to their set times. 
Return a dictionary containing the key-value pairs that are the same in each schedule.
"""


def identify_conflicts(venue1_schedule, venue2_schedule):
    result = {}

    for key, value in venue1_schedule.items():
        if key in venue2_schedule and venue2_schedule[key] == value:
            result[key] = value
    return result


venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM",
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM",
}

# print(identify_conflicts(venue1_schedule, venue2_schedule))


"""
5) As part of the festival, attendees cast votes for their favorite set. Given a dictionary votes 
that maps attendees id numbers to the artist they voted for, return 
the artist that had the highest number of votes. If there is a tie, 
return any artist with the top number of votes.
"""


def best_set(votes):
    counter = {}

    for value in votes.values():
        if value in counter:
            counter[value] += 1
        else:
            counter[value] = 1

    winner = max(counter, key=counter.get)
    return winner


votes1 = {
    1234: "SZA",
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA",
}

votes2 = {
    1234: "SZA",
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
}

# print(best_set(votes1))
# print(best_set(votes2))


"""
6) You are given an array audiences consisting of positive integers representing 
the audience size for different performances at a music festival.

Return the combined size of every audience that had the maxmium size.

The audience size of a performance is the number of people who attended that performance.
"""


# def max_audience_performances(audiences):
#     dictionary = {}
#     for audience in audiences:
#         if audience in dictionary:
#             dictionary[audience] += 1
#         else:
#             dictionary[audience] = 1
#     maximun = max(dictionary)
#     times = dictionary.get(maximun)
#     return times * maximun


# audiences1 = [100, 200, 200, 150, 100, 250]
# audiences2 = [120, 180, 220, 150, 220]


# print(max_audience_performances(audiences1))
# print(max_audience_performances(audiences2))


"""
7) If you used a dictionary as part of your solution to max_audience_performances() in the previous problem,
try reimplementing the function without using a dictionary. If you implemented max_audience_performances() without using a dictionary,
try solving the problem with a dictionary.

Once you've come up with your second solution, compare the two. Is one solution better than the other? Why or why not?
"""


def max_audience_performances(audiences):
    max_arr = max(audiences)
    counter = 0

    for audience in audiences:
        if audience == max_arr:
            counter += 1
    return max_arr * counter


audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

# print(max_audience_performances(audiences1))
# print(max_audience_performances(audiences2))


"""
8) Given an array of integers popularity_scores representing the popularity scores of songs in a music festival playlist, 
return the number of popular song pairs.

A pair (i, j) is called popular if the songs have the same popularity score and i < j.

Hint: number of pairs = (n x n-1)/2
"""


def num_popular_pairs(popularity_scores):
    counts = {}

    for score in popularity_scores:
        if score in counts:
            counts[score] += 1
        else:
            counts[score] = 1

    total_pairs = 0
    for n in counts.values():
        total_pairs += (n * (n - 1)) // 2
    return total_pairs


popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3))


"""
9) You are given two lists of strings s and t representing the stage arrangements of performers in two different performances at a music festival, such that every performer occurs at most once in s and t, and t is a permutation of s.
The stage arrangement difference between s and t is defined as the sum of the absolute difference between the index of the occurrence of each performer in s and the index of the occurrence of the same performer in t.
Return the stage arrangement difference between s and t.
A permutation is a rearrangement of a sequence. For example, [3, 1, 2] and [2, 1 , 3] are both permutations of the list [1, 2, 3].

Hint: Absolute value function
"""


"""************************************************************

                            VERSION 2
"""

"""
1) Given two lists of length n, crew and position, map the space station crew to their position on board the international space station.

Each crew member crew[i] has job position[i] on board, where 0 <= i < n and len(crew) == len(position).
Hint: Introduction to dictionaries
"""


def space_crew(crew, position):
    result = {}
    for i in range(len(crew)):
        result[crew[i]] = position[i]
    return result


exp70_crew = [
    "Andreas Mogensen",
    "Jasmin Moghbeli",
    "Satoshi Furukawa",
    "Loral O'Hara",
    "Konstantin Borisov",
]

exp70_positions = [
    "Commander",
    "Flight Engineer",
    "Flight Engineer",
    " Flight Engineer",
    "Flight Engineer",
]

ax3_crew = [
    "Michael Lopez-Alegria",
    "Walter Villadei",
    "Alper Gezeravci",
    "Marcus Wandt",
]

ax3_positions = [
    "Commander",
    "Mission Pilot",
    "Mission Specialist",
    "Mission Specialist",
]

# print(space_crew(exp70_crew, exp70_positions))
# print(space_crew(ax3_crew, ax3_positions))


"""
2) Given a dictionary planets that maps planet names to a dictionary containing the planet's number of moons and orbital period, 
write a function planet_lookup() that accepts a string planet_name and returns a string in the form Planet <planet_name> 
has an orbital period of <orbital period> Earth days and has <number of moons> moons. 
If planet_name is not a key in planets, return "Sorry, I have no data on that planet.".
"""


# def planet_lookup(planet_name):
#     out = ""
#     if planet_name in planetary_info:
#         first_key = list(planetary_info[planet_name].items())[0]

#     else:
#         out = out + "Sorry, I have no data on that planet."
#     return first_key


def planet_lookup(planet_name):
    if planet_name not in planetary_info:
        return "Sorry, I have no data on that planet."
    return f"Planet {planet_name} has an orbital period of {planetary_info[planet_name]['Moons']} Earth days and has {planetary_info[planet_name]['Orbital Period']} moons. "


planetary_info = {
    "Mercury": {"Moons": 0, "Orbital Period": 88},
    "Earth": {"Moons": 1, "Orbital Period": 365.25},
    "Mars": {"Moons": 2, "Orbital Period": 687},
    "Jupiter": {"Moons": 79, "Orbital Period": 10592},
}

# print(planet_lookup("Jupiter"))
# print(planet_lookup("Pluto"))


"""
3) As part of your job as an astronaut, you need to perform routine safety checks. 
You are given a dictionary oxygen_levels which maps room names to current oxygen levels and two integers min_val and max_val specifying 
the acceptable range of oxygen levels. Return a list of room names whose values are outside the range defined by min_val and max_val (inclusive).
"""


def check_oxygen_levels(oxygen_levels, min_val, max_val):
    result = []
    for key in oxygen_levels.keys():
        if oxygen_levels[key] < min_val:
            result.append(key)
        elif oxygen_levels[key] > max_val:
            result.append(key)

    return result


oxygen_levels = {
    "Command Module": 21,
    "Habitation Module": 20,
    "Laboratory Module": 19,
    "Airlock": 22,
    "Storage Bay": 18,
}

min_val = 19
max_val = 22

# print(check_oxygen_levels(oxygen_levels, min_val, max_val))


"""
4) Write a function data_difference() that accepts two dictionaries experiment1 and experiment2 and returns a new dictionary that contains only 
key-value pairs found exclusively in experiment1 but not in experiment2.
"""


def data_difference(experiment1, experiment2):
    result = {}

    for key, value in experiment1.items():
        if key not in experiment2 or experiment2[key] != value:
            result[key] = value
    return result


exp1_data = {"temperature": 22, "pressure": 101.3, "humidity": 45}
exp2_data = {"temperature": 18, "pressure": 101.3, "radiation": 0.5}

# print(data_difference(exp1_data, exp2_data))


"""
5) NASA has asked the public to vote on a new name for one of the nodes in the International Space Station. 
Given a list of strings votes where each string in the list is a voter's suggested new name, implement a function get_winner() 
that returns the suggestion with the most number of votes.

If there is a tie, return either option.
"""


def get_winner(votes):
    result = {}
    for vote in votes:
        if vote in result:
            result[vote] += 1
        else:
            result[vote] = 1
    return max(result, key=result.get)


votes1 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
votes2 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]

# print(get_winner(votes1))
# print(get_winner(votes2))


"""
6) Ground control has sent a transmission containing important information. 
A complete transmission is one where every letter of the English alphabet appears at least once.

Given a string transmission containing only lowercase English letters, return true if the transmission is complete, or false otherwise.
"""


def check_if_complete_transmission(transmission):
    return len(set(transmission)) == 26

    """
    :type transmission: str
    :rtype: bool
    """


transmission1 = "thequickbrownfoxjumpsoverthelazydog"
transmission2 = "spacetravel"

print(check_if_complete_transmission(transmission1))
print(check_if_complete_transmission(transmission2))
