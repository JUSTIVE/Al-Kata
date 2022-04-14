import re
import sys 

def find_nope(n,i,number):
    if i == len(n)-1:
        return
    else:
        a = len(n[i]) % 4
        if a!=0:
            number+=(4-a)
    return find_nope(n,i+1,number)

if __name__=='__main__':
    
    m = sys.stdin.readline().rstrip()
    n= re.split('(?=[A-Z])',m)
    result=find_nope(n,0,0)
    
    print(result)

