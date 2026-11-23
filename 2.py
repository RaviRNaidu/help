#PRUNING
def alphabeta(a, l, r, alpha, beta, maximizing):
    if l == r:
        return a[l]

    mid = (l+r)//2

    if maximizing:
        value = alphabeta(a, l, mid, alpha, beta, False)
        alpha = max(alpha, value)

        if alpha < beta:
            value = max(value, alphabeta(a, mid+1, r, alpha, beta, False))
        else:
            print("Right branch pruned")

    else:
        value = alphabeta(a, l, mid, alpha, beta, True)
        beta = min(beta, value)

        if beta > alpha:
            value = min(value, alphabeta(a, mid+1, r, alpha, beta, True))
        else:
            print("Right branch pruned")

    return value


a = list(map(int, input("Enter 8 leaf values: ").split()))

if len(a) == 8:
    print("Optimal value:", alphabeta(a, 0, 7, float('-inf'),
                                      float('inf'), True))
else:
    print("Enter exactly 8 values")