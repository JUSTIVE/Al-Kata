import sys

n =int(sys.stdin.readline().rstrip())

def uniq_multiple_alphabet(alphabet: str)-> list:
    return list(set(alphabet))

def check_alphabet(alphabet:list, filteralphabet:list):
    if len(alphabet)!= len(filteralphabet):
        check_true_false=0
    else: 
        check_true_false=1
    return check_true_false

if __name__=='__main__':
    a= []
    for i in range(n):
        alphabet=sys.stdin.readline().rstrip()
        uniq_alphabet=uniq_multiple_alphabet(alphabet)
        check_true_false = check_alphabet(alphabet,uniq_alphabet)
        a.append(check_true_false)
    print(sum(a))





    
# import sys
# n =int(sys.stdin.readline().rstrip())
# result = n
# for i in range(0,n):
#     word=sys.stdin.readline().rstrip()
#     for j in range(0,len(word)-1):
#         print(word[j+1:], word[j], word[j+1])
#         if word[j]==word[j+1]:
#             pass
#         elif word[j] in word[j+1:]:
#             result-=1
#             break
# print(result)
