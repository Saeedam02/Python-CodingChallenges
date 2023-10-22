import random

# Number of iterations
n = [1000, 5000, 10000]

# The number of dice
num_dice = 2

# Function to throw the dice
def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

# Event 1: Total results equal to 5
def event1_count(num_trials):
    count = 0
    for _ in range(num_trials):
        dice_results = roll_dice(num_dice)
        if sum(dice_results) == 5:
            count += 1
    return count

# Event 2: Same results
def event2_count(num_trials):
    count = 0
    for _ in range(num_trials):
        dice_results = roll_dice(num_dice)
        if len(set(dice_results)) == 1:
            count += 1
    return count

# Event 3: The first result is greater than the second result
def event3_count(num_trials):
    count = 0
    for _ in range(num_trials):
        dice_results = roll_dice(num_dice)
        if dice_results[0] > dice_results[1]:
            count += 1
    return count

# Calculation of probability using the concept of relative frequency
def calculate_probability(event_count, num_trials):
    return event_count / num_trials

for num_trial in n:
    event1 = event1_count(num_trial)
    event2 = event2_count(num_trial)
    event3 = event3_count(num_trial)

    p_event1 = calculate_probability(event1, num_trial)
    p_event2 = calculate_probability(event2, num_trial)
    p_event3 = calculate_probability(event3, num_trial)

    print(f"The number of repetitions: {num_trial}")
    print(f"Probability of event 1: {p_event1}")
    print(f"Probability of event 2: {p_event2}")
    print(f"Probability of event 3: {p_event3}")
    print("------------")
