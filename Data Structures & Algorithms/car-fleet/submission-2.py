class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(key=lambda x: x[0], reverse=True)
        #print(cars)

        stack = []
        for pos, speed in cars:
            t = (target - pos) / speed
            stack.append(t)
            if len(stack) > 1:
                last_t = stack[-2]
                if t <= last_t:
                    stack.pop()

            

        #print(stack)
        return len(stack)