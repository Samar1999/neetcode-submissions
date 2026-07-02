class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        posi_speed = []
        stack = []

        for i in range(0,len(position)):
            posi_speed.append((position[i], speed[i]))
        
        posi_speed = sorted(posi_speed)

        time_req = 0
        for i in range(len(posi_speed) - 1, -1, -1):
            time_req = (target - posi_speed[i][0])/ posi_speed[i][1]
            if stack and time_req > stack[-1]:
                stack.append(time_req)
            if not stack: stack.append(time_req)

        return len(stack)