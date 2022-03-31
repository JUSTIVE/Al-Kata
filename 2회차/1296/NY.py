import sys

n = sys.stdin.readline().rstrip()
N= int(sys.stdin.readline())

gewaehlte_woman=list()
prozent= 0
for woman_idx in range(N):
    woman_name = sys.stdin.readline().rstrip()
    x =n+woman_name

    L = x.count('L')
    O= x.count('O')
    V= x.count('V')
    E = x.count('E')
    woman_prob = ((L+O)*(L+V)*(O+V)*(O+E)*(V+E))%100

    if  woman_prob== prozent:
        gewaehlte_woman.append(woman_name)

    elif woman_prob>prozent:
        gewaehlte_woman=list()
        gewaehlte_woman.append(woman_name)
        prozent=woman_prob

print(sorted(gewaehlte_woman)[0])