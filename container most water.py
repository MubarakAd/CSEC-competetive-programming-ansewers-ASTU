class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        counter=0
        size=0
        right=len(height)-1
        while left<=right:
            if height[left]<height[right]:
                counter=(right-left)*height[left]
                left+=1
                size=max(size,counter)
            else:
                counter=(right-left)*height[right]
                right-=1
                size=max(size,counter)
        return size
        
