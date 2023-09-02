import numpy as np
from est_homography import est_homography


def warp_pts(X, X_prime, interior_pts):
    """
    First compute homography from video_pts to logo_pts using X and X_prime,
    and then use this homography to warp all points inside the soccer goal

    Input:
        X: 4x2 matrix of (x,y) coordinates of goal corners in video frame
        X_prime: 4x2 matrix of (x,y) coordinates of logo corners in penn logo
        interior_pts: Nx2 matrix of points inside goal
    Returns:
        warped_pts: Nx2 matrix containing new coordinates for interior_pts.
        These coordinate describe where a point inside the goal will be warped
        to inside the penn logo. For this assignment, you can keep these new
        coordinates as float numbers.

    """

    # You should Complete est_homography first!
    H = est_homography(X, X_prime)




    ##### STUDENT CODE START #####
    # P = np.linalg.inv(H)

    # k = H[:-1]
    # J = []
    # J = [[k[0][0] / H[2][0], k[0][1] / H[2][1], k[0][2] / H[2][2]],
    #      [k[1][0] / H[2][0], k[1][1] / H[2][1], k[1][2] / H[2][2]]]
    interior_pts_t = np.transpose(interior_pts)
    l = np.ones((np.shape(interior_pts_t)))
    k = np.vstack((interior_pts_t, l))
    # k = np.hstack((interior_pts, l))
    o = k[:3]
    J = H @ o
    f = J[2:]
    warped_pts_1 = J/f
    warped_pts_2 = warped_pts_1[:2]
    warped_pts = np.transpose(warped_pts_2)
    
    ##### STUDENT CODE END #####

    return warped_pts
