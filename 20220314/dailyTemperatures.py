from typing import List

class Solution:
    def dailyTemperatures_book(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            # 현재 온도가 스택 값보다 높다면 정답 처리
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer




if __name__ == "__main__":
    s = Solution()
    intArray = [73,74,75,71,69,72,76,73]
    print(s.dailyTemperatures_book(intArray))
