x = 0

while x < 5:
    print("x = " + str(x))
    x = x + 1

print("\nx= " + str(x))


my_variable = 0

while my_variable < 5:
    print("Hello world")
    my_variable += 1


# Fill in the blanks so that the while loop continues to run while the
# "divisor" variable is less than the "number" parameter.

def sum_divisors(number):
    # Initialize the appropriate variables
    divisor = 1
    total = 0

    # Avoid dividing by 0 and negative numbers
    # in the while loop by exiting the function
    # if "number" is less than one
    if number < 1:
        return 0

    # Complete the while loop
    while divisor < number:
        if number % divisor == 0:
            total += divisor
        # Increment the correct variable
        divisor += 1

    # Return the correct variable
    return total


print(sum_divisors(0))  # Should print 0
print(sum_divisors(3))  # Should print 1
# 1
print(sum_divisors(36))  # Should print 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should print 1+2+3+6+17+34+51
# 114
print("\n\n")
# -------------------------------------------------------------------


for x in range(5):
    print(x)

friends = ['Mertcan', 'Zafer', 'Mommy', 'Father']

print("\n\n")

for friend in friends:
    print(friend)


values = [12, 22, 2, 412, 2]

initialSum = 0
size = 0
average = 0.0


for val in values:

    initialSum += val
    size += 1

average = initialSum / size
print("Total sum: ", str(initialSum) + " - Average: ", str(average))
print("\n\n")


mult = 1

for i in range(1, 5):  # for(int i = 1; i < 5;i++)
    mult *= i  # 1 * 1  1 * 2  2 * 3   6 * 4

print(mult)
print("\n\n")


def to_celcsius(x):
    return (x - 32) * 5 / 9


for n in range(0, 101, 10):  # for(int n = 0; n < 101; n += 10)
    print(n, to_celcsius(n))

print("\n\n")
for left in range(0, 7):

    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" , ")
    print()

print("\n\n")
teams = ['Galatasaray', 'Fenerbahce', 'Besiktas', 'Trabzon']


for Outer in teams:
    for Inner in teams:
        if Inner != Outer:
            print(Outer + " x " + Inner, end=" , ")
    print()

# Write a function to find the intersection of two unsorted array


def Intersection(a, b):
    return [i for i in a if a in b]


a = [8, 2, 1, 4, 12, 5]
b = [9, 5, 4, 0, 2]

c = Intersection(a, b)

print(' '.join(map(str, c)))
