# Delta Learning Algorithm Implementation

# Given feature vector x^T and class, we determine classification of faature vector over many epochs.

import numpy as np

# Theta = -0.5
theta = -0.5
# w_1 = -4.5
w1 = -4.5
# w_2 = -1.5
w2 = -1.5
# Learning rate = 1
n = 1

# Linear threshold unit has a transfer function which is a linear weighted sum of its inputs,
# and an activation function that is the Heaviside function (step function).
# For the Heaviside function make H(0) = 0.5. 
# So if the function is above 0.5, it is positive, and below it is negative. 
def heaviside(z):
    """Heaviside step function."""
    return 1 if z >= 0.5 else 0

# Feature vector x^T
# (0, 2) = 1
x1 = np.array([0, 2])
# (1, 2) = 1
# (2, 1) = 1
# (-3, 1) = 0
# (-2, -1) = 0
# (-3, -2) = 0 

# H(wx - theta)
# for w_1, we solve: 
z = np.dot(w1, x1) - theta

print(z)

# result = heaviside(z)

# print(result)