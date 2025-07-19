class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_minutes = {}

        for user_id, time in logs:
            if user_id not in user_minutes:
                user_minutes[user_id] = set()
            user_minutes[user_id].add(time)

        answer = [0] * k
        for minutes in user_minutes.values():
            uam = len(minutes)
            if 1 <= uam <= k:
                answer[uam - 1] += 1

        return answer
