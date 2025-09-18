import numpy as np

random_matrix = np.random.randint(1, 11, size=(3, 3))
print("random_matrix:\n", random_matrix)

matrix_sum = np.sum(random_matrix)
print(f"\nSum of all elements in random_matrix: {matrix_sum}")

matrix_mean = np.mean(random_matrix)
print(f"\nMean of all elements in random_matrix: {matrix_mean}")

transposed_matrix = np.transpose(random_matrix)
print("\nTransposed matrix:\n", transposed_matrix)