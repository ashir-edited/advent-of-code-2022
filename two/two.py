# rock = A (1 point), paper = B (2 points), scissors = C (3 points)
my_move_points_map = {
    "A": {
        "X": 3,
        "Y": 1,
        "Z": 2,
    },
    "B": {
        "X": 1,
        "Y": 2,
        "Z": 3,
    },
    "C": {
        "X": 2,
        "Y": 3,
        "Z": 1,
    }
}

# loss draw win
round_outcome_points_map = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}


def calculate_score_for_round(opponent_move, outcome):
    outcome_points = round_outcome_points_map[outcome]
    move_played_result = my_move_points_map[opponent_move][outcome]
    return outcome_points + move_played_result


with open("input.txt") as f:
    score = 0
    for line in f:
        opponent_move = line[0]
        outcome = line[2]

        score += calculate_score_for_round(opponent_move, outcome)

    print(score)  # 10238
