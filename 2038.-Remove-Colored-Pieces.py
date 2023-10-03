"""
There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. 
You are given a string colors of length n where colors[i] is the color of the ith piece.

Alice and Bob are playing a game where they take alternating turns removing pieces from the line. 
In this game, Alice moves first.

Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. 
She is not allowed to remove pieces that are colored 'B'.
Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. 
He is not allowed to remove pieces that are colored 'A'.
Alice and Bob cannot remove pieces from the edge of the line.
If a player cannot make a move on their turn, that player loses and the other player wins.
Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.
"""

class Solution:
    def winnerOfGame(self, colors: list[str]) -> bool:
        colors = [col for col in colors]
        # print(colors)
        player = True
        i = 1
        n = len(colors)
        while i < n-1:
            j = i
            while j < n-1:
                if player and (colors[j] == 'A' and colors[j-1] == "A" and colors[j+1] == "A"):
                    # print("a",colors,j)
                    colors.pop(j)
                    n -= 1
                    j += 1
                    player = False
                elif not player and (colors[j]=="B" and colors[j+1] == "B" and colors[j-1] == "B"):
                    # print("b",colors,j)
                    colors.pop(j)
                    n -= 1
                    j += 1
                    player = True
                else:
                    j += 1
                    continue
                j += 1
            i += 1
        return not player
                
        # return not player

if __name__ == "__main__":
    s = Solution()
    # print(s.winnerOfGame("AAABABB"))
    # print(s.winnerOfGame("AA"))
    # print(s.winnerOfGame("ABBBBBBBAAA"))
    print(s.winnerOfGame("BBBBAAAA"))


