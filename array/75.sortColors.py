from typing import List

def sortColors(nums: List[int]) -> None:
    left, runner, right = 0, 0, len(nums) - 1

    while runner <= right:
        if nums[runner] == 0:
            nums[runner], nums[left] = nums[left], nums[runner]
            runner += 1
            left += 1
        elif nums[runner] == 1:
            runner += 1
        elif nums[runner] == 2:
            nums[runner], nums[right] = nums[right], nums[runner]
            right -= 1
    return nums