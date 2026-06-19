class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        is_previous = False
        temp_list, output = [], []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, mid, right = i, i+1, len(nums)-1

            while(mid<right):
                if [nums[left], nums[mid], nums[right]] == temp_list:
                    is_previous = True
                else:
                    is_previous = False

                temp_list = [nums[left], nums[mid], nums[right]]
                temp_list.sort()

                if sum(temp_list) == 0:
                    if not is_previous:
                        output.append(temp_list)

                    mid += 1
                    right -= 1

                elif sum(temp_list) <= 0:
                    mid += 1
                else:
                    right -= 1

        return output