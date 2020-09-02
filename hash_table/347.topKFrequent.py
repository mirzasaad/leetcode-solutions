class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        feq = defaultdict(list)
        for i, cnt in counter.items():
            feq[cnt].append(i)

        res = []
        for frequency in reversed(range(1, len(nums) + 1)): 
            if frequency in feq:
                ls = feq[frequency]
                res.extend(ls)
            if len(res) >= k:
                break

        return res