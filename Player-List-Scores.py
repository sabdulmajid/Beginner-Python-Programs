# Player-List-Scores.py

# Initialize the empty 'arrays'.
names = [None] * 5
squad_shots = [None] * 5
squad_assists = [None] * 5
squad_goals = [None] * 5
success_index = [None] * 5

# Initialize the global variables.
squad_total = 0
success_highest = 0
player_highest = ""


# Validation Function:
def validate_score(score, score_type):
    # test for integer
    try:
        int(score)
    except:
        return False

    # range test
    if score_type == 1 and (int(score) > 100 or int(score) < 0):
        return False
    if score_type == 2 and (int(score) > 50 or int(score) < 0):
        return False
    if score_type == 3 and (int(score) > 40 or int(score) < 0):
        return False

    # pass tests
    return True


# Main Loop


for i in range(5):
    # get inputs and validate all numerical data
    name = input("Enter player's name:  ")
    names[i] = name

    shots = input("Enter the number of shots made in total:  ")
    while validate_score(shots, 1) is False:
        print("Error: Unexpected input")
        shots = input("Enter the number of shots made in total:  ")

    assists = input("Enter the number of assists made in total:  ")
    while validate_score(assists, 2) is False:
        print("Error: Unexpected input")
        assists = input("Enter the number of shots made in total:  ")

    goals = input("Enter the number of goals scored in total:  ")
    while validate_score(goals, 3) is False:
        print("Error: Unexpected input")
        goals = input("Enter the number of shots made in total:  ")

    # load the 'arrays'
    squad_shots[i] = int(shots)
    squad_assists[i] = int(assists)
    squad_goals[i] = int(goals)

    # process scores
    success_index[i] = (squad_assists[i]) + (2 * squad_shots[i]) + (3 * squad_goals[i])
    squad_total = squad_total + success_index[i]

    # print current player's success index
    print(name, 'has', goals,'goals, ', assists, 'assists, ', shots, 'shots,', 'and a total of', success_index[i], 'points in his index.')

    # keep track of highest scoring player
    if success_index[i] > success_highest:
        success_highest = success_index[i]
        player_highest = name

# Calculate squad average:
squad_average = squad_total / 5

# Total squad goals.
squad_total_goals = sum(squad_goals)
# print final summary
print('\nThe total amount of squad goals are: ', squad_total_goals, 'goals.')
print('\nSquad Average:', squad_average)
print('Most successful player:', player_highest, "with", success_highest, 'as his total points.')
