class Solution:
    def groupAnagrams(self, strs):

        answer = []
        Anagrams = {}

        # input 배열로 for문 수행
        for element in strs:
            # 각 element의 문자열을 나눈 후 오름차순 정렬 후 합친다.
            temp = "".join(sorted(list(element)))
            # Anagrams 딕셔너리에 temp라는 key가 있을 때
            if temp in Anagrams.keys():
                # Anagrams[temp] 에 element를 추가한다.
                Anagrams[temp].append(element)
            else:
                # Anagrams[temp] 라는 key 가 없으므로 배열형태로 element를 추가한다.
                Anagrams[temp] = [element]
        # Anagrams.keys() 배열로 for문 수행
        for key in Anagrams.keys():
            # answer 배열에 Anagrams[key]에 대한 value값을 추가한다.
            answer.append(Anagrams[key])

        return answer


if __name__ == "__main__":
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strs))
