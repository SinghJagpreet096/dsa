class Solution:
    def kWeakestRows(self, mat:list[list[int]],k:int) -> list[int]:
        strength = {}
        
        for i, row in enumerate(mat):
            # print(i,row)
            count = 0
            for j, val  in enumerate(row):
                if val:
                    count +=1
                else:
                    break
            strength[i] = count
        result = sorted(strength.items(), key= lambda item :item[1])[:k]
        return [i[0] for i in result]
        

        

        
    
s = Solution()
print(s.kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3))

