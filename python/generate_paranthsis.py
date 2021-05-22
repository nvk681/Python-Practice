def construct(list, opening, closing, max, string):
    if len(string) == max:
        list.append(string)
        return
    if opening == closing:
        construct(list, opening+1, closing, max, string+"(")
    else:
        if closing < opening:
            construct(list, opening, closing+1, max, string+")")
        if opening < max/2:
            construct(list, opening+1, closing, max, string+"(")

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        opening = 1
        closing = 0
        list = []
        string = "("
        construct(list, opening, closing, n*2, string)
        return list
    