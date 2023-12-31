import numpy as np


def calculate(list):
  if len(list) < 9:
    raise ValueError('List must contain nine numbers.')
  else:
    # initializing dictionary with None values:
    calculations = {
        'mean': None,
        'variance': None,
        'standard deviation': None,
        'max': None,
        'min': None,
        'sum': None
    }
    # Values for flattened matrix
    storage = np.array([list[0:3], list[3:6], list[6:9]])
    print(storage)
    storage_min = storage.min()
    storage_max = storage.max()
    storage_sum = storage.sum()
    storage_mean = storage.mean()
    storage_var = storage.var()
    storage_std = storage.std()

    # Values across the rows
    storage_min_row = storage.min(0)
    storage_max_row = storage.max(0)
    storage_sum_row = storage.sum(0)
    storage_mean_row = storage.mean(0)
    storage_var_row = storage.var(0)
    storage_std_row = storage.std(0)

    # Values across the columns
    storage_min_col = storage.min(1)
    storage_max_col = storage.max(1)
    storage_sum_col = storage.sum(1)
    storage_mean_col = storage.mean(1)
    storage_var_col = storage.var(1)
    storage_std_col = storage.std(1)

    # Update dictionary
    # .tolist() converts numpy array to python list
    calculations.update({
        "min":
        [storage_min_row.tolist(),
         storage_min_col.tolist(), storage_min]
    })
    calculations.update({
        "max":
        [storage_max_row.tolist(),
         storage_max_col.tolist(), storage_max]
    })
    calculations.update({
        "sum":
        [storage_sum_row.tolist(),
         storage_sum_col.tolist(), storage_sum]
    })
    calculations.update({
        "mean":
        [storage_mean_row.tolist(),
         storage_mean_col.tolist(), storage_mean]
    })
    calculations.update({
        "variance":
        [storage_var_row.tolist(),
         storage_var_col.tolist(), storage_var]
    })
    calculations.update({
        "standard deviation":
        [storage_std_row.tolist(),
         storage_std_col.tolist(), storage_std]
    })

    return calculations