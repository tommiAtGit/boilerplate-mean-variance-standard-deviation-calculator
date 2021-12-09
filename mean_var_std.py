import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    aList = []

    newarr = np.array_split(list, 3)

    print(newarr)
    for array in newarr:
	    aList.append(array.tolist())
  
    print (aList)

    print("\n")
    print("**Mean**")
    mean_0 = np.mean(aList, axis = 0)
    mean_1 = np.mean(aList, axis = 1)
    mean =  np.mean(aList)
    means=[mean_0.tolist(),mean_1.tolist(), mean]
    print(means)

    print("\n")
    print("**Varance**")
    var_0 = np.var(aList, axis = 0)
    var_1 = np.var(aList, axis = 1)
    var =  np.var(aList)
    variances = [var_0.tolist(),var_1.tolist(), var]
    print(variances)

    print("\n")
    print("**Std deviation**")
    std_0 = np.std(aList, axis = 0)
    std_1 = np.std(aList, axis = 1)
    std =  np.std(aList)
    stdDevs = [std_0.tolist(),std_1.tolist(), std]
    print(stdDevs)

    print("\n")
    print("**Max**")
    max_0 = np.max(aList, axis = 0)
    max_1 = np.max(aList, axis = 1)
    maxs =  np.max(aList)
    max = [max_0.tolist(),max_1.tolist(), maxs]
    print(max)

    print("\n")
    print("**Min**")
    min_0 = np.min(aList, axis = 0)
    min_1 = np.min(aList, axis = 1)
    mins =  np.min(aList)
    min = [min_0.tolist(),min_1.tolist(), mins]
    print(min)

    print("\n")
    print("**sum**")
    sum_0 = np.sum(aList, axis = 0)
    sum_1 = np.sum(aList, axis = 1)
    sums =  np.sum(aList)
    sum = [sum_0.tolist(),sum_1.tolist(), sums]


    calculations={
        "mean": means,
        "variance":variances,
        "standard deviation" :stdDevs,
        "max":max,
        "min":min,
        "sum":sum
    }


    return calculations