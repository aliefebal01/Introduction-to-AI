import numpy as np

def regression_based_on_data(l, u, a, y):
    """
    Please modify the body of this function according to the description in exercise 2.1
    """
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
    # choose F different future functions : Phi_k(a)= a^k
    F = 4

    # A: n * F, A_ij = Phi_j(a_i)
    n = len(a)
    A = np.zeros((n, F))

    for i in range(n):
        for j in range(F):
            A[i, j] = a[i] ** j

    # a_hat = (A^T * A)^(-1) * A^T * y
    a_hat = np.dot(np.dot(np.linalg.inv(np.dot(A.transpose(), A)), A.transpose()), y)

    # 2. find a_max maximizing f_hat(a), a in [l, u]
    # f_hat(a) = sum_0^(F-1) a_hat_k * a^k

    a_max = None
    f_hat_max = -np.inf

    for i in range(n):
        if l <= a[i] <= u:
            f_hat = 0
            for k in range(F):
                f_hat += a_hat[k] * (a[i] ** k)
            if f_hat > f_hat_max:
                f_hat_max = f_hat
                a_max = a[i]
<<<<<<< Updated upstream

    return a_max
=======
    
    return a_max
    
>>>>>>> Stashed changes
