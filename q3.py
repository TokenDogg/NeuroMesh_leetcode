import numpy as np
def max_weight_subset(nums):
    candidates = []
    max_weight = -999999
    for i in nums:
        candidates.append([i])
    count = 0
    while len(candidates) > 0:
        subset = candidates.pop(0)
        weight = np.mean(subset) - np.median(subset)
        if weight > max_weight:
            max_weight = weight
        for i in candidates:
            if i == None:
                continue
            new = list(set(subset + i))
            new.sort()
            if new not in candidates:
                candidates.append(new)
    return max_weight

print(max_weight_subset([1,3,5,9]))
print(max_weight_subset([1,2,3,4]))