from itertools import permutations, combinations

inp = list(map(int, input().split()))
ac = []
for i in range(2, len(inp) + 1):
    ac.extend(list(combinations(inp, i)))
maxWeight = 0
for c in ac:
    sumc = sum(c)
    for i in range(1, len(c)):
        for j in permutations(c, i):
            t = sum(j)
            if t * 2 == sumc:
                maxWeight = max(maxWeight, t)
print(maxWeight)
