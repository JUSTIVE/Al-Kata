import re
import sys
m=sys.stdin.readline().strip()
n=re.compile('(pi|ka|chu)+')
if n.fullmatch(m):
    print('Yes')
else:
    print('NO')
