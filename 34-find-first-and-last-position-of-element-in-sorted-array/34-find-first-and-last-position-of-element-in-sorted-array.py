class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getRightBorder(nums, target):
            left, right = 0, len(nums) - 1
            rightBoder = -2
            while left <= right:
                middle = (left + right) // 2

                if nums[middle] > target:
                    right = middle - 1

                else:
                    left = middle + 1
                    rightBoder = left
            return rightBoder
    
        def getLeftBorder(nums, target):
            left, right = 0, len(nums) - 1
            leftBoder = -2
            while left <= right:
                middle = (left + right) // 2
                if nums[middle] >= target:
                    right = middle - 1
                    leftBoder = right
                else:
                    left = middle + 1
            return leftBoder
        
        rightBorder = getRightBorder(nums, target)
        leftBorder = getLeftBorder(nums, target)
        if (leftBorder == -2 or rightBorder == -2):
            return [-1,-1]
        if (rightBorder - leftBorder>1):
            return [leftBorder +1, rightBorder - 1]
        return [-1,-1]