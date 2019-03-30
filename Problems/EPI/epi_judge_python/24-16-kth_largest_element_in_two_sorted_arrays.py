from test_framework import generic_test


def find_kth_in_two_sorted_arrays(A, B, k):
    b = max(0, k - len(B))
    t = min(len(A), k)

    while b < t:
        x = b + (t - b) // 2

        A_x_1 = float('-inf') if x <= 0 else A[x - 1]
        A_x = float('inf') if x >= len(A) else A[x]

        B_k_x_1 = float('-inf') if k - x <= 0 else B[k - x - 1]
        B_k_x = float('inf') if k - x >= len(B) else B[k - x]

        if A_x < B_k_x_1:
            b = x + 1
        elif A_x_1 > B_k_x:
            t = x - 1
        else:
            return max(A_x_1, B_k_x_1)

    A_b_1 = float('-inf') if b <= 0 else A[b - 1]
    B_k_b_1 = float('-inf') if k - b - 1 < 0 else B[k - b - 1]

    return max(A_b_1, B_k_b_1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "24-16-kth_largest_element_in_two_sorted_arrays.py",
            'kth_largest_element_in_two_sorted_arrays.tsv',
            find_kth_in_two_sorted_arrays))
