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
            counter +=1
    return max_arr * counter

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
