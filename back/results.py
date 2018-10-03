import numpy as np

from random import shuffle
from itertools import combinations
from group import countries as data
from group import grouping, default_teams, groups_names, final_grid


table = grouping(default_teams)


def goals() -> list:
    score = np.random.choice(8, 2, p=[0.27, 0.35, 0.22, 0.13, 0.021,
                                      0.0056, 0.002, 0.0014])
    return score


def penalty_goals() -> list:
    score = np.randome.choice(6, 2, p=[0.001, 0.02, 0.079, 0.1, 0.4, 0.4])
    return score


def chance_to_win(team_1: str, team_2: str) -> tuple:
    team_1_points = int(data[team_1]["points"])
    team_2_points = int(data[team_2]["points"])
    sum_points = team_1_points + team_2_points
    team_1_chance = round(team_1_points/sum_points, 2)
    team_2_chance = round(team_2_points/sum_points, 2)
    return team_1_chance, team_2_chance


def game(team_1: str, team_2: str) -> dict:
    score = goals()
    p1, p2 = chance_to_win(team_1, team_2)

    if p1 >= p2:
        score = sorted(score, reverse=True)

    else:
        score = sorted(score)

    final_score = np.random.choice(score, 2, replace=False, p=[p1, p2])
    return {team_1: final_score[0], team_2: final_score[1]}
