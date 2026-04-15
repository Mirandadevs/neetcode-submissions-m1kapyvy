class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        res = []
        for freq in reversed(range(len(buckets))):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
