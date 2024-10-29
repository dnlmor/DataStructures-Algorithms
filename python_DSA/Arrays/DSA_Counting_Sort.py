def counting_sort(arr):
    max_val = max(arr) + 1
    count = [0] * max_val
    for num in arr:
        count[num] += 1
    i = 0
    for num, freq in enumerate(count):
        for _ in range(freq):
            arr[i] = num
            i += 1
