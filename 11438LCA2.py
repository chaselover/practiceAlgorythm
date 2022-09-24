import sys
sys.setrecursion(int(1e5))
input = sys.stdin.readline
LOG = 21 # (1000000의 log2를 취한 값의 올림값)(2의 i승 단위의 부모값을 저장하기 위한 크기.)

# 각 노드의 depth를 찾아 기록하기 위한 dfs
def find_depth(cur_node, depth):
    check[cur_node] = True
    depth[cur_node] = depth
    for next_node in graph[x]:
        if not check[next_node]:
            parent[next_node][0] = cur_node
            find_depth(next_node, depth+1)
# 공통조상 찾는 함수
def LCA(a,b):
    # b가 더 깊도록 설정
    if depth[a] > depth[b]:
        a,b = b,a
        # 더 깊은 b에 대해 동일해질때까지 올린다.
    for i in range(LOG-1,-1,-1):
        if depth[b] - depth[a] >= (1<<i):
            b = parent[b][i]
    # 노드가 같아질 때까지 올린다.
    if a==b:
        return a

    for i in range(LOG - 1,-1,-1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 이후에 부모가 찾고자 하는 조상.
    return parent[a][0]

def set_parent():
    find_depth(1,0)
    for i in range(1,LOG):
        for j in range(1, n+1):
            # preorder로 순회하며 root부터 top-down으로 부모노드를 채워 내려간다.
            parent[j][i] = parent[parent[j][i-1]][i-1]
    # 각 최초의 부모 노드로 부터 그 노드의 부모노드를 기록하도록 한다.()

n = int(input())

parent = [[0]*LOG for _ in range(n+1)] # 부모 노드 정보(n+1개의 노드에 대해 1,2,4,8,16..번째 부모값을 전부 기록.)
depth = [0] * (n+1) # 각 노드까지의 깊이
check = [0] * (n+1) # 깊이가 계산 되었는지 여부

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

set_parent()

m = int(input())

for i in range(m):
    a,b = map(int,input().split())
    print(LCA(a,b))