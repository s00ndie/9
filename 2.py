def difference(*nums):
    if len(nums) ==0:
        result = 0
        return result
    elif len(nums) >1:
        n1 = min(nums)
        n2 = max(nums)
        result = n2 - n1
        if type(result) is float:
            result = round(result,2)

        return result

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
