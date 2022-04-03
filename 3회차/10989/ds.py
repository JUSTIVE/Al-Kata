import sys
def main():
    N = int(sys.stdin.readline().split()[0])
    numbers_str = list(map(lambda x: sys.stdin.readline().split()[0], range(N)))
    numbers = list(map(int, numbers_str))
    sorted_numbers = []
    sorted_numbers.append(numbers.pop(0))
    for number in numbers:
        sorted_numbers = FindPlace(sorted_numbers, number)
    print(sorted_numbers)

def FindPlace(sorted_numbers: list, number: int) -> list:
    if number <= sorted_numbers[0]:
        sorted_numbers.insert(0,number)
    elif sorted_numbers[-1] <= number:
        sorted_numbers.append(number)
    else: # number가 sorted_numbers 범위 안에 들어올 때
        mid = (len(sorted_numbers)-1)//2
        if len(sorted_numbers) == 2: # sorted_numbers가 두개밖에 없으면 그 안에 집어넣으면 됨
            sorted_numbers.insert(1,number)
        elif number == sorted_numbers[mid]: # mid index로 number를 찾으면, mid index에 집어넣으면 됨
            sorted_numbers.insert(mid, number)
        elif number < sorted_numbers[mid]:
            sorted_numbers = FindPlaceInSublist(sorted_numbers, 1, mid, number)
        elif sorted_numbers[mid] < number:
            sorted_numbers = FindPlaceInSublist(sorted_numbers, mid+1, -1, number)
        else:
            print('error')
    return sorted_numbers

def FindPlaceInSublist(sorted_numbers:list, index_init:int, index_end:int, number:int) -> list:
    SearchingNumbers = sorted_numbers[index_init:index_end]
    del sorted_numbers[index_init:index_end]
    return InsertSubList(sorted_numbers, FindPlace(SearchingNumbers, number), 1)

def InsertSubList(target: list, sublist: list, idx: int) -> list:
    list_result = target[0:idx]
    list_result.extend(sublist)
    list_result.extend(target[idx:])
    return list_result

if __name__ == '__main__':
    main()