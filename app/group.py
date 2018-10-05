import ast

from collections import deque


with open('../data.txt', 'r') as f:
    countries = f.read()

countries = ast.literal_eval(countries)

final_grid = [['A1', 'B2'], ['C1', 'D2'], ['E1', 'F2'], ['G1', 'H2'],
              ['B1', 'A2'], ['D1', 'C2'], ['F1', 'E2'], ['H1', 'G2']]

groups_names = ["A", "B", "C", "D", "E", "F", "G", "H"]

default_teams = ['Египет', 'Россия', 'Саудовская Аравия', 'Уругвай',
                 'Иран', 'Марокко', 'Португалия', 'Испания',
                 'Австралия', 'Дания', 'Франция', 'Перу',
                 'Аргентина', 'Хорватия', 'Исландия', 'Нигерия',
                 'Бразилия', 'Коста-Рика', 'Сербия', 'Швейцария',
                 'Германия', 'Южная Корея', 'Мексика', 'Швеция',
                 'Бельгия', 'Англия', 'Панама', 'Тунис',
                 'Колумбия', 'Япония', 'Польша', 'Сенегал']

stats = {'games': 0, 'won': 0, 'draw': 0, 'lost': 0,
         'gf': 0, 'ga': 0, 'diff': 0, 'points': 0}


def grouping(teams_list):
    group_stage = {}
    teams = deque(teams_list)
    for i in groups_names:
        group_stage[i] = {teams.popleft(): stats.copy() for _ in range(4)}
    return group_stage
