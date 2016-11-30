def simple_mean(x, y):
    """Function that takes 2 numerical arguments and returns their mean.
    """
    mean = (x + y) / 2
    return mean


def advanced_mean(values):
    """Function that takes a list of numbers and returns the mean of all
    the numbers in the list.
    """
    total = 0
    for v in values:
        total += v
    mean = total / len(values)
    return mean

print("Mean of 2 & 3:", simple_mean(2, 3))
print("Mean of 8 & 10:", simple_mean(8, 10))
print("Mean of [2, 4, 6]", advanced_mean([2, 4, 6]))
print("Mean of values even numbers under 20:", advanced_mean(list(range(0, 20, 2))))
