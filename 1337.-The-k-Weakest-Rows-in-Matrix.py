class Solution:
    def kWeakestRows(self, mat:list[list[int]],k:int) -> list[int]:
        strength = {}
        
        for i, row in enumerate(mat):
            print(i,row)
            count = 0
            for j, val  in enumerate(row):
                if val:
                    count +=1
                else:
                    break
            strength[i] = count
        print(strength)
        

        
    
s = Solution()
s.kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3)

