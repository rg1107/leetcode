class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Didnt understand the problem completely, went to code too soon without considering all things
        # https://leetcode.com/problems/maximum-score-from-removing-substrings/solutions/6992626/greedy-two-pass-stack-c-java-python-js-o-n-explained
        def solve(text: str, pattern: str, score: int):
            stack = []
            points = 0
            for char in text:
                if stack and stack[-1] == pattern[0] and char == pattern[1]:
                    stack.pop()
                    points += score
                else:
                    stack.append(char)
            return points, "".join(stack)

        if x >= y:
            points1, remaining_s = solve(s, "ab", x)
            points2, _ = solve(remaining_s, "ba", y)
        else:
            points1, remaining_s = solve(s, "ba", y)
            points2, _ = solve(remaining_s, "ab", x)
            
        return points1 + points2