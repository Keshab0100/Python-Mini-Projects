
def binary_search(a, low, high, target):
    if (high < low):
        return -1
    mid = (low+high)//2
    if (a[mid] == target):
        return mid
    elif (a[mid] > target):
        return binary_search(a, low, mid-1, target)
    else:
        return binary_search(a, mid+1, high, target)


if __name__ == '__main__':
    a = [1, 2, 3, 4, 6, 7, 4, 3, 2, 1]
    low = 0
    high = len(a)
    target = 7
    print(binary_search(a, low, high, target))
