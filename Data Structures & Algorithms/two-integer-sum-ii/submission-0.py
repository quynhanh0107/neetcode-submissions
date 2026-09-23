class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        preMap = defaultdict(int)

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in preMap:
                return [preMap[diff], i+1]
            preMap[n] = i + 1
        return []
        