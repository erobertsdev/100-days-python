programming_dict = {
    "Bug": "An error in code",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dict["Bug"])

# Adding to dictionary
programming_dict["Loop"] = "The action of doing something over and over again."
print(programming_dict)

# Clear an existing dictionary
# programming_dict = {}
# print(programming_dict)

# Edit an item in a dictionary
programming_dict["Bug"] = "A bugaloo hoody hoo"
print(programming_dict)

# Loop through a dictionary
for key in programming_dict:
    print(key)
    print(programming_dict[key])

# Grading program exercise
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draca": 74,
    "Neville": 62
}

student_grades = {}
for student in student_scores:
    if student_scores[student] >= 90:
        student_grades[student] = 'A'
    elif student_scores[student] >= 80 and student_scores[student] < 90:
        student_grades[student] = 'B'
    elif student_scores[student] >= 70 and student_scores[student] < 80:
        student_grades[student] = 'C'
    elif student_scores[student] >= 60 and student_scores[student] < 70:
        student_grades[student] = 'D'
    else:
        student_grades[student] = 'F'

print(student_grades)

# nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 9
    }
}

travel_list = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {"country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 9
    }
]

def add_new_country(list_name, country, total_visits, cities_visited):
    list_name.append({
        "country": country,
        "total_visits": total_visits,
        "cities_visited": cities_visited
    })

add_new_country(travel_list, "Russia", 2, ["Moscow", "Saint Petersburg", "Russia Face"])
print(travel_list)

# Blind Auction - Project

bids = {}
bidding_finished = False

def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bid(bids)

