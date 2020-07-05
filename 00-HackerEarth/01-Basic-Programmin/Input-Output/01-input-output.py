class NumDeletionsToMakeAnagram:
    """
    Trick is to find num of common letters.
    You have to delete 
        len(a) + len(b) - (2*num_common_letters)
    """

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def solve(self):
        num_same_letters = 0
        s1 = {}

        # create letter-vs-num of occurances map (natural nums)
        for l1 in self.str1:
            if l1 in s1.keys():
                s1[l1] += 1
            else:
                s1[l1] = 1

        for l2 in self.str2:
            if l2 in s1.keys():
                s1[l2] -= 1
                num_same_letters += 1
                if s1[l2] == 0:
                    del s1[l2]

        return (len(self.str1)+len(self.str2)) - (num_same_letters*2)



if __name__ == '__main__':
    T = int(input())
    for test_case in range(0,T):
        a = input()
        b = input()
        soln = NumDeletionsToMakeAnagram(a, b)
        print(soln.solve())
