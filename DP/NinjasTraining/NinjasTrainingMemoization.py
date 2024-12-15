class Solution:
    def ninjaTraining(self, matrix):
        days = len(matrix)

        dp = [[-1 for j in range(4)] for i in range(days)]
        if days == 0:
            return 0
        return self.func(days-1,3,matrix,dp)
    
    def func(self,day,last,matrix,dp):
        # base case
        if day == 0:
            maxi=0
            for i in range(3):
                if i!=last:
                    maxi = max(maxi,matrix[0][i])
            dp[day][last]=maxi
            return dp[day][last]
        if dp[day][last]!=-1:
            return dp[day][last]
        maxi = 0
        for i in range(3):
            if i!=last:
                activity = matrix[day][i] + self.func(day-1,i,matrix,dp)
                maxi = max(activity,maxi)
        dp[day][last] = maxi
        return dp[day][last]