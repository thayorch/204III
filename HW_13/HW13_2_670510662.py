#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW13_2
# 204111 Sec 001

def count_vote(pref_matrix: list) -> list:
    ranking = {}
    for vote in pref_matrix:
        for i in range(len(vote)):
            ranking[vote[i]] = ranking.get(vote[i], 0)
            ranking[vote[i]] += (len(vote)-i)
    ranked_pokemon = sorted(list(map(lambda x,y: (x,y),ranking,ranking.values())))
    ranked_pokemon = sorted(ranked_pokemon, key=lambda x: x[1], reverse=True)
    return ranked_pokemon

if __name__ == '__main__':
    pref_matrix = [
        ['Mewtwo', 'Suicune', 'Pikachu'],
        ['Mewtwo', 'Suicune', 'Pikachu'],
        ['Mewtwo', 'Suicune', 'Pikachu'],
        ['Mewtwo', 'Suicune', 'Pikachu']
    ]
    print(count_vote(pref_matrix))
    print(count_vote([['a','b']]))
