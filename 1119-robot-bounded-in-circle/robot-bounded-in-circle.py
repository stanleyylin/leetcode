class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        dir = 0 # 0=N,1=E,2=S,3=W
        for c in instructions:
            if c == 'G':
                if dir == 0:
                    y += 1
                elif dir == 1:
                    x += 1
                elif dir == 2:
                    y -= 1
                elif dir == 3:
                    x -= 1
            elif c == 'L':
                dir = (dir - 1) % 4
            elif c == 'R':
                dir = (dir + 1) % 4
        
        if (x == 0 and y == 0) or dir != 0:
            return True
        else:
            return False