class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        tot = 0
        now = 0
        start = 0
        for i in range(len(gas)):
            v = gas[i] - cost[i]
            now = now + v
            if now < 0:
                start = i+1
                now = 0
            tot += v
        if tot >= 0:
            return start
        else: 
            return -1

if __name__ == '__main__':
	print Solution().canCompleteCircuit([1,2,3,3], [2,1,5,1])


