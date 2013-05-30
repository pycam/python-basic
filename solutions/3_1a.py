def simple_mean(a, b):
    avg = (a + b) / 2.0
    return avg

def better_mean(numbers):
    total = 0.0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    return avg

result = simple_mean(5, 10)
print "Simple mean of 5 & 10:", result

num_list = [1,2,3,4,5,6]
result = better_mean(num_list)
print "Mean of", num_list, "=", result

num_tuple = (5,6,7,99)
result = better_mean(num_tuple)
print "Mean of", num_tuple, "=", result

