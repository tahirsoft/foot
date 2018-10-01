import numpy as np

from parser import countries


def goals():
    score = np.random.choice(8, 2, p=[0.27, 0.35, 0.22, 0.13, 0.021,
                                      0.0056, 0.002, 0.0014])
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
        score = sorted(score, reverse=True)
    else:
        score = sorted(score)
    final_score = np.random.choice(score, 2, replace=False, p=[p1, p2])
    return team_1, final_score[0], team_2, final_score[1]
