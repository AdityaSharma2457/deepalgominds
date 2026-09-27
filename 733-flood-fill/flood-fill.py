from collections import deque
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

        original = image[sr][sc]
        image[sr][sc] = color
        if original == color:
            return image
        q=deque([[sr,sc]])
        m=len(image)
        n=len(image[0])
        direc=((1,0),(0,1),(0,-1),(-1,0))

        while(q):
            i,j=q.popleft()

            for k in direc:
                ni=i+k[0]
                nj=j+k[1]

                if (ni>=0 and nj>=0 and ni<m and nj<n and image[ni][nj]==original):
                    image[ni][nj]=color
                    q.append([ni,nj])
        return image