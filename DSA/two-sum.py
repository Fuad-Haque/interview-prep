def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return []

print(two_sum([2, 7, 11, 15], 9))



def three_sum(numss, targett):
    for i in range(len(numss)):
        for j in range(i +1, len(numss)):
            for k in range(j + 1, len(numss)):
                if numss[i] + numss[j] + numss[k] == targett:
                    return [i, j, k]
    return []

print(three_sum([8, 9, 44, 55, 35, 45], 100))
