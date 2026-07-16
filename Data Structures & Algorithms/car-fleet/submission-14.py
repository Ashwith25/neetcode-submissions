class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        map = {}
        for idx, i in enumerate(position):
            map[i] = speed[idx]

        position.sort()
        position = position[::-1]

        times = [(target - i) / map[i] for i in position]

        stack = [times[0]]
        i=0
        while i<len(position):
            if stack and stack[-1]<times[i]:
                stack.append(times[i])
            i+=1

        return len(stack)