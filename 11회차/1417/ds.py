import sys
from typing import List

def main():
    N = int(sys.stdin.readline()[0])

    candidates = list(map(int, map(lambda x: sys.stdin.readline().split()[0], range(N))))
    origin = candidates[0]
    def find_max_index(target_list: List[int]) -> int:
        max_index = target_list.index(max(target_list))
        if max_index == 0:
            return target_list.index(max(target_list[1:]))-1
        else:
            return max_index

    def disrupt():
        target = find_max_index(candidates)
        candidates[0] = candidates[0]+1
        candidates[target] = candidates[target] - 1

    # def disrupt(candidates_input: List[int]) -> List[int]:
    #     candidates_inst = candidates_input.copy()
    #     target = find_max_index(candidates_inst)
    #     candidates_inst[0] = candidates_inst[0]+1
    #     candidates_inst[target] = candidates_inst[target] - 1
    #     return candidates_inst

    def secret_mission():
        def secret_sub_mission():
            disrupt()
            secret_mission()

        if max(candidates) != candidates[0]:
            secret_sub_mission()
        elif max(candidates) == candidates[0]:
            def check_ties_exist(target_list_: list) -> bool:
                if len(target_list_) > 1:    
                    vip = target_list_[0]
                    target_list_sub = target_list_[1:]
                    if vip == max(target_list_sub):
                        return True
                    elif vip > max(target_list_sub):
                        return False
                else:
                    return False
            is_tie = check_ties_exist(candidates)
            if is_tie:
                secret_sub_mission()
            else:
                pass

    # def secret_mission(candidates_in: List[int]) -> List[int]:
    #     def secret_sub_mission(candidates_input: List[int]) -> List[int]:
    #         candidates_disrupted = disrupt(candidates_input)
    #         return secret_mission(candidates_disrupted)

    #     if max(candidates_in) != candidates_in[0]:
    #         candidates_result = secret_sub_mission(candidates_in)
    #     elif max(candidates_in) == candidates_in[0]:
    #         def check_ties_exist(target_list_: list) -> bool:
    #             if len(target_list_) > 1:    
    #                 vip = target_list_[0]
    #                 target_list_sub = target_list_[1:]
    #                 if vip == max(target_list_sub):
    #                     return True
    #                 elif vip > max(target_list_sub):
    #                     return False
    #             else:
    #                 return False
    #         is_tie = check_ties_exist(candidates_in)
    #         if is_tie:
    #             candidates_result = secret_sub_mission(candidates_in)
    #         else:
    #             candidates_result = candidates_in
    #     return candidates_result
    # candidates_result = secret_mission(candidates)
    secret_mission()
    print(candidates[0] - origin)

if __name__ == '__main__':
    main()