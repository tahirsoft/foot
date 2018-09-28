import numpy as np

from parser import countries


def goals():
    score = np.random.choice(8, 2, p=[0.28, 0.25, 0.15, 0.12,
                                      0.1, 0.05, 0.04, 0.01])
    return score


def chance_to_win(team_1, team_2):
    team_1_points = int(countries[team_1]["points"])
    team_2_points = int(countries[team_2]["points"])
    sum_points = team_1_points + team_2_points
    team_1_chance = round(team_1_points/sum_points, 2)
    team_2_chance = round(team_2_points/sum_points, 2)
    return team_1_chance, team_2_chance


def game(team_1, team_2):
    score = goals()
    p1, p2 = chance_to_win(team_1, team_2)
    if p1 >= p2:
        sorted(score, reverse=True)
    else:
        sorted(score)
    final_score = np.random.choice(score, 2, p=[p1, p2])
    return team_1, final_score[0], team_2, final_score[1]


p
