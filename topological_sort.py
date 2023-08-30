from collections import deque

n, m = map(int, input().split())

tree = [[] for i in range(n)]
degree = [0 for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    degree[b] += 1

que = deque()
for i in range(n):
    if degree[i] == 0:
        que.append(i)

ans = []
while que:
    x = que.popleft()
    ans.append(x)

    for nx in tree[x]:
        degree[nx] -= 1
        if degree[nx] == 0:
            que.append(nx)

if sum(degree) != 0:
    print(-1)
    exit()

for i in ans:
    print(i)