def intersection(arrays):
    cache = {}
    result = []

    #mark all items based on how many times we see them
    for i in arrays:
        for j in i:
            #first time found
            if j not in cache:
                cache[j] = 1
            #subsequent findings, increase value to be greater than 1
            else:
                cache[j] += 1
    
    #build result list
    for key, value in cache.items():
        if value > 1:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
