def winner(candidates):

    if len(candidates) != 3:
        return(False)

    for player in candidates:
        try:
            player['name']
            player['scores']
        except:
            return(False)

        if len(player['scores']) > 2 or len(player['scores']) < 1:
            return(False)

        for num in player['scores']:
            if num > 100:
                print('funciona')
                return(False)

    winner = ""
    best = 0
    for player in candidates:
        total = 0
        for points in player["scores"]: total += points
        if total > best and total < 101:
            best = total
            winner = player["name"]
    print(winner)


#        total += points for points in player["scores"]


c1 = {'name':"Bob", 'scores':[10, 65] }
c2 = {'name':"Bill", 'scores':[90, 5] } ###
c3 = {'name':"Jennifer", 'scores':[55] } ###
c4 = {'name':"John", 'scores':[5, 15] }
c5 = {'name':"Brad", 'scores':[3, 15] }
c6 = {'name':"Laurel", 'scores':[5, 12] }
c7 = {'name':"Charlie", 'scores':[5, 105] }
c8 = {'name':"Paul", 'scores':[80, 25] }
c9 = {'name':"Marc", 'scores':[80, 25] }
c10 = {'name':"Oliver", 'scores':[80, 25] }
c11 = {'name':"Bruce", 'scores':[] }
c12 = {'name':"Alfred", 'scores':[10, 15, 20] }
c13 = {'scores':[10, 20] }
c14 = {'name':"Cheater" }
c15 = {'name':"Robert", 'scores':[45] }
c16 = {'name':"Rob", 'scores':[40, 45] }
c17 = {'name':"Ned", 'scores':[10] }
c18 = {'name':"Gandalf", 'scores':[85] }

'''
class Participants:
    base = c
    numero = int

    def __init__(self, number):
        self.numero

Participants(range(1,19))


participants = []
n = 1
for c in range(1,19):
    participants.append(("c"+str(n)))
    n += 1

print(participants)
'''

winner([c1, c2, c3])
winner([])
winner([c1])
winner([c1, c2])
winner([c1, c2, c3, c4])
winner([c1, c11, c3])
winner([c1, c3, c12])
winner([c1, c2, c6])
winner([c1, c7, c2])
winner([c8, c9, c10])
winner([c1, c2, c13])
winner([c1, c14, c2])
winner([c15, c16, c17])
winner([c15, c17, c18])
winner([c16, c17, c18])
winner([c18, c17, c16])
