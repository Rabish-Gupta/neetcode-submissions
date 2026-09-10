from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq =  Counter(nums)
        new_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        lst = list(new_freq.keys())
        return lst[:k]