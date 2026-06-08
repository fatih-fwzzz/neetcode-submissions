class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapped = {}

        for str in strs:
            cleaned = "".join(sorted(str))
            if cleaned not in mapped:
                mapped[cleaned] = [str]
            else:
                mapped[cleaned].append(str)

        return list(mapped.values())