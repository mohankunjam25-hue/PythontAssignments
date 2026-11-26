# 1. Nested Loops: Prime Numbers

for num in range(2, 51):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")




# 2. Fibonacci Sequence


first = 0
second = 1

for count in range(10):
    print(first, end=" ")

    next_number = first + second
    first = second
    second = next_number
