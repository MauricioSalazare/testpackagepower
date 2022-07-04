import numpy as np
from testpackagepower import compute_function, load_line

if __name__ == "__main__":

    result = compute_function(2, 4)
    print(f"Result: {result}")

    # This is a shitty thing to do
    values = np.linspace(1, 10, 100)

    all_results = []
    for value in values:
        all_results.append(compute_function(value, value * 2))
    all_results = np.array(all_results)

    info = load_line()
    print(info)

