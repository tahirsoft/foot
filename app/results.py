import numpy as np
import ast

from random import shuffle
from itertools import combinations

from app.group import groups_names, final_grid, grouping


def goals() -> list:
    score = np.random.choice(8, 2, p=[0.27, 0.35, 0.22, 0.13, 0.021,
                                      0.0056, 0.002, 0.0014])
    return score


def penalty_goals() -> list:
    score = np.random.choice(6, 2, replace=False, p=[0.001, 0.01, 0.07,
                                                     0.119, 0.4, 0.4])
    return score


def chance_to_win(team_1: str, team_2: str) -> tuple:
    with open('app/data.txt', 'r') as f:
        countries_data = f.read()
    countries_data = ast.literal_eval(countries_data)

    team_1_points = int(countries_data[team_1]["points"])
    team_2_points = int(countries_data[team_2]["points"])
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


def games_in_group(countries: list) -> list:
    group_games = combinations(countries, 2)
    return group_games


def group_games_results(group: str) -> list:
    countries = group.keys()
    group_games = games_in_group(countries)
    games_results = [game(i[0], i[1]) for i in group_games]
    shuffle(games_results)
    return games_results


def group_stats(team_list: list) -> dict:
    table = grouping(team_list)
    for group in groups_names:
        for result in group_games_results(table[group]):
            team_1, team_2 = result.keys()
            table[group][team_1]["games"] += 1
            table[group][team_2]["games"] += 1
            table[group][team_1]["gf"] += result[team_1]
            table[group][team_2]["gf"] += result[team_2]
            table[group][team_1]["ga"] += result[team_2]
            table[group][team_2]["ga"] += result[team_1]
            table[group][team_1]["diff"] += result[team_1] - result[team_2]
            table[group][team_2]["diff"] += result[team_2] - result[team_1]

            if result[team_1] > result[team_2]:
                table[group][team_1]["won"] += 1
                table[group][team_2]["lost"] += 1
                table[group][team_1]["points"] += 3

            elif result[team_2] > result[team_1]:
                table[group][team_2]["won"] += 1
                table[group][team_1]["lost"] += 1
                table[group][team_2]["points"] += 3

            else:
                table[group][team_1]["draw"] += 1
                table[group][team_2]["draw"] += 1
                table[group][team_2]["points"] += 1
                table[group][team_1]["points"] += 1
    return table


def final_staging(team_list: list) -> tuple:
    mini_table = {}
    table = group_stats(team_list)
    for group_name in groups_names:
        place = 1
        group = table[group_name]

        for k, v in sorted(group.items(),
                           key=lambda x: (x[1]['points'], x[1]['diff']),
                           reverse=True):

            if place < 3:
                mini_table[group_name + str(place)] = k
                place += 1

    teams = sum(
        [[mini_table[i[0]], mini_table[i[1]]] for i in final_grid],
        []
    )
    return table, teams


def final_stage_results(teams_grid: list) -> dict:
    results = [game(teams_grid[i], teams_grid[i+1])
               for i in range(0, len(teams_grid), 2)]

    for i in results:

        if len(set(i.values())) == 1:
            penalty = penalty_goals()
            i["penalty"] = f'{penalty[0]}:{penalty[1]}'

    return results


def kick_out(results: dict) -> list:
    winners = []
    losers = []
    for i in results:
        team_1, team_2, *penalty = i.keys()

        if i[team_1] == i[team_2]:
            penalty_result = i[penalty[0]]

            if penalty_result[0] > penalty_result[2]:
                winners.append(team_1)

            else:
                winners.append(team_2)

        elif i[team_1] > i[team_2]:
            winners.append(team_1)

        else:
            winners.append(team_2)

        if len(results) == 2:
            if team_1 in winners:
                losers.append(team_2)
            else:
                losers.append(team_1)
    if losers:
        return winners, losers

    return winners


def final_stage_games(team_list):
    table, teams_grid_one_eighth = final_staging(team_list)
    results_one_eighth = final_stage_results(teams_grid_one_eighth)

    teams_grid_quaterfinal = kick_out(results_one_eighth)
    results_quaterfinal = final_stage_results(teams_grid_quaterfinal)

    teams_grid_semifinal = kick_out(results_quaterfinal)
    results_semifinal = final_stage_results(teams_grid_semifinal)

    finalists, third_placed = kick_out(results_semifinal)
    third_place = final_stage_results(third_placed)
    final = final_stage_results(finalists)

    return (table, results_one_eighth, results_quaterfinal,
            results_semifinal, third_place, final)
