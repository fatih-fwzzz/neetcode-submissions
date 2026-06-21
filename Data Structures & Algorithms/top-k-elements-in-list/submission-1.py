class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        output = []

        nums.sort()

        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1

        top_ks = sorted(freq_map, key=freq_map.get, reverse=True)

        for top_k in top_ks:
            if len(output) == k:
                break
            
            output.append(top_k)

        return output