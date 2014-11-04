class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        c, n = [], len(ratings)
        for i in range(n):
        	if i == 0 or ratings[i] <= ratings[i-1]:
        		c.append(1)
        	else:
        		c.append( c[i-1]+1 )

        for i in range(n-1):
        	if ratings[n-2-i] > ratings[n-1-i]:
        		c[n-2-i] = max(c[n-2-i], c[n-1-i] + 1)
        return sum(c)

if __name__ == '__main__':
	print Solution().candy([1,2,2])

