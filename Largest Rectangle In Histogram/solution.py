class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
		stack = []
		length = []
		ans = 0
		height.append( 0 )
		n = len(height)
		for i in range(n):
			k = 0
			while stack and stack[-1] >= height[i]:
				k += length[-1];
				ans = max(ans, k*stack[-1]);
				length.pop()
				stack.pop()
			stack.append( height[i] )
			length.append( k + 1 )

		return ans
