import os
import random

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen
cls()

teamlist = []

print("#####################")
print("### Nordstadtliga ###")
print("###   Spielplan   ###")
print("#####################")
print("")
team_count = int(input("Wieviele Mannschaften nehmen teil? "))
print("")

for x in range(team_count):
    print("Mannschaft",x+1,"Name? ")
    team = input()
    teamlist.append(team)
    print("")

list_of_pairs = [(teamlist[p1], teamlist[p2]) for p1 in range(len(teamlist)) for p2 in range(p1+1,len(teamlist))]

random.shuffle(list_of_pairs)

for x in range(len(list_of_pairs)):
    print("Paarung",x+1,": ", list_of_pairs[x][0], " gegen " , list_of_pairs[x][1])