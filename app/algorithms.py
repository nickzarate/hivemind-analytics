import numpy as np
from numpy import array, matmul, transpose
from numpy.linalg import inv

def phi_ols_estimator(covariates, p):
    X = array(covariates)
    X = np.column_stack((
        array(
            [1] * X.shape[0]
        ),
        X,
        X**2
    ))
    Xt = transpose(X)

    # phi = inv(Xt * X) * Xt * p
    phi = matmul(
        matmul(
            inv(
                matmul(
                    Xt,
                    X
                )
            ),
            Xt
        ),
        p
    )
    return phi
