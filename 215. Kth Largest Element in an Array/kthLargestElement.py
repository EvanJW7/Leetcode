class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        if len(nums)>=2:
            k = int(k)
            return nums[-k]

        else:
            nums = ''.join(map(str, nums))
            return nums
        