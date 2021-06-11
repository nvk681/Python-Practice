
def combinationSum2(numbers, target):
        total = sum(numbers)
        if total == target:
            return [numbers]
        if total < target:
            return []
        numbers.sort()
        res=set()
        get_set(numbers,target,[],res)
        return [list(i) for i in res]

def get_set(numbers, target, ls, res):
    if target==0:
        res.append(tuple(ls))
        return
    if target<0:
        return
    for i in range(len(numbers)):
        if target<numbers[i]: return
        get_set(numbers[i+1:],target-numbers[i],ls+[numbers[i]],res)
 
print(combinationSum2([10,1,2,7,6,1,5],8))