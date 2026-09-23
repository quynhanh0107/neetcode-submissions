class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        res = [0] * leng
        pref = [0] * leng
        suff = [0] * leng

        pref[0] = 1
        suff[leng-1] = 1

        for i in range(1, leng):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range(leng-2, -1, -1):
            suff[i] = nums[i+1] * suff[i+1]
        for i in range(leng):
            res[i] = pref[i] * suff[i]
        return res


        