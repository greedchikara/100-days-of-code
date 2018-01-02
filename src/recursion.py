Iterative approach
def get_fib(position):
    if (position == 0):
        return 0
    if (position == 1):
        return 1

    fib_seq = [0, 1]

    for num in range(2, position):
        nextElement = fib_seq[num - 1] + fib_seq[num - 2]
        fib_seq.append(nextElement)
    return fib_seq

print get_fib(10)

# Recursive approach

def get_fib(position):
    if (position == 0 or position == 1):
        return position
    return get_fib(position - 1) + get_fib(position - 2)

print get_fib(6)
    
