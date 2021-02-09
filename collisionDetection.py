#!/usr/bin/env python3

own = [int(i) for i in input().split()]

enemy = [[int(i) for i in input().split()] for _ in range(int(input()))]
print(enemy)

for i, e in enumerate(enemy):
    f=False
    for x in (own[0], own[0]+own[2]):
        for y in (own[1], own[1]+own[3]):
            if e[0] <= x <= e[0]+e[2] and e[1] <= y <= e[1]+e[3]:
                f = True
                break
        else:
            continue
        break
    if not f:
        for x in (e[0], e[0]+e[2]):
            for y in (e[1], e[1]+e[3]):
                if own[0] <= x <= own[0]+own[2] and own[1] <= y <= own[1]+own[3]:
                    f = True
                    break
            else:
                continue
            break
    if not f:
        if own[0] <= e[0] <= own[0]+own[2] and e[1] <= own[1] <= e[1]+e[3] or e[0] <= own[0] <= e[0]+e[2] and own[1] <= e[1] <= own[1]+own[3]:
            f=True
    if f:
        print("敵機", i+1, "が当たり")

