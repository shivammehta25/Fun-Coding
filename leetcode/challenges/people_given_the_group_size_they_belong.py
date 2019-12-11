# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/submissions/
import collections

# ------------------- Slow Python3 Better than 23% Only --------------------


class Solution1:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        people = collections.defaultdict(list)
        for i, v in enumerate(groupSizes):
            people[v].append(i)
        final_value = []
        for v in people:
            while len(people[v]) > 0:
                final_value.append(people[v][:v])
                people[v] = people[v][v:]

        return final_value


# ------------------ Better Version better than 93% -----------------------

class Solution2:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        people = collections.defaultdict(list)
        final_answer = []
        for i, v in enumerate(groupSizes):
            people[v].append(i)
            if len(people[v]) == v:
                final_answer.append(people[v])
                del people[v]

        for v in people:
            final_answer.append(people[v])

        return final_answer
