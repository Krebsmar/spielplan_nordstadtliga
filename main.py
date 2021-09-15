list = ["Team A","Team B", "Team C"]

list_count = len(list)

print(list_count)
print(list[0])


for x in range(len(list)):
    print (list[x])

list.append("Team D")

for x in range(len(list)):
    print (list[x])

list_of_pairs = [(list[p1], list[p2]) for p1 in range(len(list)) for p2 in range(p1+1,len(list))]

print(list_of_pairs)