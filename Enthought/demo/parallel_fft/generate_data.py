"""
Generate a 500MB data file of 16-bit floating-point numbers.
"""
import numpy as np


def create_data(shape=(500, 500, 1000), dtype=np.float16):
    data = np.array(np.random.random(shape), dtype=dtype)
    return data


def write_data(data, filename='data.npy'):
    np.save(filename, data)


def main():
    data = create_data()
    write_data(data)
    
    
if __name__ == '__main__':
    main()