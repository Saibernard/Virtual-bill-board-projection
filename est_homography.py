import numpy as np


def est_homography(X, X_prime):
    """
    Calculates the homography of two planes, from the plane defined by X
    to the plane defined by X_prime. In this assignment, X are the coordinates of the
    four corners of the soccer goal while X_prime are the four corners of the penn logo

    Input:
        X: 4x2 matrix of (x,y) coordinates of goal corners in video frame
        X_prime: 4x2 matrix of (x,y) coordinates of logo corners in penn logo
    Returns:
        H: 3x3 homogeneours transformation matrix s.t. X_prime ~ H*X

    """

    ##### STUDENT CODE START #####

    A = np.ones((8, 9))

    A[0] = [-X[0][0], -X[0][1], -1, 0, 0, 0, X[0][0] * X_prime[0][0], X[0][1] * X_prime[0][0], X_prime[0][0]]
    A[1] = [0, 0, 0, -X[0][0], -X[0][1], -1, X[0][0] * X_prime[0][1], X[0][1] * X_prime[0][1], X_prime[0][1]]
    A[2] = [-X[1][0], -X[1][1], -1, 0, 0, 0, X[1][0] * X_prime[1][0], X[1][1] * X_prime[1][0], X_prime[1][0]]
    A[3] = [0, 0, 0, -X[1][0], -X[1][1], -1, X[1][0] * X_prime[1][1], X[1][1] * X_prime[1][1], X_prime[1][1]]
    A[4] = [-X[2][0], -X[2][1], -1, 0, 0, 0, X[2][0] * X_prime[2][0], X[2][1] * X_prime[2][0], X_prime[2][0]]
    A[5] = [0, 0, 0, -X[2][0], -X[2][1], -1, X[2][0] * X_prime[2][1], X[2][1] * X_prime[2][1], X_prime[2][1]]
    A[6] = [-X[3][0], -X[3][1], -1, 0, 0, 0, X[3][0] * X_prime[3][0], X[3][1] * X_prime[3][0], X_prime[3][0]]
    A[7] = [0, 0, 0, -X[3][0], -X[3][1], -1, X[3][0] * X_prime[3][1], X[3][1] * X_prime[3][1], X_prime[3][1]]

    [U,S,Vt] = np.linalg.svd(A)
    V = np.transpose(Vt)
    x = V[:, 8:]
    H = x.reshape(3, 3)




    ##### STUDENT CODE END #####

    return H




