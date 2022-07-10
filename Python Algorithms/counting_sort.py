def counting_sort(arr):
    maxEl = max(arr)
    countArrayLength = maxEl+1
    countArray = [0] * countArrayLength

    for el in arr:
        countArray[el] += 1

    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1]

    outputArray = [0] * len(arr)
    i = len(arr) - 1

    while i >= 0:
        currentEl = arr[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray
