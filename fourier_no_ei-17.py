print(np.cos(beta) * (N / 2.), np.sin(beta) * (N / 2.))
# 7.25753794281 14.259317761
np.fft.fft(vec_v)
# array([-0.0000 +0.j    ,  7.2575+14.2593j,  0.0000 +0.j    ,
# 0.0000 +0.j    ,  0.0000 +0.j    ,  0.0000 +0.j    ,
# -0.0000 +0.j    ,  0.0000 -0.j    , -0.0000 -0.j    ,
# -0.0000 +0.j    , -0.0000 -0.j    ,  0.0000 +0.j    ,
# -0.0000 +0.j    ,  0.0000 -0.j    ,  0.0000 +0.j    ,
# 0.0000 +0.j    , -0.0000 +0.j    ,  0.0000 +0.j    ,
# 0.0000 -0.j    ,  0.0000 +0.j    , -0.0000 -0.j    ,
# 0.0000 +0.j    , -0.0000 +0.j    ,  0.0000 +0.j    ,
# -0.0000 +0.j    , -0.0000 +0.j    , -0.0000 -0.j    ,
# -0.0000 +0.j    ,  0.0000 -0.j    , -0.0000 +0.j    ,
# 0.0000 -0.j    ,  7.2575-14.2593j])
