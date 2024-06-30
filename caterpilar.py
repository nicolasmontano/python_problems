# caterpilar 1
def solution(M, A):
    N = len(A)
    last_occurrence = [-1] * (M + 1)
    start = 0
    count = 0

    for end in range(N):  # O(n)
        # check if in last_occurrence
        print("start:", start)
        if last_occurrence[A[end]] >= start:
            start = last_occurrence[A[end]] + 1  # updates start

        last_occurrence[A[end]] = end
        count += (end - start + 1)
        print(f"end:{end},dist:{(end - start + 1)},count:{count}")

    return count
