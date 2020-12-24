def solution(X, A):
    # 0 이면 미방문
    # 1 이면 방문
    selected_leaves = [0] * X

    # 방문한 잎들의 개수
    total_count=0

    for idx,leaf in enumerate(A):
        # 미방문이면 방문에 체크와 방문한 잎들 +1
        if selected_leaves[leaf-1]==0:
            selected_leaves[leaf-1]+=1
            total_count+=1

        if total_count == X:
            return idx


    return -1

