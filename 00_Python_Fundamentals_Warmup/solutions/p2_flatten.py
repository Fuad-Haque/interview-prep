"""Algorithm name: Iterative Unpacking/List Traversal"""

def flatten_bruteforce(nested):
    result = []
    for element in nested:
        if isinstance(element, list):
            for item in element:
                result.append(item)
        else:
            result.append(element)
    return result
print(flatten_bruteforce([[1,2], [3], [4,5,6]]))
print(flatten_bruteforce([[1,2], [3], [4,5], [6]]))
print(flatten_bruteforce([1, [2,3], [4, [5,6]]]))

def flatten_optimized(nessted):
    return [item for sublist in nessted for item in (sublist if isinstance(sublist, list) else [sublist])]
print(flatten_optimized([[1,2],[3],[4,5,6]]))          
print(flatten_optimized([[1,2],[3,[4,5]],[6]]))        
print(flatten_optimized([1, [2, 3], [4, [5, 6]]])) 