# https://www.codewars.com/kata/5469e0798a3502f4a90005c9
# Rotate an array ->
# data is the array, n is the numbers to rotate
# Example:
# with array [1, 2, 3, 4, 5]

# n = 1      =>    [5, 1, 2, 3, 4]
# n = 2      =>    [4, 5, 1, 2, 3]
# n = 3      =>    [3, 4, 5, 1, 2]
# n = 4      =>    [2, 3, 4, 5, 1]
# n = 5      =>    [1, 2, 3, 4, 5]
# n = 6      =>    [5, 1, 2, 3, 4]
# n = 0      =>    [1, 2, 3, 4, 5]
# n = -1     =>    [2, 3, 4, 5, 1]
# n = -2     =>    [3, 4, 5, 1, 2]
# n = -3     =>    [4, 5, 1, 2, 3]
# n = -4     =>    [5, 1, 2, 3, 4]
# n = -5     =>    [1, 2, 3, 4, 5]
# n = -6     =>    [2, 3, 4, 5, 1]

def positiveN(data, n, arr):
    if(n >= 0):
        for index, item in enumerate(data):
            if (index + n < len(data)):
                arr[index + n] = item
            else:
                arr[index - len(data) + n] = item

def negativeN(data, n, arr):
    if(n < 0):
        for index, item in enumerate(data):
            if (0 <= index + n < len(data)):
                arr[index + n] = item
            else:
                arr[(index + n - len(data)) % len(data)] = item

def rotate(data, n):
    if len(data) == 0:
        return []
    if (n > len(data)):
        n = n % len(data)

    arr = data.copy()

    positiveN(data, n, arr)
    negativeN(data, n, arr)

    return arr

print(1, rotate([1, 2, 3, 4, 5], 1))
print(2, rotate([1, 2, 3, 4, 5], 2))
print(3, rotate([1, 2, 3, 4, 5], 3))
print(4, rotate([1, 2, 3, 4, 5], 4))
print(5, rotate([1, 2, 3, 4, 5], 5))
print(6, rotate([1, 2, 3, 4, 5], 6))
print(0, rotate([1, 2, 3, 4, 5], 0))
print(-1, rotate([1, 2, 3, 4, 5], -1))
print(-2, rotate([1, 2, 3, 4, 5], -2))
print(-3, rotate([1, 2, 3, 4, 5], -3))
print(-4, rotate([1, 2, 3, 4, 5], -4))
print(-5, rotate([1, 2, 3, 4, 5], -5))
print(-6, rotate([1, 2, 3, 4, 5], -6))
print("true false", rotate([True, True, False], 2))
print(12478, rotate([1, 2, 3, 4, 5], 12478))
print("empty array", rotate([], 976999))
