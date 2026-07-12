class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:

            maxx = stones[0]
            for i in range(1, len(stones)):
                if stones[i] > maxx:
                    maxx = stones[i]

            stones.remove(maxx)

            secondmaxx = stones[0]
            for i in range(1, len(stones)):
                if stones[i] > secondmaxx:
                    secondmaxx = stones[i]

            stones.remove(secondmaxx)

            if maxx != secondmaxx:
                stones.append(maxx - secondmaxx)

        if len(stones) == 0:
            return 0
        return stones[0]
        