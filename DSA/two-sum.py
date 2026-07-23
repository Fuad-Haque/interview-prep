# optimized version 

"""One loop, running through nums once. Inside it, complement in seen is a dictionary check — this takes the same tiny amount of time whether seen has 10 items or 10 million. It doesn't get slower as the dictionary grows.
Time complexity: O(n) — where n is the length of nums. Work scales directly with input size: double the list, roughly double the work."""

def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return []

print(two_sum([2, 7, 11, 15], 9))


# brute force method - checks every possibility

"""Three loops, one inside another. For every i, it runs the whole j loop. For every j, it runs the whole k loop. That nesting is what makes the cost multiply rather than add.
Time complexity: O(n³) — where n is the length of numss. This is the key difference from Two Sum's brute force (which has O(n²), two nested loops for two numbers). Three Sum needs three loops for three numbers, so the cost goes up one more level: n × n × n."""

def three_sum(numss, targett):
    for i in range(len(numss)):
        for j in range(i +1, len(numss)):
            for k in range(j + 1, len(numss)):
                if numss[i] + numss[j] + numss[k] == targett:
                    return [i, j, k]
    return []

print(three_sum([8, 9, 44, 55, 35, 45, 56], 100))
