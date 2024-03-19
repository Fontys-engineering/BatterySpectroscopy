import numpy as np
import re

SPICE_REGEX = r"-?\d\.\d+e[+-]\d+"

def load_spice_data(file_path: str) -> np.ndarray:
    with open(file_path, "r") as file:
        data_length = sum(1 for _ in file) - 1
        file.seek(0)
        next(file)  # Skip header
        data_strings = (re.findall(SPICE_REGEX, line) for line in file)
        data = np.empty((data_length, 3), dtype=np.float64)
        for i, data_string in enumerate(data_strings):
            data[i] = np.fromiter(data_string, np.float64, count=3)
    data = data.transpose()
    data[1] = 10 ** (data[1]/20)  # Convert from logaritmic to linear
    return data

def load_AD2_data(file_path: str) -> np.ndarray:
    with open(file_path, "r") as file:
        data = np.genfromtxt(file, comments='#', delimiter=',',
                             skip_header=1).transpose()
        # Swap magnitude and phase indices
        data[[1, 2]] = data[[2, 1]]
    return data

def load_SDS_data(file_path: str) -> np.ndarray:
    with open(file_path, "r") as file:
        data = (np.genfromtxt(file, comments='#', delimiter=',')
                  .transpose())
    return data