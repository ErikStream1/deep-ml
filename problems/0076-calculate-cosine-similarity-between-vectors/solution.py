import numpy as np

def cosine_similarity(v1, v2):

	return v1 @ v2 /( np.linalg.norm(v1, ord = 2) * np.linalg.norm(v2, ord = 2)) if len(v1) == len(v2) else -1
