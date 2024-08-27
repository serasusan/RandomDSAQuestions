class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        elif numRows==1:
            return [[1]]
        
        prevArr = self.generate(numRows-1)
        newArr = [1]*numRows
        for i in range(1,n-1):
            newArr[i]= prevArr[i-1]+prevArr[i]
        prevArr.append(newArr)
        return prevArr

            

