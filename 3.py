#A*
import heapq

goal = (1,2,3,4,5,6,7,8,0)

def heuristic(s):
    return sum(abs(i//3-(v-1)//3)+abs(i%3-(v-1)%3)
               for i,v in enumerate(s) if v != 0)

start = tuple(map(int, input("Enter 9 puzzle values (0 for blank): ").split()))

if len(start) != 9 or sorted(start) != list(range(9)):
    print("Invalid input")
else:
    pq = [(heuristic(start), 0, start, [start])]
    best = {start: 0}
    solution = None

    while pq:
        f, g, s, path = heapq.heappop(pq)

        if g != best[s]:
            continue

        if s == goal:
            solution = path
            break

        z = s.index(0)
        r, c = divmod(z, 3)

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                nz = nr*3+nc
                new = list(s)
                new[z], new[nz] = new[nz], new[z]
                new = tuple(new)
                ng = g+1

                if ng < best.get(new, float('inf')):
                    best[new] = ng
                    heapq.heappush(pq, (ng+heuristic(new), ng,
                                        new, path+[new]))

    if solution:
        print("Moves:", len(solution)-1)
        for s in solution:
            for i in range(0,9,3):
                print(s[i:i+3])
            print()
    else:
        print("No solution found")