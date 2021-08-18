import sys
input = sys.stdin.readline


def manacher(string):
    n = len(string)
    a = [0] * n  # i번째 문자를 중심으로 하는 가장 긴 팰린드롬 반지름 크기.
    c = 0  # 중심점(center) 초기화
    r = 0  # 시작점에서 가장 먼 반경(펠린드롬 끝나는 인덱스중 가장 큰 값.)
    answer = 0
    for now in range(n):
        if string[now] != '#':
            answer +=1
        # i번째 문자가 now 아래쪽에 있는 문자를 중심으로 하는 팰린드롬 범위 밖의 문자라는 뜻.
        # 때문에 now 이전에 얻은 정보를 재활용하지 못하고 i를 기준으로 초기화시켜 재계산함.
        if r < now:
            a[now] = 0
        # i번째 문자가 i미만의 문자를 중심으로 하는 팰린드롬에 속한다면?
        # 1. i를 중심으로 하는 가장 긴 팰린드롬이 기존 최장 팰린드롬인 c를 중심으로 하는 가장 긴 팰린드롬에 완전히 속하는 경우 -> i의 c점에 대한 대칭점 now'을 기준으로 하는 펠린드롬은 i를 기준으로 하는 팰린드롬과 완전한 대칭. a[now]=a[now']인데 p[now']은 이전에 구해놓았기 때문에 연산 안해도됨.
        # 2. i를 중심으로 하는 가장 긴 팰린드롬이 c를 중심으로 한느 가장 긴 팰린드롬에 일부만 포함된느 경우 -> 초기 반지름 a[now] = ((c+a[c])-now)가 보장이됨(가장 긴 펠린드롬의 오른쪽 한계로부터 i만큼 왼쪽으로 줄인 반지름에서 (c+a[c])-now+1부터 비교 시작)
        # 3. i를 중심으로 한느 가장 긴 팰린드롬이 c < i인 c를 중심으로 하는 가장 긴 팰린드롬과 겹치는 경우. (c의 날개와 i의 날개가 동일지점인 경우)
        # 역시 case 2처럼 a[now] = ((c+a[c])-now)만큼의 반지름이 보장이 됨. 그 이후로 부터 비교하면 됨. now'은 (2*c)-i이므로 now'의 날개와 r-i값중 더 작은 곳을 보장받고 움직이면 됨.
        else:
            a[now] = min(a[(2*c) - now], r - now)
            answer += a[now]//2

        # i번째 인덱스 기준 가장 긴 펠린드롬 반지름을 펼쳤을 시 0~len(s)의 범위 안에 존재해야하며
        # i기준 a[now](반지름)만큼 펼친 그 양옆문자도 같으면?(-1.+1인덱스가 같으면)
        # a[now]+1(반지름 확장)
        while(now-a[now]-1>=0 and now+a[now]+1 < n and string[now-a[now]-1] == string[now+a[now]+1]):
            a[now] = a[now] + 1
            if string[now + a[now]] != '#':
                answer +=1
        # 시작점에서 가장 먼 반경인 now + a[now]가 기존 최장 반지름 길이 r보다 크므로
        # r초기화, 중심점 c는 현재 최장 펠린드롬의 중심점인 i로 초기화.
        # 결국 r,c는 현 시점에서 가장 먼 팰린드롬의 날개값(가장 멀리갈때 초기화됨.)
        # a[now]가 0이어도 r보다 i가 커지면 갱신됨.
        if (r < now + a[now]):
            r = now + a[now]
            c = now
    return answer

s = input().rstrip()
print(manacher('#' + '#'.join(s)+'#'))