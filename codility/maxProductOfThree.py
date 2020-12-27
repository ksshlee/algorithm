def solution(A):

    # A 정렬
    A.sort()

    if A[0]*A[1]*A[-1] > A[-1]*A[-2]*A[-3]:
        return A[0]*A[1]*A[-1]
    else:
        return A[-1]*A[-2]*A[-3]

