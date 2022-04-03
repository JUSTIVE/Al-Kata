import sys
from typing import List

def main():
    N = int(sys.stdin.readline().split()[0])
    words = list(map(lambda x: sys.stdin.readline().split()[0], range(N)))

    def JoinChars(word: str) -> str:
        word_list = list(word)

        def DelChar(idx: int, word_list: List[str]) -> List[str]:
            if idx == len(word_list)-1:
                pass

            elif word_list[idx] == word_list[idx+1]:
                del word_list[idx+1]
                word_list = DelChar(idx, word_list)

            elif word_list[idx] != word_list[idx+1]:
                word_list = DelChar(idx+1, word_list)

            return word_list

        word_list_joined = DelChar(0, word_list)
        return ''.join(word_list_joined)

    JoinedWords = list(map(JoinChars, words))

    def IsGroup(Name:str) -> bool:
        word_list = list(Name)
        
        def CharExist(Name: str, char: str, idx: int) -> bool:
            return True if Name.find(char, idx+1) > 0 else False
        
        isgroup = True

        for idx, word in enumerate(word_list):
            if CharExist(Name, word, idx):
                isgroup = False
                break

        return isgroup

    print(len(list(filter(IsGroup, JoinedWords))))




if __name__ == '__main__':
    main()