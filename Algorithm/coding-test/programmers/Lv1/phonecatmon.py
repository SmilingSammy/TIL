def solution(nums):
    catch_num = len(nums) // 2
    return min(len(set(nums)), catch_num)