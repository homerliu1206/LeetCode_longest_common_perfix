class Solution:
    def longestCommonPrefix(self, strs):
        # cut the words
        alph = [] # little list
        big = [] # big list
        a = 0
        while a < len(strs):
            for line in strs[a]:
                alph.append(line)
            big.insert(a, alph)
            alph = []
            a += 1
        # print(big)

        # find the min length
        length = []
        b = 0
        while b < len(big):
            length.append(len(big[b]))
            b += 1
        # print(min(length))

        # fing the common perfix
        perfix = []
        check = []
        result = []
        if len(big) == 1:
            result = str(''.join(big[0]))
        elif len(big) >= 2:

            for i in range(min(length)):
                for x in range(len(big)):
                    if big[0][i] == big[x][i]:
                        check.append('True')
                    else:
                        check.append('False')
                if 'False' not in check:
                    perfix.append(big[0][i])
                else:
                    break
            result = str(''.join(perfix))
        # return result
        print(f"The lengest perfix is : {result}")

solution = Solution()
solution.longestCommonPrefix(['cir', 'car'])

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Input: strs = ["a"]
# Output: "a"