def read_matrix(name):
    print(f"请输入矩阵 {name} 的行数和列数（用空格隔开）：")
    rows, cols = map(int, input().split())

    print(f"请逐行输入 {rows} 行，每行 {cols} 个数字（用空格隔开）：")
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


def multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    C = []
    for i in range(rows_A):
        row = []
        for j in range(cols_B):
            total = 0
            for k in range(cols_A):
                total += A[i][k] * B[k][j]
            row.append(total)
        C.append(row)
    return C


print("=== 矩阵乘法计算器 ===")
A = read_matrix("A")
B = read_matrix("B")

C = multiply(A, B)
print("\n计算结果是：")
for row in C:
    print(row)