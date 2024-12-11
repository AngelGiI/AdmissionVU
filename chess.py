# -*- coding: utf-8 -*-
"""
Created on Sat May 21 19:38:53 2022

@author: Angel
"""

class player_result:
    def __init__(self, name: str, points: float, resistance_points: float, sonnenborn_berger: float, black: int):
        self.name = name
        self.points = points
        self.resistance_points = resistance_points
        self.sonnenborn_berger = sonnenborn_berger
        self.black = black

    def __str__(self):
        return 'player_result(name=\'' + self.name + '\', points=' + str(self.points) + ', resistance_points=' + \
               str(self.resistance_points) + ', sonnenborn_berger=' + str(self.sonnenborn_berger) + \
               ', black=' + str(self.black) + ')'

    def __eq__(self, other):
        return self.name == other.name and self.points == other.points and \
               self.resistance_points == other.resistance_points and \
               self.sonnenborn_berger == other.sonnenborn_berger and self.black == other.black

def merge(left, right, pos):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left][pos] >= right[index_right][pos]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result

def merge_sort(array,pos):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    return merge(
        left=merge_sort(array[:midpoint],pos),
        right=merge_sort(array[midpoint:],pos),
        pos=pos)

def determine_output(input: str):
    content = input.split('\n')
    players={}
    while content[0] != '':
        # Players are stored (empty).
        players[content.pop(0)]={'pt':0.0,'win':[],'draw':[],'lose':[],'b':0}
    del content[0]
    for i in range(len(content)):
        if content[i] != '':
            cositas = content[i].split()
            # Results are filled line by line.
            players[cositas[1]]['b']+=1
            if cositas[2] == '1':
                players[cositas[0]]['pt']+=1
                players[cositas[0]]['win'].append(cositas[1])
                players[cositas[1]]['lose'].append(cositas[0])
            elif cositas[2] == '0':
                players[cositas[1]]['pt']+=1
                players[cositas[1]]['win'].append(cositas[0])
                players[cositas[0]]['lose'].append(cositas[1])
            else:
                players[cositas[0]]['pt']+=0.5
                players[cositas[1]]['pt']+=0.5
                players[cositas[0]]['draw'].append(cositas[1])
                players[cositas[1]]['draw'].append(cositas[0])
    # Calculation of resistance and Sonnenborn-Berger points.
    totals=[]
    for i in players.keys():
        rp=0
        sb=0
        for j in players[i]['win']:
            rp+=players[j]['pt']
            sb+=players[j]['pt']
        for j in players[i]['draw']:
            rp+=players[j]['pt']
            sb+=0.5*players[j]['pt']
        for j in players[i]['lose']:
            rp+=players[j]['pt']
        # Players and their puntuations are stored in order to compare them.
        totals.append([i,players[i]['pt'],rp,sb,players[i]['b']])
    # Players are sorted.
    for i in range(4,0,-1):
        # Number of black games first -> number of points last since each level
        # of merge_sort overrides previous level of merge except when points 
        # between 2 or more players are the same.
        totals = merge_sort(totals,i)
    # # Results are turned into class player_result.
    for i in range(len(totals)):
        totals[i]=player_result(totals[i][0],totals[i][1],totals[i][2],
                                totals[i][3],totals[i][4])
    return totals
        