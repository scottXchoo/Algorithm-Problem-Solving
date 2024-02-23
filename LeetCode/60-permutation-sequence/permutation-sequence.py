class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        lists = []
        for i in range(n):
            lists.append(i+1)

        answer = ""
        permutation = permutations(lists, n)
        for idx, perm in enumerate(permutation):
            if idx + 1 == k:
                for p in perm:
                    answer += str(p)

        return answer