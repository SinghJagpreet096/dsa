"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> list[list[int]]:


        return list(zip(*matrix[::-1]))
        
                

            # print(matrix[j][i])
                
        
        
        
        # pass
if __name__ == "__main__":
    s = Solution()
    print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))
        