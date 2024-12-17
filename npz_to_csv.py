import os

import numpy as np
import pandas as pd

ignore_path = 'venv'

if __name__ == '__main__':
    base_path = input('Enter directory path for data conversion: ')

    for base_dir, _, files in os.walk(base_path):
        if 'venv' in base_dir:
            continue

        for file in files:
            if file.endswith('.npz'):
                base_file_name = file[:-4]

                output_file = os.path.join(base_dir, base_file_name + '.csv')

                print(f'Converting {base_dir} {file}...')

                arrays = dict()

                with np.load(os.path.join(base_dir, file)) as data_arrays:
                    for key in data_arrays:
                        arrays[key] = data_arrays[key]

                pd.DataFrame(arrays).to_csv(output_file, index=False)
