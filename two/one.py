# rock = [A,X] , paper = [B, Y], scissors = [C, Z]
outcome_dict = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0,
    },
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6,
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3,
    }
}

score_dict = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def calculate_score_for_round(opponent_move, my_move):
    return outcome_dict[opponent_move][my_move] + score_dict[my_move]


with open("input.txt") as f:
    score = 0
    for line in f:
        opponent_move = line[0]
        my_move = line[2]

        score += calculate_score_for_round(opponent_move, my_move)

    print(score)  # 8890
