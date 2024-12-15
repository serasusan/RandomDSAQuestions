class Solution:
    def ninjaTraining(self, matrix):
        days = len(matrix)
        
        if days == 0:
            return 0
        return self.func(days-1,3,matrix)
    
    def func(self,day,last,matrix):
        # base case
        if day == 0:
            maxi=0
            for i in range(3):
                if i!=last:
                    maxi = max(maxi,matrix[0][i])
            return maxi
        maxi = 0
        for i in range(3):
            if i!=last:
                activity = matrix[day][i] + self.func(day-1,i,matrix)
                maxi = max(activity,maxi)
        return maxi