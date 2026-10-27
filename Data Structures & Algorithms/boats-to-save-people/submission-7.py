class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people)==1:
            return 1
        people.sort()
        left=0
        right=len(people)-1
        boats=0
        while right>=left:
            if people[left]+people[right]<=limit:
                left=left+1
                right=right-1
                boats=boats+1
            else:
                boats=boats+1
                right=right-1
        return boats