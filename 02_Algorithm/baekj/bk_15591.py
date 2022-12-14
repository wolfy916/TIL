# MooTube (silver)
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    cnt = 0
    minV_L = [INF] * (N + 1)  # 최소 가중치를 받을 리스트
    visited = [0] * (N + 1)
    check = N

    q = deque([s])
    visited[s] = 1
    check -= 1
    while q:
        v = q.popleft()

        # 가중치가 k보다 작게 나오면 해당 노드 뒤로는 볼 필요가 없음
        if minV_L[v] < k:
            continue
        # INF 값이 아니면 k이상 이면 count
        elif minV_L[v] >= k and minV_L[v] != INF:
            cnt += 1

        # 회심의 가지치기 visited.count(0) == 1을 대체함
        if check == 0:
            continue

        for w, r in adjL[v]:
            if not visited[w]:
                q.append(w)
                minV_L[w] = min(minV_L[v], r)  # 부모 노드의 최소 가중치값과 비교
                visited[w] = 1
                check -= 1
    return cnt


N, Q = map(int, input().split())  # 1 ≤ N: 영상 번호, Q: 농부의 질문 개수 ≤ 5,000
adjL = [deque() for _ in '_'*(N+1)]
for _ in '_'*(N-1):
    p, q, r = map(int, input().split())  # 1 ≤ pi, qi ≤ N, 1 ≤ ri ≤ 1,000,000,000
    adjL[p].append((q, r))
    adjL[q].append((p, r))

INF = 1000000000
for _ in '_'*Q:
    k, s = map(int, input().split())  # 1 ≤ ki ≤ 1,000,000,000, 1 ≤ vi ≤ N
    print(bfs())