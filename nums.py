def find_missing_nums(nums):
    lnums = len(nums)
    alnset = set(range(1, lnums + 1))

    for num in nums:
        if num in alnset:
            alnset.remove(num)

    return list(alnset)

print(find_missing_nums([2,3,1,1,3,6]))
print(find_missing_nums([2,1,1,1,1,6]))
print(find_missing_nums([2,1,1,1,1,1,4]))
