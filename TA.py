def TDMA(lower_diag, main_diag, upper_diag, b): # size n - 1, n, n - 1, n
    n = len(b)
    x = [0] * n
    aplha = [upper_diag[0] / main_diag[0]]
    beta = [b[0] / main_diag[0]]

    for i in range(1, n - 1):
        aplha.append(upper_diag[i] / (main_diag[i] - lower_diag[i - 1] * aplha[i - 1]))
        beta.append((b[i] - lower_diag[i - 1] * beta[i - 1]) / (main_diag[i] - lower_diag[i - 1] * aplha[i - 1]))
    beta.append((b[n - 1] - lower_diag[n - 2] * beta[n - 2]) / (main_diag[n - 1] - lower_diag[n - 2] * aplha[n - 2]))

    x[n - 1] = beta[n - 1]

    for i in range(n - 1, 0, -1):
        x[i - 1] = beta[i - 1] - aplha[i - 1] * x[i]

    return x

