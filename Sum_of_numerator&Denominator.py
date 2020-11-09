from fractions import Fraction


def Probability(A,B):
    ratio = A/B
    p_q = Fraction(ratio).limit_denominator()
    new = str(p_q)
    li = new.split("/")
    ans = int(li[0]) + int(li[1])
    return ans

print(Probability(6, 9))
