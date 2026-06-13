class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        starti=0
        startj=0
        endi=len(matrix)-1
        endj=len(matrix[0])-1
        arr=matrix

        while(starti<=endi and startj<=endj):
            midi= (starti+endi)//2
            midj= (startj+endj)//2

            if(arr[midi][midj]==target):
                return True
            elif(arr[midi][midj]<target):
                if(arr[midi][endj]<target):
                    starti=midi+1
                else:
                    startj=midj+1
            elif(arr[midi][midj]>target):
                 if (arr[midi][0]>target):
                    endi=midi-1
                 else:
                    endj=midj-1
        return False
