class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        left, right = 0, len(heights)-1

        while(left<right):
            width = right-left
            limit_height = min(heights[left], heights[right])
            area = width*limit_height

            if area > output:
                output = area

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return output
            