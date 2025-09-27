class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        count = 0
        n = len(nums)
        for k in range(n - 1, 1, -1):  
            i, j = 0, k - 1  
            while i < j:
                
                if nums[i] + nums[j] > nums[k]:
                    count += j - i  
                    j -= 1
                else:
                    i += 1
        return count
nums1 = [2, 2, 3, 4]
nums2 = [4, 2, 3, 4]

print(Solution().triangleNumber(nums1))
print(Solution().triangleNumber(nums2)) 
