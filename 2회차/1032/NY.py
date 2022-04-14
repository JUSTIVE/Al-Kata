import sys
N = int(sys.stdin.readline().rstrip())
first = list(sys.stdin.readline().rstrip())
name_= []
for i in range(N-1):
    name_list = list(sys.stdin.readline().rstrip())    
    for j in range(len(name_list)):
        if first[j] == name_list[j]:
            pass
        else:
            first[j]='?'
print(''.join(first))