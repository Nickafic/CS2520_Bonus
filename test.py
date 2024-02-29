import timeit

def A(n1, n2):
    #A(0, n) = n + 1(for any integer n)
    if n1 < 0 and n2 < 0:
        return -1
    if n1 == 0:
        return n2 + 1
    elif n2 == 0:
        return A(n1 - 1, 1)
    else:
        return A(n1 - 1, A(n1, n2 - 1))
    #A(m + 1, 0) = A(m, 1)(m is a non - negative integer)
    #A(m + 1, n + 1) = A(m, A(m + 1, n))(m and n are non - negative integers)

def main():
    start = timeit.timeit()
    print(A(3, 6))

    print()

main()