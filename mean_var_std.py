import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    row1 = list[0:3]
    row2 = list[3:6]
    row3 = list[6:9]
    matrix = np.array([
        row1,
        row2,
        row3
    ])
    calculations = {}

    # Separate the values into their respective axis
    axis1 = matrix[:,0], matrix[:,1], matrix[:,2]
    axis2 = matrix[0,:], matrix[1,:], matrix[2,:]

    # Calculate the mean
    axis1_mean = []
    axis2_mean = []
    for array in axis1:
        axis1_mean.append(np.mean(array))
    for array in axis2:
        axis2_mean.append(np.mean(array))
    calculations['mean'] = [axis1_mean, axis2_mean, np.mean(list)]

    # Calculate the variance
    axis1_var = []
    axis2_var = []
    for array in axis1:
        axis1_var.append(np.var(array))
    for array in axis2:
        axis2_var.append(np.var(array))
    calculations['variance'] = [axis1_var, axis2_var, np.var(list)] 

    # Calculate standard deviation
    axis1_std = []
    axis2_std = []
    for array in axis1:
        axis1_std.append(np.std(array))
    for array in axis2:
        axis2_std.append(np.std(array))
    calculations['standard deviation'] = [axis1_std, axis2_std, np.std(list)]

    # Calculate the max value
    axis1_max = []
    axis2_max = []
    for array in axis1:
        axis1_max.append(np.max(array))
    for array in axis2:
        axis2_max.append(np.max(array))
    calculations['max'] = [axis1_max, axis2_max, np.max(list)]

    # Calculate the min
    axis1_min = []
    axis2_min = []
    for array in axis1:
        axis1_min.append(np.min(array))
    for array in axis2:
        axis2_min.append(np.min(array))
    calculations['min'] = [axis1_min, axis2_min, np.min(list)]

    # Calculate the sum
    axis1_sum = []
    axis2_sum = []
    for array in axis1:
        axis1_sum.append(np.sum(array))
    for array in axis2:
        axis2_sum.append(np.sum(array))

    calculations['sum'] = [axis1_sum, axis2_sum, np.sum(list)]

    return calculations

