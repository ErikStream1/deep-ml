def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	
	if len(a[0]) != len(b): return -1
	
	ans = [0 for _ in range(len(b))]
	for i,v in enumerate(a):
		for j in range(len(b)):
			ans[i] += v[j] * b[j]
	
	return ans



	# import numpy as np
	# return np.array(a) @ np.array(b) if len(a) == len(b) else -1
