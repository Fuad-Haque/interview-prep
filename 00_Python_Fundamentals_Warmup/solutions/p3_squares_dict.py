"""Algorithm name: Dictionary comprehension with range()"""

def squares_dict(n):
    result = {}
    for i in range(1, n+1):
        result[i] = i**2
    return result
print(squares_dict(6))

def squaress_dict(m):
    return{j: j**2 for j in range(1, m+1)}
print(squaress_dict(7))


#1 Two Sum
def twoSum(numbers, target):
    number_map = {number: i for i, number in enumerate(numbers)}
    for i, number in enumerate(numbers):
        complement = target - number
        if complement in number_map and number_map[complement] != i:
            return [i, number_map[complement]]
    return []
print(twoSum([1, 2, 3, 4, 5], 9))